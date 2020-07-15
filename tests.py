import requests
from pprint import pprint as print

url     = 'http://127.0.0.1:5000/'
output  = {}
verbose = True

try:
    output = (requests.get(url, params={'file': 'test_functions',
                                     'function': 'add',
                                     'a': 5,
                                     'b': 15}).json())
    if verbose:
        print(output)
    assert output["return"] == 20

    output = (requests.get(url, params={'file': 'test_functions',
                                     'function': 'add',
                                     'a': '\"5\"',
                                     'b': '\"15\"'}).json())
    if verbose:
        print(output)
    assert output["return"] == "515"

    output = (requests.get(url, params={'file': 'test_functions',
                                     'function': 'type_of',
                                     'arg': '\"ababa\"'}).json())
    if verbose:
        print(output)
    assert output["return"] == "<class \'str\'>"

    output = (requests.get(url, params={'file': 'test_functions',
                                     'function': 'un_jsonible',
                                     'arg': '\"ababa\"'}).json())
    if verbose:
        print(output)
    assert len(output["information"]) > 0
except AssertionError:
    print(output)
