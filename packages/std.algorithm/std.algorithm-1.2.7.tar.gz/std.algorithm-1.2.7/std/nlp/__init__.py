# -*- coding: UTF-8 -*-
import regex as re

def detect_language(text):
    if re.compile('\p{Han}{2,}').match(text):
        return 'cn'

    cn = 0
    en = 0

    mid = len(text) / 2
    for i, ch in enumerate(text):
        position_weight = (i - mid + 0.01) / mid
        position_weight = position_weight ** 2
        if re.compile('\p{Letter}').match(ch):
            if re.compile('\p{Han}').match(ch):
                cn += 8 * position_weight
            else:
                en += position_weight

        elif re.compile('\p{Number}').match(ch):
            if ord(ch) > 256:
                cn += 2 * position_weight
            else:
                en += position_weight

        elif re.compile('\p{Punctuation}').match(ch):
            if ord(ch) > 256:
                cn += 2 * position_weight
            else:
                en += position_weight

        elif re.compile('\p{Symbol}').match(ch):
            ...
        elif re.compile('\p{Separator}').match(ch):
            ...
        elif re.compile('\p{Mark}').match(ch):
            ...
        else:
            ...
            
    if cn > en:
        return 'cn'

    if en > cn:
        return 'en'
    
    return 'en'