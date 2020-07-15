import requests
from pprint import pprint as print

url     = 'http://127.0.0.1:5000/'
output  = {}
verbose = True

try:
    output = (requests.post(url, json={'file': 'test_functions',
                                        'function': 'add',
                                        'a': 5,
                                        'b': 15}).json())
    if verbose:
        print(output)
    assert output["return"] == 20

    output = (requests.post(url, json={'file': 'test_functions',
                                        'function': 'add',
                                        'a': "5",
                                        'b': "15"}).json())
    if verbose:
        print(output)
    assert output["return"] == "515"

    output = (requests.post(url, json={'file': 'test_functions',
                                        'function': 'type_of',
                                        'arg': "ababa"}).json())
    if verbose:
        print(output)
    assert output["return"] == "<class \'str\'>"

    output = (requests.post(url, json={'file': 'test_functions',
                                        'function': 'un_jsonible',
                                        'arg': "ababa"}).json())
    if verbose:
        print(output)
    assert len(output["information"]) > 0 and len(output["return"]) == 0

    output = (requests.post(url, json={'file': 'test_functions',
                                        'function': 'error'}).json())
    if verbose:
        print(output)
    assert len(output["information"]) > 0 and len(output["return"]) == 0

    output = (requests.post(url, json={'file': 'test_functions',
                                      'function': 'add_to_array',
                                      'num': 7,
                                      'array': [-1, 2, 3]}).json())
    if verbose:
        print(output)
    assert output["return"] == [6, 9, 10]

    output = (requests.post(url, json={'file': 'test_functions',
                                      'function': 'swap_kv',
                                      'num': 7,
                                      'array': "not array",
                                      'intel': 'amd'}).json())
    if verbose:
        print(output)


    output = (requests.post(url, json={'file': 'test_functions',
                                      'function': 'identity',
                                      'num': 7,
                                      'array': [-1, 2, 3],
                                      'finfandangle': {'three': 3, 'seven': [7], "doop": {"a": "a"}}}).json())
    if verbose:
        print(output)

    print("=== ALL TESTS PASSED ===")
except AssertionError:
    print(output)
