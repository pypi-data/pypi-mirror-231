from types import FunctionType, MethodType
import numpy as np, regex as re
from std.data import numpify
import random, torch

class DataLoader:

    def __init__(self,
                 original_list,
                 x_name=None,
                 y_name=None,
                 batch_size=32,
                 dynamic_size=None,
                 shuffle=False,
                 numpify_x=None,
                 numpify_y=None,
                 sort=True,
                 reverse=False,
                 deepspeed=False):
        if dynamic_size:
            if isinstance(dynamic_size, (FunctionType, MethodType)):
                self.batch_size = batch_size
                self.dynamic_size = dynamic_size
            else:
                self.batch_size = dynamic_size
                self.dynamic_size = True
        else:
            self.batch_size = batch_size
            self.dynamic_size = False
            
        from inspect import isgenerator
        if isgenerator(original_list):
            original_list = [*original_list]
            
        if x_name is None:
            try:
                doc = original_list[0].__doc__.strip()
                args = eval(doc)
            except SyntaxError:
                args = [re.split('\s*:\s*', declspec)[0] for declspec in re.split('\s*,\s*', re.match('\w+\((.+)\)$', doc)[1])]
            
            *x_name, y_name = args
            if len(x_name) == 1:
                x_name = x_name[0]
        
        self.x_name = x_name
        if sort:
            self.original_list = original_list
            self.counting_sort(reverse=reverse)
        else:
            self.training_list = original_list

        self.y_name = y_name
        self.numpify_x = numpify_x
        self.numpify_y = numpify_y if y_name else None
        
        self.dataset = [self.to_tensor(batch) for batch in self.batches()]

        self.deepspeed = deepspeed
        if deepspeed:
            num_replicas = torch.distributed.get_world_size()
            global_rank = torch.distributed.get_rank()
            total_size = len(self.dataset)
            #if zero_stage is 2, drop last remainder of the dataset!
            total_size -= total_size % num_replicas
            self.dataset = self.dataset[global_rank:total_size:num_replicas]
            print('len(self.dataset) =', len(self.dataset))
        elif shuffle if y_name else False:
            self.shuffle(self.dataset)

    def predict(self, model, numpy=True): 
        return self.reorder(model.predict_generator(self), numpy=numpy)
    
    def reorder(self, y_pred, numpy=True):
        if not hasattr(self, 'original_list'):
            return y_pred
        
        for inst, result in zip(self.training_list, y_pred):
            inst.result = result
        y_pred = [inst.result for inst in self.original_list]
        
        if numpy:
            y_pred = np.array(y_pred)           
        return y_pred
        
    def counting_sort(self, reverse=False):
        if isinstance(self.x_name, str):
            self.training_list = counting_sort(self.original_list, self.x_name, reverse=reverse)
        else:
            training_list = self.original_list
            for x_name in self.x_name:
                training_list = counting_sort(training_list, x_name, reverse=reverse)
            self.training_list = training_list

    def __getitem__(self, index):
        return self.dataset[index]

    def get_memory_allocation(self, tensor):
        shape = get_tensor_shape(tensor)
        if isinstance(self.dynamic_size, (FunctionType, MethodType)):
            return self.dynamic_size(*shape)

        from _functools import reduce
        return reduce(lambda x, y: x * y, shape)
        
    def batches(self): 
        if self.dynamic_size:
            if isinstance(self.x_name, str):
                x_name = self.x_name
            else:
                x_name = self.x_name[0]
                
            memorySize = 0
            for inst in self.training_list:
                memorySize += self.get_memory_allocation(getattr(inst, x_name))

            memorySize /= len(self.training_list)
            batch_memory = self.batch_size * memorySize
            
            batch_size = self.batch_size
            _memorySize = self.get_memory_allocation(getattr(self.training_list[batch_size - 1], x_name))
            if _memorySize < memorySize:
                _batch_size = max(1, int(batch_memory / _memorySize))
                if _batch_size > batch_size:
                    batch_size = _batch_size
                    memorySize = _memorySize
                    print('initial batch_size =', batch_size)

            i = 0
            while i < len(self.training_list):
                _memorySize = self.get_memory_allocation(getattr(self.training_list[i + batch_size - 1], x_name))
                if _memorySize > memorySize:
                    _batch_size = max(1, int(batch_memory / _memorySize))
                    if _batch_size < batch_size:
                        batch_size = _batch_size
                        memorySize = _memorySize
                        print('adjust batch_size to', batch_size)
     
                yield self.training_list[i:i + batch_size]
                i += batch_size
        else: 
            for i in range(0, len(self.training_list), self.batch_size):
                yield self.training_list[i:i + self.batch_size]

    def shuffle(self):
        # print("shuffling the data")
        random.shuffle(self.dataset)

    def __len__(self):
        return len(self.dataset)

    def on_epoch_end(self):
        print('\none epoch has ended!')

    @staticmethod
    def format_sample(batch, attribute, format_func):
        sample = [getattr(s, attribute) for s in batch]
            
        batch = format_func(sample) if format_func else np.array(sample)
        if batch.dtype == object:
            return numpify(sample)
        return batch

    @staticmethod
    def format_data(batch, attributes, format_func):
        if isinstance(attributes, (list, tuple)):
            samples = []
            if isinstance(format_func, (list, tuple)):
                for attribute, format_func in zip(attributes, format_func):
                    samples.append(DataLoader.format_sample(batch, attribute, format_func))
            else:
                for attribute in attributes:
                    samples.append(DataLoader.format_sample(batch, attribute, format_func))
            return samples
        elif attributes:
            return DataLoader.format_sample(batch, attributes, format_func)

    def to_tensor(self, batch):
        args = self.numpify(batch)
        if isinstance(args, tuple):
            return tuple([self.from_numpy(arg) for arg in arg] if isinstance(arg, list) else self.from_numpy(arg) for arg in args)
        
        if isinstance(args, list):
            return tuple(self.from_numpy(arg) for arg in args)
        
        return self.from_numpy(args)
                
    def numpify(self, batch):
        assert batch is not None

        x_sample = self.format_data(batch, self.x_name, self.numpify_x)

        if self.y_name:
            y_sample = self.format_data(batch, self.y_name, self.numpify_y)
            return x_sample, y_sample
        return x_sample

    def from_numpy(self, ndarray):
        try:
            return torch.from_numpy(ndarray)
        except TypeError:
            ...


