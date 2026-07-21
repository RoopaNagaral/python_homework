import logging
from functools import wraps

#Task 1
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
...

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"function: {func.__name__}")
        
        if args:
            logger.info(f"positional parameters: {list(args)}")
        else:
            logger.info(f"positional parameters: none")
            
        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info(f"keyword parameters: none")
        
        result = func(*args, **kwargs)
        logger.info(f"return: {result}")
        
        return result
    return wrapper

print("Output of Task 1:")
@logger_decorator
def greet():
    print("Hello! World")

@logger_decorator
def chek_args(*args):
    return True

@logger_decorator
def kw_retuen(**kwargs):
    return logger_decorator
 
greet()
chek_args(10,15,20,"orange")
kw_retuen(a=25, b="Hello", c=True)
    
# Task 2