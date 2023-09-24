import uuid

from .events import _trigger_event, EVENT_TYPES

class SynchronousEnvironment:
    
    def __init__(self) -> None:
        self.executed_functions = []
        self.id = uuid.uuid4()
    
    def on_function_execution_start(self, function_wrapper_instance, parent_id):
        function_wrapper_instance.execution_id = self.id

        if len(self.executed_functions) == 0:
            _trigger_event(EVENT_TYPES.EXECUTION_START, None)
        else:
            if parent_id:
                function_wrapper_instance.parent_id = parent_id
            else:
                last_function_manager_instance = self.executed_functions[-1]
                function_wrapper_instance.parent_id = last_function_manager_instance.id
        
        self.executed_functions.append(function_wrapper_instance)
    
    def on_function_execution_end(self, function_wrapper_instance):
        has_execution_finished = len(
            [a  for a in self.executed_functions if a.execution_ended]
        ) > 0

        if not has_execution_finished:
            return
        
        event_data = dict(
            executed_functions = self.executed_functions
        )
        _trigger_event(EVENT_TYPES.EXECUTION_END, event_data)




    
    


class AsynchronousEnvironment:

    def __init__(self) -> None:
        self.executed_functions = []
    
    def on_function_execution_start(self, function_wrapper_instance, parent_id):
        if len(self.executed_functions) == 0:
            _trigger_event(EVENT_TYPES.EXECUTION_START, None)

        if parent_id:
            function_wrapper_instance.parent_id = parent_id
        
        self.executed_functions.append(function_wrapper_instance)
    
    def on_function_execution_end(self, function_wrapper_instance):
        event_data = dict(
            executed_functions = self.executed_functions
        )
        _trigger_event(EVENT_TYPES.EXECUTION_END, event_data)



class SharedEnvironmentManager:

    def __init__(self) -> None:
        self.environment = None
    
    def update(self, environment):
        self.environment = environment


_manager = SharedEnvironmentManager()
_manager.update(SynchronousEnvironment())

def set_execution_environment(environment):
    _manager.update(environment)

def get_execution_environment():
    return _manager.environment