''' Utilities for ML models '''
import numpy as np
import json
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator
from rsi_dstools.mlutils.multi_model import MultipleOutputModel


def jstringify_model_object(mdl, string=False, simple_jsonify=False):
    if isinstance(mdl,MultipleOutputModel):
        output = {tag: jstringify_model_object(model, string=string, simple_jsonify=simple_jsonify) 
            for tag, model in mdl.items()}
        if string:
            output = str(output)
        return output
    if isinstance(mdl,Pipeline):
        terms = []
        order = {}
        for i, step in enumerate(mdl.steps):
            if string:
                term = ' '.join([el.strip() for el in str(step).split('\n')])
            else:
                term = {f'step_{i}_{step[0]}': jstringify_model_object(
                    step[1], string=string, simple_jsonify=simple_jsonify)}
            if not(simple_jsonify) and ((step[1].__name__ in ['TfidfVectorizer', 'CountVectorizer'])  or
                    isinstance(step[1], BaseEstimator)):

                comp, _order = make_dict_from_obj(step[1], order=order, remove_keys=['_stop_words_id'])
                order.update(_order)
                if string:
                    term = ' '.join([str(step[0]).strip(), str(comp)])
                else:
                    term = {f'step_{i}_{step[0]}': comp}
            terms.append(term)
        if string:
            return ' --> '.join(terms)
        else:
            return terms
    else:
        comp, _ = make_dict_from_obj(mdl)
        if string:
            comp = str(comp)
        return comp

def make_dict_from_obj(obj, order={}, remove_keys=[]):
    ''' Attempt to create a approx JSON-able  
        representation of the input object.
    '''
    d = {}
    keys_sort_idx = {}
    for k, v in obj.__dict__.items():
        if k in remove_keys:
            continue
        elif isinstance(v, np.ndarray):
            d[k] = v.round(6).tolist()
        elif isinstance(v,dict):
            ndict = {}
            keys = list(v.keys())
            if k in order and len(order[k]) == len(keys):
                order = order[k]
            else:
                order = np.argsort(keys)
            for kk in [keys[o] for o in order]:
                try:
                    json.dumps(v[kk])
                except TypeError:
                    pass
                else:
                    ndict[kk] = v[kk]
            d[k] = ndict
            keys_sort_idx[k] = order
        else:
            try:
                json.dumps(v)
            except TypeError:
                continue
            d[k] = v
    return d, keys_sort_idx
