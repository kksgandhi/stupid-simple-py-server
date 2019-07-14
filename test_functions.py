def add(a, b):
    return a + b

def swap_kv(**kwargs):
    return {v: k for k, v in kwargs.items()}

def error(**kwargs):
    return 1/0

def add_to_array(num, array):
    return list(map(lambda x: x + num, array))

def type_of(arg):
    return str(type(arg))
