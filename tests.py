import requests
url = 'http://127.0.0.1:5000/'

assert (requests.get(url, params={'file': 'test_functions',
                                 'function': 'add',
                                 'a': 5,
                                 'b': 15}).json()["return"] 

                                 == 20)

assert (requests.get(url, params={'file': 'test_functions',
                                 'function': 'add',
                                 'a': '\"5\"',
                                 'b': '\"15\"'}).json()["return"] 

                                 == "515")

assert (requests.get(url, params={'file': 'test_functions',
                                 'function': 'type_of',
                                 'arg': '\"ababa\"'}).json()["return"]
                                 
                                 == "<class \'str\'>")

