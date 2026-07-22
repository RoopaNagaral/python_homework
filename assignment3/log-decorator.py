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
        
        pos_params = list(args) if args else "none"
        kw_params = kwargs if kwargs else "none"
        
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {pos_params}")
        logger.log(logging.INFO, f"keyword parameters: {kw_params}")

        result = func(*args, **kwargs)

        # Log the actual return value
        logger.log(logging.INFO, f"return: {result!r}")
        logger.log(logging.INFO, "-" * 40)
        
        return result
    return wrapper

print("Output of Task 1:")
@logger_decorator
def no_param_function():
    print("Hello! World")

@logger_decorator
def positional_only_function(*args):
    return True

@logger_decorator
def keyword_only_function(**kwargs):
    return logger_decorator
 
if __name__ == "__main__":
    no_param_function()
    positional_only_function(10, 20, "apple", 3.14)
    keyword_only_function(a=1, b="two", c=True)

# --- Task Completed ---