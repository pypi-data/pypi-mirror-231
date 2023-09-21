import datetime, std, random, time, inspect, traceback, os, math, torch
from std import computed, Object
import numpy as np
from std.data import numpify
from _collections import defaultdict
from .data import DataLoader

def is_torch(model):
    # Method Resolution Order by C3 Linearization algorithm
    return any(str(t) == "<class 'torch.nn.modules.module.Module'>" for t in reversed(type(model).__mro__))

def set_cuda_visible_devices():
    CUDA_VISIBLE_DEVICES = os.environ.get('CUDA_VISIBLE_DEVICES')
    if CUDA_VISIBLE_DEVICES == '-1':
        print('use cpu memory')
    else:
        print('use gpu device')
        if not CUDA_VISIBLE_DEVICES:
            try:
                os.environ["CUDA_VISIBLE_DEVICES"] = availableGPU()
            except Exception as e:
                print(e)
                traceback.print_exc()

def selcect_single_free_device(ids):
    for i in range(len(ids)):
        try:
            file = f"cuda:{ids[i]}.lock"
            if os.path.exists(file):
                continue

            with open(file, 'w+') as _:
                return i
        except Exception as e:
            print(e)
            traceback.print_exc()
    print('failed to select a device id, returning -1')
    return -1

def availableGPU():
# pip dependency:
# pip install nvidia-ml-py3
    try:
        import pynvml  # @UnresolvedImport
        pynvml.nvmlInit()
    except Exception as e:
        print(e)
        traceback.print_exc()
        return -1
# shutil.copy('C:/Windows/System32/nvml.dll', 'C:/Program Files/NVIDIA Corporation/NVSMI/nvml.dll')
# fix: copy C:\Windows\System32\nvml.dll and paste to C:\Program Files\NVIDIA Corporation\NVSMI\nvml.dll

    maxFreeMemory = 0
    maxFreeMemoryID = 0
    for i in range(pynvml.nvmlDeviceGetCount()):
        print('the %dth GPU info:' % i)
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        print('used memory = ', meminfo.used / (1 << 20))
        print('free memory = ', meminfo.free / (1 << 20))
        print('total memory = ', meminfo.total / (1 << 20))
        if meminfo.free > maxFreeMemory:
            maxFreeMemoryID = i
            maxFreeMemory = meminfo.free

    print('GPU with the maximum Free Memory is %d, with Free Memory of %f MiB' % (maxFreeMemoryID, maxFreeMemory / (1 << 20)))
    
    ids = {maxFreeMemoryID}
    for i in range(pynvml.nvmlDeviceGetCount()):
        if i == maxFreeMemoryID:
            continue
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)        
        print('meminfo.free =', meminfo.free)
        print('maxFreeMemory * 0.9 =', maxFreeMemory * 0.9)
        if meminfo.free > maxFreeMemory * 0.99:
            ids.add(i)

    print('ids =', ids)

    if num_gpus := os.environ.get('num_gpus'):
        num_gpus = int(num_gpus)
        print('num_gpus =', num_gpus)
        ids = [id for id in ids if not os.path.exists(f'cuda:{id}.lock')]

        device_id = []
        for _ in range(num_gpus):
            index = selcect_single_free_device(ids)
            if index >= 0:
                device_id.append(ids.pop(index))

        device_id = ','.join([str(j) for j in device_id])
    else:
        device_id = [*ids][random.randrange(0, len(ids))]
        device_id = str(device_id)
    print('selected device_id =', device_id)

    return device_id

def initialize_vocab(file, start=2):
    index = start
    vocab = {}
    from std.file import Text
    for word in Text(file):
        assert word and word == word.strip()
        assert word not in vocab
        vocab[word] = index
        index += 1
    return vocab

def method_name(func): 
    if inspect.ismethod(func):
        self = func.__self__
        if hasattr(self, 'name'):
            name = self.name
        else:
            name = self.__class__.__name__
        
        return name + '.' + func.__func__.__name__
    
    if inspect.isfunction(func):
        return func.__qualname__
    
    return func.__qualname__

