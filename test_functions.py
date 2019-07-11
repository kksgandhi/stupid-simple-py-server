def add(a, b):
    return a + b

def swap_kv(**kwargs):
    return {v: k for k, v in kwargs.items()}

def error(**kwargs):
    return 1/0
