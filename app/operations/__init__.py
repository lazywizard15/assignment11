# app/operations/__init__.py 

# Expose the functions so they can be imported as:
# from app.operations import add

from .core_logic import add, subtract, multiply, divide 
# If the functions were already defined here, you need to use an explicit export list:
# __all__ = ['add', 'subtract', 'multiply', 'divide']