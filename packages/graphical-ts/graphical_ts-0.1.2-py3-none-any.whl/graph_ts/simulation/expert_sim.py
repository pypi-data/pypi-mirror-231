## Expert Simulation

# 1. the future value is last value / average of historical values + positive/negative effect as VELOCITY!

# 2. requiement: 
    # implement the mode "velcity" for edge function
    
from .dgcm import DGCM
from ..mapping.edge_function import EdgeFunction
from ..misc.utils import *
import inspect


@check_len
@check_binary
def bin2cont(x, scale, effect_len, effect_type='grad'):
    diff = x[-1] - x[0] # -1, 0, 1
    if effect_type == 'diff':
        return diff * rise(scale, effect_len)    
    if effect_type == 'grad':
        return diff * scale * np.ones(effect_len)
    
@check_len
def cat2cont(x, scale, effect_len, effect_type='grad'):
    end_state = x[-1]
    scl = scale[end_state]
    
    return bin2cont(x, scl, effect_len, effect_type)    

def cont2cont(x, scale, effect_len, effect_type='grad'):
    return np.ones(effect_len) * mean_grad(x, scale)


@check_binary
def bin2cat(x, target_value): # indim = outdim = 1
    return x * target_value

def cat2cat(x, mapping): # indim = outdim = 1
    return mapping[x]

def cont2cat(x, spectrum):
    return group_it(x, spectrum) # indim = outdim = 1

@check_binary
def bin2bin(x, flip=False): # indim = outdim = 1
    if flip:
        return 1 - x
    else: 
        return x

def cat2bin(x, catogory):
    return np.isin(x, catogory)

def cont2bin(x, up, low):
    return bound_it(x, up, low)




def extract_args(func):
    """Extract arguments of a function except 'x'"""
    args = inspect.getfullargspec(func).args
    return [arg for arg in args if arg != 'x']

class ExpertSim(DGCM):
    CONT = 'continuous'
    CAT = 'categorical'
    BIN = 'binary'
    TYP_SET = {'continuous', 'categorical', 'binary'}
    
    MATCH_TYPE = {
        (CONT, CONT): {
            'fn': cont2cont, 
            'arg_names': extract_args(cont2cont)
        },
        (CONT, BIN): {
            'fn': cont2bin,
            'arg_names': extract_args(cont2bin)
        },
        (CONT, CAT): {
            'fn': cont2cat,
            'arg_names': extract_args(cont2cat)
        },
        (BIN, CONT): {
            'fn': bin2cont,
            'arg_names': extract_args(bin2cont)
        },
        (BIN, BIN): {
            'fn': bin2bin,
            'arg_names': extract_args(bin2bin)
        },
        (BIN, CAT): {
            'fn': bin2cat,
            'arg_names': extract_args(bin2cat)
        },
        (CAT, CONT): {
            'fn': cat2cont,
            'arg_names': extract_args(cat2cont)
        },
        (CAT, BIN): {
            'fn': cat2bin,
            'arg_names': extract_args(cat2bin)
        },
        (CAT, CAT): {
            'fn': cat2cat,
            'arg_names': extract_args(cat2cat)
        }
    }
    
    def add_edge(self, u, v, lag=0, 
                 input_len=1,
                 scale=1, effect_len=1,
                 up=np.inf, low=-np.inf,
                 category=None,
                 target_value=None,
                 flip=False,
                 mapping=None,
                 spectrum=None,
                 gauss_loc=0,
                 gauss_scl=1,
                 rng=None,
                 mode=None,
                 **attr):
        
        u_typ = self.nodes[u]['type']
        v_typ = self.nodes[v]['type']
    
        
        _fn = ExpertSim.MATCH_TYPE[(u_typ, v_typ)]['fn']
        _efn_params = dict(indim=input_len, 
                           gauss_loc=gauss_loc, 
                           gauss_scl=gauss_scl, 
                           rng=rng)
        
        if v_typ == ExpertSim.CONT:
            _mode = mode if mode is not None else 'grad'
            _efn_params.update(dict(outdim=effect_len, 
                                    scale=scale,
                                    mode=_mode,
                                    effect_len=effect_len,
                                    effect_type=_mode))
        
        if v_typ == ExpertSim.CAT:
            _efn_params.update(dict(mode='value'))
            if u_typ == ExpertSim.CAT: _efn_params.update(dict(mapping=mapping))
            if u_typ == ExpertSim.BIN: _efn_params.update(dict(target_value=target_value))
            if u_typ == ExpertSim.CONT: _efn_params.update(dict(spectrum=spectrum))
            
        if v_typ == ExpertSim.BIN:
            _efn_params.update(dict(mode='value'))
            if u_typ == ExpertSim.CAT: _efn_params.update(dict(category=category))
            if u_typ == ExpertSim.BIN: _efn_params.update(dict(flip=flip))
            if u_typ == ExpertSim.CONT: _efn_params.update(dict(up=up, low=low))
        
        _efn = EdgeFunction(function=_fn, **_efn_params)

        key = super().add_edge(u, v, lag, **attr)
        
        self.assign_edge_with_fn(u, v, func=_efn, lag=lag)
        
        return key

            
        



