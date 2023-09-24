import datetime
from .serializer import serialize_object
from .events import _trigger_event, EVENT_TYPES

class Logger:

    

    def __init__(self, function_manager_instance = None):
        # the function the is being executed
        self.function_manager_instance = function_manager_instance
        self.logs = []


    def create_object(self, object = None, message = None):
        self.__log__(
            message=message,
            log_type=EVENT_TYPES.CREATE_OBJECT,
            object= object
        )
    
    def delete_object(self, object = None, message = None):
        self.__log__(
            message=message,
            log_type=EVENT_TYPES.DELETE_OBJECT,
            object =  object
        )
    
    def update_object(self, object = None, message = None):
        self.__log__(
            message=message,
            log_type=EVENT_TYPES.UPDATE_OBJECT,
            object =  object
        )
    
    def error(self, message = None, object = None):
        self.__log__(
            message=message,
            log_type=EVENT_TYPES.ERROR,
            object= object
        )
    
    def warn(self, message = None, object = None):
        self.__log__(
            message=message, 
            log_type=EVENT_TYPES.WARNING,
            object= object
        )
    
    def info(self, message = None, object = None):
        self.__log__(
            message=message,
            log_type=EVENT_TYPES.INFO,
            object= object
        )
    
    def log_function_execution_start(self):
        self.__log__(
            message='Starting Function Execution - {}'.format(self.function_manager_instance.name),
            log_type=EVENT_TYPES.FUNCTION_EXECUTION_START,
            object= dict(
                function = self.function_manager_instance
            )
        )
    
    def log_function_execution_end(self):
        self.__log__(
            message='Function Execution Ended - {}'.format(self.function_manager_instance.name),
            log_type=EVENT_TYPES.FUNCTION_EXECUTION_END,
            object= dict(
                function = self.function_manager_instance,
                logs = self.function_manager_instance.logger.logs
            )
        )

    def log_function_execution_failure(self, message = None, traceback = None):
        self.__log__(
            message='ERROR {}: Execution Failed. {}'.format(self.function_manager_instance.name, message),
            log_type=EVENT_TYPES.FUNCTION_EXECUTION_FAILURE,
            object=dict(
                traceback = traceback
            )
        )
    

    def __log__(self, message= None, object = None, log_type = None, **kwargs):

        event_data = dict(
            message = message,
            log_type = log_type,
            object = serialize_object(object) if object else None,
            logged_at = datetime.datetime.now()
        )
        ## make it configurable ?
        self.logs.append(
            event_data
        )

        _trigger_event(log_type, event_data)