def counting_sort(original_list, attr, reverse=False, axis=0):
    training_list = []
    dicOfInstance = []
            
    for inst in original_list:
        tensor = getattr(inst, attr)
        seq_length = get_tensor_shape(tensor, axis)
        assert seq_length > 0
        
        if len(dicOfInstance) < seq_length:
            dicOfInstance += [None] * (seq_length - len(dicOfInstance))
            
        index = seq_length - 1
        
        if dicOfInstance[index] is None:
            dicOfInstance[index] = []
        
        dicOfInstance[index].append(inst)
        
    # concatenate all the instances order by seq_length
    # print('maximum seq_length =', len(dicOfInstance))
    
    for index in range(len(dicOfInstance)):
        if dicOfInstance[index] is not None:
            batches = dicOfInstance[index]
            if axis + 1 < len(get_tensor_shape(getattr(batches[0], attr))):
                batches = counting_sort(batches, attr, reverse=False, axis=axis + 1)
            training_list += batches
            
    if reverse:
        training_list.reverse()
        
    return training_list
    

def get_tensor_shape(tensor, axis=None):
    if axis is None:
        shape = []
        while isinstance(tensor, (list, tuple)):
            shape.append(len(tensor))    
            tensor = tensor[0]
            
        return shape

    else:
        for _ in range(axis):
            tensor = tensor[0]
        return len(tensor)

