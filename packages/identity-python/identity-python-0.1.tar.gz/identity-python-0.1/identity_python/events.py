
class EVENT_TYPES:

    EXECUTION_END = 'EXECUTION_END'
    EXECUTION_START = 'EXECUTION_START'

    ERROR = 'ERROR'
    INFO = 'INFO'
    WARNING = 'WARNING'

    CREATE_OBJECT = 'CREATE_OBJECT'
    UPDATE_OBJECT = 'UPDATE_OBJECT'
    DELETE_OBJECT = 'DELETE_OBJECT'

    FUNCTION_EXECUTION_START = 'FUNCTION_EXECUTION_START'
    FUNCTION_EXECUTION_END = 'FUNCTION_EXECUTION_END'
    FUNCTION_EXECUTION_FAILURE = 'FUNCTION_EXECUTION_FAILURE'





def _on_execution_start(data):
    ...

def _on_execution_end(data):
    ...

_default_callbacks = {
    f'{EVENT_TYPES.EXECUTION_START}': _on_execution_start,
    f'{EVENT_TYPES.EXECUTION_END}': _on_execution_end
}

_callbacks = {
    
}

def _trigger_event(event_type, data):

    if _default_callbacks.get(event_type, None):
        _default_callbacks[event_type](data)
    
    if _callbacks.get(event_type, None):
        _callbacks[event_type](data)
    
    
def add_event_listener(event_type, callback):
    _callbacks[event_type] = callback


def remove_event_listener(event_type):
    del _callbacks[event_type]

