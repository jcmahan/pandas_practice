# def greet() -> None:
#     print('hello')

# greet()

# def greet2(name)-> str:
#     print(f'Hello, {name}')

# greet2('James')

# param vs argument -- param is what we define during writing a function, 
# the argument is the value we provide when calling the function 
# def load_table(table_name)-> str:
#     print('Loading', table_name)

# load_table('retail_sales.csv')
# load_table('customer_df')

# return sends a value back from the function
# def square(number)-> int:
#     return number**2

# print(square(5))

# *args lets a function receive multiple positional arguments
# **kwargs lets a function receive mutliple keyword arguments
# def show_values(*args):
#     print(args)
# show_values('sales', 'dbo', 'mydb')

# def show_values2(**kwargs):
#     print(kwargs)
# show_values2(table = 'sales', schema = 'dbo', database = 'mydb')

# decorator = also a function that takes in another function and adds more functionality
# we don't have to keep changing the original function
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('This is from the wrapper')
#         func(*args, **kwargs)
#         return wrapper

# @my_decorator
# def load_table():
#     print('Loading data')

# # load_table = my_decorator(load_table)
# load_table()

from datetime import datetime
from functools import wraps

def etl_logs(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Load starting')
        print('Start time', datetime.now())
        result = func(*args, **kwargs)
        print('Load Done')
        print('end time', datetime.now())
        return result
    return wrapper

# @etl_logs
# def load_table(tablename, schema, databasename):
#     print(f'Loading data into {databasename}.{schema}.{tablename}')
# load_table('sales', 'dbo', 'mydb')

def handle_failure(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as error:
            print('Job Failed')
            print('error:', error)
            return None
    return wrapper

@handle_failure
@etl_logs
def load_table(tablename, schema, databasename):
    print(f'Loading data into {databasename}.{schema}.{tablename}')
# load_table('sales', 'dbo', 'mydb')
# load_table(1/0)