def print_decimal(avg):
    if abs(avg) > 1e-3:
        return '%.4f' % avg
    else:
        return '%.4e' % avg
           
def print_time(eta):
    if eta > 3600:
        return '%d:%02d:%02d' % (eta // 3600, (eta % 3600) // 60, eta % 60)
    elif eta > 60:
        return '%d:%02d' % (eta // 60, eta % 60)
    else:
        return '%ds' % eta

class SymbolicModel:
    
    def __init__(self, model=None):
        self.model = model
    
    def sanctity_check(self):
        if self.vocab:
            assert min(self.vocab.values()) == 2
            assert max(self.vocab.values()) == self.dimension - 1
        return True
        
    def initialize_vocab(self, start=2):
        self.vocab = initialize_vocab(self.vocabFile, start=start)
        self.sanctity_check()
        self.UNK_INDEX = 1
        
    @property
    def dimension(self):
        return len(self.vocab) + 2

    def string2id(self, s):
        assert len(s) > 0
        return [self.vocab.get(i, self.UNK_INDEX) for i in s]

    def string2ids(self, s):
        return [[self.vocab.get(c, self.UNK_INDEX) for c in w] for w in s]
        
    def preprocess(self):
        self.model.outputs
        self.model.make_substitutions()
        
    def state_dict(self, modelPath):
        print('loading', modelPath)
        import h5py
        with h5py.File(modelPath, mode='r') as f:
            return self.model.load_weights(f)

    def __call__(self, *inputs, **kwargs):
        with self.context(**kwargs):
            return self.forward(*inputs)
        
    def forward(self, *inputs):
        for symbol, data in zip(self.model.inputs, inputs):
            symbol.numpy = data
            for symbolic_size, size in zip(symbol.shape, data.shape):
                symbolic_size.numpy = np.array(size)
        
        outputs = self.model.outputs
        
        if isinstance(outputs, (tuple, list)):
            data = type(outputs)((type(output)(output.torch for output in output) if isinstance(output, (tuple, list)) else output.torch for output in outputs))
        else:
            data = outputs.torch
            
        return data


class KerasModel: 

    numpify_x = numpify
    device = None
    learning_rate = 5e-5
    weight_decay = 0.01
    gradient_accumulation_steps = 1
    callback = None

    @staticmethod
    def is_integer(data):
        if isinstance(data, (tuple, list)):
            return all(KerasModel.is_integer(d) for d in data)
        return isinstance(data, int)
    
    @staticmethod
    def numpify_y(arr):
        if KerasModel.is_integer(arr):
            return numpify(arr, mask_value=-100, dtype=np.int64)
        return numpify(arr)

    def __init__(self, **kwargs):
        if hasattr(self, 'model'):
            self.model.eval()
            if torch.cuda.is_available():
                self.model.to('cuda:0')
                self.device = torch.device("cuda", 0)

    def initialize_vocab(self, start=2):
        self.vocab = initialize_vocab(self.vocabFile, start=start)
        self.sanctity_check()
        self.UNK_INDEX = 1

    def sanctity_check(self):
        if self.vocab:
            assert min(self.vocab.values()) == 2
            assert max(self.vocab.values()) == self.dimension - 1
        return True

    def print_history(self, history, delimiter='\n'):
        length = len(history['loss'])
        
        arr = []
        for i in range(length):
            dic = {}
            for key, value in history.items():
                dic[key] = value[i]
            arr.append(str(dic))
        
        print(delimiter.join(arr))   
        print("printed at", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) 

    @property
    def dimension(self):
        return len(self.vocab) + 2

    def string2id(self, s):
        assert len(s) > 0
        return [self.vocab.get(i, self.UNK_INDEX) for i in s]

    @computed
    def metrics(self):
        if hasattr(self, 'loss'):
            loss = self.loss
            accuracy = self.accuracy
        else:
            output_layer = [layer for layer in self.model.layers if hasattr(layer, 'loss')]
            if not output_layer:
                output_layer = self.model
            elif len(output_layer) == 1:
                output_layer, = output_layer
                
            if isinstance(output_layer, list):
                loss = [layer.loss for layer in output_layer]
                accuracy = [layer.accuracy for layer in output_layer]
            else:
                loss = output_layer.loss
                accuracy = output_layer.accuracy
            
        return Object(loss=loss, accuracy=accuracy)
    
    @property
    def loss(self):
        return self.metrics['loss']
    
    @property
    def accuracy(self):
        return self.metrics['accuracy']
            
    def forward(self, x):
        return self.model.forward(x)

    def gradient_checkpointing_enable(self):
        self.model.gradient_checkpointing_enable()

    @std.Timer('training')
    def training(self, **kwargs):
        epochs = kwargs.pop('epochs', None) or getattr(self, 'epochs', 2)
        print('epochs =', epochs)
        
        batch_size = kwargs.pop('batch_size', None) or getattr(self, 'batch_size', 64)
        print('batch_size =', batch_size)
        
        training = kwargs.pop('training', 1)
        print('training =', training)
        
        device = self.device
        print("device =", device)

        learning_rate = kwargs.pop('learning_rate', None) or getattr(self, 'learning_rate', 5e-5)
        print("learning_rate =", learning_rate)
        
        dynamic_size = kwargs.pop('dynamic_size', None) or getattr(self, 'dynamic_size', None)
        print("dynamic_size =", dynamic_size)
        
        args = Object()
        args.deepspeed = kwargs.pop('deepspeed', None)
        from transformers import SchedulerType
        args.lr_scheduler_type = SchedulerType(kwargs.pop('lr_scheduler_type', 'cosine'))
        args.num_warmup_steps = kwargs.pop('num_warmup_steps', 0)
        args.gradient_accumulation_steps = kwargs.pop('gradient_accumulation_steps', 1)
        args.save_model_step = kwargs.pop('save_model_step', None)

        if args.deepspeed:
            #https://huggingface.co/docs/transformers/main_classes/deepspeed
            args.train_micro_batch_size_per_gpu = batch_size
            args.learning_rate = learning_rate
            args.weight_decay = kwargs.pop('weight_decay', 0.01)
            
            args.seed = kwargs.pop('seed', 1234)
            args.local_rank = kwargs.pop('local_rank', -1)
            args.disable_dropout = kwargs.pop('disable_dropout', True)
            args.offload = kwargs.pop('offload', None)
            args.zero_stage = kwargs.pop('zero_stage', 0)
            args.lora_dim = kwargs.pop('lora_dim', 0)
            args.lora_module_name = kwargs.pop('lora_module_name', '_proj')
            args.enable_tensorboard = kwargs.pop('enable_tensorboard', False)
            args.tensorboard_path = kwargs.pop('tensorboard_path', './')
            args.only_optimize_lora = kwargs.pop('only_optimize_lora', False)
            args.gradient_checkpointing = False if args.only_optimize_lora else kwargs.pop('gradient_checkpointing', False)
            args.modules_to_save = kwargs.pop('modules_to_save', '')
            args.fp16 = kwargs.pop('fp16', True)
            args.num_gpus = kwargs.pop('num_gpus', 1)
            
            args.device_rank = args.local_rank
            
            print("args.local_rank =", args.local_rank)
            if args.local_rank == -1:
                device = torch.device("cuda")
            else:
                torch.cuda.set_device(args.local_rank)
                device = torch.device("cuda", args.local_rank)
                # Initializes the distributed backend which will take care of sychronizing nodes/GPUs
                import deepspeed
                from deepspeed.utils.logging import logger
                logger.disabled = True
                deepspeed.init_distributed()
            self.device = device
            args.global_rank = torch.distributed.get_rank()
            print("args.global_rank =", args.global_rank)
            
            from .config import get_train_ds_config
            ds_config = get_train_ds_config(offload=args.offload,
                                            stage=args.zero_stage,
                                            enable_tensorboard=args.enable_tensorboard,
                                            tb_path=args.tensorboard_path,
                                            tb_name=type(self).__name__,
                                            fp16=args.fp16)
            ds_config['train_micro_batch_size_per_gpu'] = args.train_micro_batch_size_per_gpu
            ds_config['train_batch_size'] = args.train_micro_batch_size_per_gpu * torch.distributed.get_world_size() * args.gradient_accumulation_steps

            if args.zero_stage == 3:
                from transformers.deepspeed import HfDeepSpeedConfig
                dschf = HfDeepSpeedConfig(ds_config) #keep this object alive when loading weights into model
                self.model = type(self)(*self.args).model

            if args.lora_dim > 0:
                from .lora import convert_linear_layer_to_lora, only_optimize_lora_parameters
                self.model = convert_linear_layer_to_lora(self.model, args.lora_module_name, args.lora_dim)
                if args.only_optimize_lora:
                    self.model = only_optimize_lora_parameters(self.model, args.modules_to_save)
        
            set_random_seed(args.seed)
        
        generator = DataLoader(self.load_data(training, **kwargs),
                             batch_size=batch_size,
                             dynamic_size=dynamic_size,
                             numpify_x=self.numpify_x,
                             numpify_y=self.numpify_y,
                             deepspeed=args.deepspeed)

        if args.deepspeed:
            # Split weights in two groups, one with weight decay and the other not.
            optimizer_grouped_parameters = get_optimizer_grouped_parameters(self.model, args.weight_decay)
            from deepspeed.ops.adam import DeepSpeedCPUAdam#, FusedAdam
            AdamOptimizer = DeepSpeedCPUAdam if args.offload else torch.optim.AdamW
            optimizer = AdamOptimizer(optimizer_grouped_parameters,
                                      lr=args.learning_rate,
                                      betas=(0.9, 0.95))
            self.optimizer = optimizer
            
        elif hasattr(self, 'optimizer'):
            optimizer = self.optimizer
        else:
            optimizer = torch.optim.AdamW(self.grouped_parameters, learning_rate)
            self.optimizer = optimizer

        from transformers import get_scheduler
        lr_scheduler = get_scheduler(
            name=args.lr_scheduler_type,
            optimizer=optimizer,
            num_warmup_steps=args.num_warmup_steps,
            num_training_steps=epochs * math.ceil(len(generator) / args.gradient_accumulation_steps))
        
        self.lr_scheduler = lr_scheduler
        if args.deepspeed:
            self.model, self.optimizer, _, self.lr_scheduler = deepspeed.initialize(
                model=self.model,
                optimizer=optimizer,
                args=args,
                config=ds_config,
                lr_scheduler=self.lr_scheduler,
                dist_init_required=True)
            
            if args.gradient_checkpointing:
                self.gradient_checkpointing_enable()
        
        self.args = args
        def on_epoch_end(*_):
            self.save_weights()

        self.callback = LambdaCallback(on_epoch_end=on_epoch_end)
        
        if args.save_model_step:
            def on_batch_end(step):
                if (step + 1) % args.save_model_step == 0:
                    self.save_weights()

            setattr(self.callback, 'on_batch_end', on_batch_end)

        history = self.fit_generator(generator, epochs=epochs)
        
        self.print_history(history)

    @computed
    def is_ready_for_printing(self):
        if self.args.deepspeed:
            return self.args.global_rank <= 0
        return True

    def print(self, *args):
        if self.is_ready_for_printing:
            print(*args)

    def fit_generator(self,
            train_data,
            val_data=[],
            epochs=10,
            patience=5,
            monitor="val_loss",
            mode="min", 
            shuffle=True):
            
        history = {}
        for epoch in range(epochs):
            self.print("Epoch {0}/{1}\n".format(epoch + 1, epochs))

            if shuffle and hasattr(train_data, 'shuffle'):
                train_data.shuffle()
            
            train_metrics = EpochRunner(BatchRunner(instance=self, training=True))(train_data)
            self.callback.on_epoch_end()
                
            for name, metric in train_metrics.items():
                history[name] = history.get(name, []) + [metric]

            if val_data:
                val_epoch_runner = EpochRunner(BatchRunner(instance=self, training=False))
                with torch.no_grad():
                    val_metrics = val_epoch_runner(val_data)
                    
                val_metrics["epoch"] = epoch
                for name, metric in val_metrics.items():
                    self.history[name] = self.history.get(name, []) + [metric]
            
            # early-stopping -------------------------------------------------
            if not val_data:
                continue
            
            arr_scores = history[monitor]
            best_score_idx = np.argmax(arr_scores) if mode == "max" else np.argmin(arr_scores)
            if best_score_idx == len(arr_scores) - 1:
                print("<<<<<< reach best {0} : {1} >>>>>>".format(monitor, arr_scores[best_score_idx]), file=sys.stderr)
            if len(arr_scores) - best_score_idx > patience:
                print("<<<<<< {} without improvement in {} epoch, early stopping >>>>>>".format(monitor, patience), file=sys.stderr)
                break
 
        return history

    @std.Timer('evaluate')
    def evaluate(self, **kwargs):
        batch_size = kwargs.pop('batch_size', None) or getattr(self, 'batch_size', 64)
        print('batch_size =', batch_size)
        
        training = kwargs.pop('training', 0)
        print('training =', training)
        
        device = self.device
        print("device =", device)

        fp16 = kwargs.pop('fp16', None)
        generator = DataLoader(self.load_data(training, **kwargs),
                             batch_size=batch_size,
                             numpify_x=self.numpify_x,
                             numpify_y=self.numpify_y)
        
        return EpochRunner(BatchRunner(instance=self, training=False))(generator)

    @std.Timer('predict')
    def predict(self, inputs, **kwargs):
        batch_size = kwargs.pop('batch_size', None)
        if batch_size is None:
            batch_size = len(inputs)

        sort = kwargs.get('sort', False)
        generator = DataLoader(inputs,
                             batch_size=batch_size,
                             numpify_x=self.numpify_x,
                             numpify_y=self.numpify_y,
                             sort=sort)

        return EpochRunner(BatchRunner(instance=self, training=False)).predict(generator)

    def load_weights(self):
        print('\nloading model from', self.modelFile)
        import h5py
        with h5py.File(self.modelFile, 'r') as f:
            self.iostream(self.model, f, mode='r')
            
    @property
    def iostream(self):
        from .torch.hdf5 import iostream
        iostream = torch.no_grad()(iostream)
        
    def save_weights(self):
        modelFile = self.modelFile
        self.print('\nsaving model to', modelFile)
        import os
        from std.file import createNewPath
        createNewPath(os.path.dirname(modelFile))

        if modelFile.endswith('.h5'):
            import h5py
            with h5py.File(modelFile, 'w') as f:
                self.iostream(self.model, f, mode='w')

        elif modelFile.endswith('.pt'):
            torch.save(self.model, modelFile)

        elif modelFile.endswith('.bin'):
            args = self.args
            if args.deepspeed:
                from .lora import convert_lora_to_linear_layer
                self.model = convert_lora_to_linear_layer(self.model)

                if args.global_rank == 0:
                    save_hf_format(self.model, modelFile)

                if args.zero_stage == 3:
                    # for zero stage 3, each gpu only has a part of the model, so we need to save the model on each gpu by using DS-Engine
                    save_zero_three_model(self.model,
                                          args.global_rank,
                                          modelFile,
                                          zero_stage=args.zero_stage)
            else:
                torch.save(self.model.state_dict(), modelFile)

    @property
    def grouped_parameters(self):
        decay, nondecay = std.array_split(self.model.parameters(), lambda p : len(p.shape) > 1)
        return [
            {
                "params": decay,
                "weight_decay": self.weight_decay,
            },
            {
                "params": nondecay,
                "weight_decay": 0.0,
            }
        ]


class Callback(object):
    """Abstract base class used to build new callbacks.
    """

    def __init__(self):
        self.validation_data = None
        self.model = None

    def set_params(self, params):
        self.params = params

    def set_model(self, model):
        self.model = model

    def on_batch_begin(self, batch, logs=None):
        """A backwards compatibility alias for `on_train_batch_begin`."""

    def on_batch_end(self, batch, logs=None):
        """A backwards compatibility alias for `on_train_batch_end`."""

    def on_epoch_begin(self, epoch, logs=None):
        """Called at the start of an epoch.
        """

    def on_epoch_end(self, epoch, logs=None):
        """Called at the end of an epoch.
        """

    def on_train_batch_begin(self, batch, logs=None):
        """Called at the beginning of a training batch in `fit` methods.
        """
        # For backwards compatibility
        self.on_batch_begin(batch, logs=logs)

    def on_train_batch_end(self, batch, logs=None):
        """Called at the end of a training batch in `fit` methods.
        """
        # For backwards compatibility
        self.on_batch_end(batch, logs=logs)

    def on_test_batch_begin(self, batch, logs=None):
        """Called at the beginning of a batch in `evaluate` methods.
        """

    def on_test_batch_end(self, batch, logs=None):
        """Called at the end of a batch in `evaluate` methods.
        """

    def on_predict_batch_begin(self, batch, logs=None):
        """Called at the beginning of a batch in `predict` methods.
        """

    def on_predict_batch_end(self, batch, logs=None):
        """Called at the end of a batch in `predict` methods.
        """

    def on_train_begin(self, logs=None):
        """Called at the beginning of training.
        """

    def on_train_end(self, logs=None):
        """Called at the end of training.
        """

    def on_test_begin(self, logs=None):
        """Called at the beginning of evaluation or validation.
        """

    def on_test_end(self, logs=None):
        """Called at the end of evaluation or validation.
        """

    def on_predict_begin(self, logs=None):
        """Called at the beginning of prediction.
        """

    def on_predict_end(self, logs=None):
        """Called at the end of prediction.
        """


class LambdaCallback(Callback):
    r"""
    Create a simple callback on the fly using lambda functions.
    """

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if v is not None:
                setattr(self, k, v)


class EpochRunner:

    def __init__(self, batch_runner):
        self.batch_runner = batch_runner
        if self.training:
            batch_runner.model.train()
        else:
            batch_runner.model.eval()
        
    width = 30
    
    def __call__(self, dataloader):
        total_loss = 0
        total_count = 0
        
        loss_dict = defaultdict(float)
        accuracy_dict = defaultdict(float)
        
        target = len(dataloader)
        total_time = 0
        from tqdm import tqdm
        pbar = tqdm(dataloader, bar_format='{desc}')
        for current, batch in enumerate(pbar):
            if isinstance(self.device, torch.device):
                if isinstance(batch, tuple):
                    batch = [*batch]

                for i, data in enumerate(batch):
                    if isinstance(data, (list, tuple)):
                        data = [data.to(self.device) for data in data]
                    else:
                        if data.dtype == torch.int:
                            data = data.long()
                        data = data.to(self.device)
                    batch[i] = data

            time_start = time.time()

            current += 1
            if self.training:
                try:
                    loss_per_batch, loss_items, accuracy_items = self.batch_runner(*batch)
                except Exception as e:
                    print(e)
                    features, y_true = batch
                    if not isinstance(features, list):
                        features = [features]
                    for data in features:
                        print(data.dtype, data.shape)
                    traceback.print_exc()
                    continue
            else:
                with torch.no_grad():
                    args = self.batch_runner(*batch)
                    if self.batch_runner.loss:
                        loss_per_batch, loss_items, accuracy_items = args
                    else:
                        return args

            total_loss += loss_per_batch.sum().item()
            total_count += loss_per_batch.numel()
        
            for name, val in loss_items.items():
                loss_dict[name] += val.sum().item()
                
            for name, val in accuracy_items.items():
                if val.dtype == torch.bool:
                    val = val.float()
                accuracy_dict[name] += val.sum().item()

            history = dict(loss=total_loss / total_count)
            historyLoss = {name: value / total_count for name, value in loss_dict.items()}
            history.update(**historyLoss)
            
            historyAccuracy = {name: value / total_count for name, value in accuracy_dict.items()}
            history.update(**historyAccuracy)
            
            bar = '%%%dd/%d' % (int(np.floor(np.log10(target))) + 1, target) % current
            
            prog = float(current) / target
            prog_width = int(self.width * prog)
            
            progress_bar = ''
            if prog_width > 0:
                progress_bar += ('=' * (prog_width - 1))
                if current < target:
                    progress_bar += '>'
                else:
                    progress_bar += '='
                    
            progress_bar += '.' * (self.width - prog_width)
            
            strs = [f'{bar} [{progress_bar}]', '', f"loss: {print_decimal(history['loss'])}"]
            
            if len(historyLoss) > 1:
                strs += [f"{name}: {print_decimal(value)}" for name, value in historyLoss.items()]

            strs += [f"{name}: {print_decimal(value)}" for name, value in historyAccuracy.items()]
            
            total_time += time.time() - time_start
            ETA = (target - current) * total_time / current
            strs[1] = f'ETA: {print_time(ETA)}'
            if self.args.deepspeed:
                strs.append(f'at rank: {self.args.global_rank}')
            pbar.set_description_str(' - '.join(strs))
            self.callback.on_batch_end(current)

        return history

    def predict_single(self, batch):
        if isinstance(self.device, torch.device): 
            if isinstance(batch, tuple):
                batch = [*batch]

            for i, data in enumerate(batch):
                if data is None:
                    continue

                if isinstance(data, (list, tuple)):
                    data = [data.to(self.device) for data in data]
                else:
                    if data.dtype == torch.int:
                        data = data.long()
                    data = data.to(self.device)
                batch[i] = data

        with torch.no_grad():
            return self.batch_runner(*batch)

    def predict(self, dataloader):
        if len(dataloader) > 1:
            from tqdm import tqdm
            dataloader = tqdm(dataloader)
        return torch.vstack([self.predict_single(batch) for batch in dataloader])

    @computed
    def device(self):
        return self.batch_runner.device
    
    @computed
    def training(self):
        return self.batch_runner.training

    @computed
    def is_ready_for_printing(self):
        return self.batch_runner.is_ready_for_printing

    @computed
    def args(self):
        return self.batch_runner.args

    @computed
    def callback(self):
        return self.batch_runner.callback


class BatchRunner:

    def __init__(self, instance, training=True):
        self.instance = instance
        self.training = training
        if training:
            self.accumulation_step = 0
    
    @computed
    def model(self):
        return self.instance.model
    
    @computed
    def args(self):
        return self.instance.args
    
    @computed
    def is_ready_for_printing(self):
        return self.instance.is_ready_for_printing
    
    @computed
    def loss(self):
        return self.instance.metrics.loss
    
    @computed
    def accuracy(self):
        return self.instance.metrics.accuracy
    
    @computed
    def optimizer(self):
        return self.instance.optimizer

    @computed
    def lr_scheduler(self):
        return self.instance.lr_scheduler

    @computed
    def device(self):
        return self.instance.device
    
    @computed
    def callback(self):
        return self.instance.callback
    
    @computed
    def gradient_accumulation_steps(self):
        return self.instance.gradient_accumulation_steps

    def forward(self, *args):
        return self.instance.forward(*args)

    def __call__(self, features, y_true):
        #import pydevd; pydevd.settrace('192.168.5.21')
        try:
            y_pred = self.forward(*features) if isinstance(features, list) else self.forward(features)
        except RuntimeError as e:
            if "out of memory" in str(e):
                if hasattr(torch.cuda, 'empty_cache'):
                    torch.cuda.empty_cache()
            
            traceback.print_exc()
            raise e
        except Exception as e:
            traceback.print_exc()
            raise e
        
        if y_true is None:
            return y_pred

        if isinstance(self.loss, (list, tuple)):
            loss_dict = {method_name(loss_fn): loss_fn(y_true, y_pred) for loss_fn, y_true, y_pred in zip(self.loss, y_true, y_pred)}
        else:
            loss_dict = {method_name(self.loss): self.loss(y_true, y_pred)}

        loss = sum(loss_dict.values())
        if self.training and self.optimizer is not None:
            loss_mean = torch.mean(loss)
        
            if torch.isnan(loss_mean):
                print(loss_mean + 'is nan, stop training')
                raise Exception('nan error') 
            # backward()
            if self.args.deepspeed:
                self.model.backward(loss_mean)
                self.model.step()
            else:
                if self.gradient_accumulation_steps > 1:
                    loss_mean = loss_mean / self.gradient_accumulation_steps

                self.accumulation_step += 1
                loss_mean.backward()

                if self.accumulation_step == self.gradient_accumulation_steps:
                    self.optimizer.step()
                    try:
                        lr_scheduler = self.lr_scheduler
                        if lr_scheduler is not None:
                            lr_scheduler.step()# Update learning rate schedule
                    except AttributeError:
                        ...

                    self.optimizer.zero_grad()
                    self.accumulation_step = 0

        if isinstance(self.accuracy, dict):
            step_metrics = {name: metric_fn(y_true, y_pred) for name, metric_fn in self.accuracy.items()}
        elif isinstance(self.accuracy, (list, tuple)):
            step_metrics = {method_name(metric_fn): metric_fn(y_true, y_pred) for metric_fn, y_true, y_pred in zip(self.accuracy, y_true, y_pred)}
        else:
            step_metrics = {'accuracy': self.accuracy(y_true, y_pred)}
        
        return loss, loss_dict, step_metrics

def set_random_seed(seed):
    if seed is not None:
        from transformers import set_seed
        set_seed(seed)
        random.seed(seed)
        np.random.seed(seed)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

def get_optimizer_grouped_parameters(
    model,
    weight_decay,
    lora_lr=5e-4,
    no_decay_name_list=["bias", "LayerNorm.weight"],
    lora_name_list=["lora_right_weight", "lora_left_weight"],
):
    optimizer_grouped_parameters = [
        {
            "params": [
                p for n, p in model.named_parameters()
                if (not any(nd in n for nd in no_decay_name_list)
                    and p.requires_grad and not any(nd in n
                                                    for nd in lora_name_list))
            ],
            "weight_decay":
            weight_decay,
        },
        {
            "params": [
                p for n, p in model.named_parameters()
                if (not any(nd in n for nd in no_decay_name_list)
                    and p.requires_grad and any(nd in n
                                                for nd in lora_name_list))
            ],
            "weight_decay":
            weight_decay,
            "lr":
            lora_lr
        },
        {
            "params": [
                p for n, p in model.named_parameters()
                if (any(nd in n
                        for nd in no_decay_name_list) and p.requires_grad)
            ],
            "weight_decay":
            0.0,
        },
    ]
    if not optimizer_grouped_parameters[1]["params"]:
        optimizer_grouped_parameters.pop(1)
    return optimizer_grouped_parameters

def save_hf_format(model, output_model_file):
    # used to save huggingface format, so we can use it for hf.from_pretrained
    model_to_save = model.module if hasattr(model, 'module') else model
    save_dict = model_to_save.state_dict()
    for key in list(save_dict.keys()):
        if "lora" in key:
            del save_dict[key]
    torch.save(save_dict, output_model_file)


def save_zero_three_model(model_ema, global_rank, output_model_file, zero_stage=0):
    zero_stage_3 = (zero_stage == 3)
    model_to_save = model_ema.module if hasattr(model_ema, 'module') else model_ema
    if not zero_stage_3:
        if global_rank == 0:
            torch.save(model_to_save.state_dict(), output_model_file)
    else:
        import deepspeed
        from .lora import _z3_params_to_fetch
        output_state_dict = {}
        for k, v in model_to_save.named_parameters():
            if hasattr(v, 'ds_id'):
                with deepspeed.zero.GatheredParameters(_z3_params_to_fetch([v]), enabled=zero_stage_3):
                    v_p = v.data.cpu()
            else:
                v_p = v.cpu()
            if global_rank == 0 and "lora" not in k:
                output_state_dict[k] = v_p
        if global_rank == 0:
            torch.save(output_state_dict, output_model_file)
        del output_state_dict
