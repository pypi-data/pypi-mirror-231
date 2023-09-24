

__function_registry__ = dict()
__serializer_registry__ = dict()

def register_function(function_execution_manager):
    
    __function_registry__[function_execution_manager.name] = function_execution_manager

def get_function(name):
    return __function_registry__.get(name, None)


def register_serializer(type, serializer_function):
    __serializer_registry__[type.__name__] = serializer_function

def get_serializer(type):
    return __serializer_registry__.get(type.__name__, None)