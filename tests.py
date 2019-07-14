import requests
from pprint import pprint as print

url = 'http://127.0.0.1:5000/'
output = {}

try:
    output = (requests.get(url, params={'file': 'test_functions',
                                     'function': 'add',
                                     'a': 5,
                                     'b': 15}).json())
    assert output["return"] == 20

    output = (requests.get(url, params={'file': 'test_functions',
                                     'function': 'add',
                                     'a': '\"5\"',
                                     'b': '\"15\"'}).json())
    assert output["return"] == "515"

    output = (requests.get(url, params={'file': 'test_functions',
                                     'function': 'type_of',
                                     'arg': '\"ababa\"'}).json())
    assert output["return"] == "<class \'str\'>"
except AssertionError:
    print(output)
