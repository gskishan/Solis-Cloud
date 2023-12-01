# hooks.py

def before_function_execution():
    """
    Hook called before executing a function.
    """
    print("Executing function...")

def after_function_execution(result):
    """
    Hook called after executing a function.
    :param result: The result of the function.
    """
    print(f"Function execution completed. Result: {result}")

def on_error(exception):
    """
    Hook called when an error occurs during function execution.
    :param exception: The exception raised during the error.
    """
    print(f"Error during execution: {exception}")

# Additional hooks can be added as needed
