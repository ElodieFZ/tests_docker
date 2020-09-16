def _lowercase(obj):
    """ Make all keys from a dictionary lowercase 
    (ok for nested dictionaries, but will not work for dictionaries within lists) """
    if isinstance(obj, dict):
        return {k.lower():_lowercase(v) for k, v in obj.items()}
    else:
        return obj


def _merge_dicts(d1, d2):
    """
    Merge dictionaries d1 and d2 with values from d1 overwritten by d2 if exists in both dictionaries.
    Merging includes nested dictionaries.
    Dictionnary d1 will contain the merged dictionary.
    Raises error if one key contains a dict in one dict but no in the other.
    """
    out = d1
    for k in d2:
        if k in out:
            if isinstance(out[k], dict) and isinstance(d2[k], dict):
                _merge_dicts(out[k], d2[k])
            elif (isinstance(out[k], dict) and not isinstance(d2[k], dict)) or (not isinstance(out[k], dict) and isinstance(d2[k], dict)):
                raise TypeError
            else:
                out[k] = d2[k]
        else:
            out[k] = d2[k]
    return True



