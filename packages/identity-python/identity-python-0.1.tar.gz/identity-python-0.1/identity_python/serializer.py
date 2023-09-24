import inspect
from .registry import register_serializer, get_serializer

def serialize(types = []):
    if not types or len(types) <= 0:
        raise Exception('serialize decorator should be called with types argument.')
    
    for t in types:
        if not inspect.isclass(t) and not isinstance(t, str):
            raise Exception('serialize decorator should be called with class types or string names.')

    def inner(function):

        for t in types:
            register_serializer(t, function)
        
        return function

    return inner


def serialize_object(obj):

    serializer =  get_serializer(obj.__class__)

    ## Call default serializer
    if not serializer:
        return obj
    
    return serializer(obj)

