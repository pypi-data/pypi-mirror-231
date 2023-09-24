import traceback
import uuid

import datetime
import traceback

from .registry import register_function, get_function
from .execution_environment import get_execution_environment


class FunctionManager:

    def __init__(self):
        self.name = None
        self.description = None
        self.target_function = None
    
    def create_new_runner(self):
        function_runner_instance = FunctionRunner()
        function_runner_instance.name = self.name
        function_runner_instance.description = self.description
        function_runner_instance.target_function = self.target_function
        return function_runner_instance


class FunctionRunner:


    def __init__(self) -> None:
        
        from .logger import Logger
        self.id = str(uuid.uuid4())
        self.name = None
        self.description = None


        self.logger = Logger(function_manager_instance=self)


        # self.input_schema = None
        # self.output_schema = None


        # This is the target function that was decorated
        self.target_function = None
        
        
        self.execution_start_time = None
        self.execution_end_time = None
        
        self.executed_successfully = False

        self.execution_ended = False
        self.execution_initiated = False

        self.exception = None
        self.input_data = None
        self.output_data = None
        
        self.execution_id = None
        self.parent_id = None
        


    def execute (self, *args, **kwargs):

        self.input_data = []
        for a in args:
            self.input_data.append(a)
        self.input_data.append(dict(**kwargs))


        try:
            self.logger.log_function_execution_start()
            self.execution_start_time = datetime.datetime.now()
            kwargs['logger'] = self.logger
            self.execution_initiated = True
            self.output_data = self.target_function(*args, **kwargs)
            self.execution_end_time = datetime.datetime.now()
            self.executed_successfully = True
            self.execution_ended = True
            self.logger.log_function_execution_end()
            
        except Exception as e:
            
            self.execution_ended = True
            self.execution_end_time = datetime.datetime.now()
            self.exception = e
            self.output_data = None
            self.executed_successfully = False
            self.logger.log_function_execution_failure(message=str(e), traceback=traceback.format_exc())
            self.logger.log_function_execution_end()
            return
        
        return self.output_data
    
    def run(self, *args, parent_id = None, **kwargs):

        get_execution_environment().on_function_execution_start(self, parent_id)

        output = self.execute(*args, **kwargs)

        get_execution_environment().on_function_execution_end(self)
        
        if self.executed_successfully:
            return output

        
        if self.exception:
            raise self.exception
        
    
    def serialize(self):
        return dict(
            name = self.name,
            description = self.description
        )


def identify(name = None, description = None):


    def inner(function):

        manager = FunctionManager()
        manager.name = name
        manager.description = description

        manager.target_function = function

        if not manager.name:
            manager.name = function.__name__
        
        register_function(manager)

        def execution_function(logger = None, *args, **kwargs):
            
            parent_id = None
            function_manager_instance = getattr(logger, 'function_manager_instance', None)
            if function_manager_instance and isinstance(function_manager_instance, FunctionRunner):
                parent_id = function_manager_instance.id

            function_runner_instance = manager.create_new_runner()
            function_runner_instance.run(parent_id=parent_id, *args, **kwargs)
            
        
        return execution_function
        

    return inner


def invoke_function(name = None, args = [], kwargs = dict()):

    function_manager_instance: FunctionManager = get_function(name)
    if not function_manager_instance:
        raise Exception(f'{name} is not registered as a function.')

    runner = function_manager_instance.create_new_runner()
    return runner.run(*args, **kwargs)
