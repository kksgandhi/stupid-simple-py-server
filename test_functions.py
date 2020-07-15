"""
Test functions that the server can call upon
"""
def add(a, b):
    """ adds two elements """
    return a + b

def swap_kv(**kwargs):
    """ swaps within a dictionary """
    return {v: k for k, v in kwargs.items()}

def error():
    """ errors """
    return 1/0

def add_to_array(num, array):
    """ adds num to every element in the array """
    return list(map(lambda x: x + num, array))

def type_of(arg):
    """ returns type of argument """
    return str(type(arg))

def un_jsonible(arg):
    """ returns object that cannot be converted to JSON """
    return type(arg)

def identity(**kwargs):
    """ returns arguments with no changes """
    return kwargs
