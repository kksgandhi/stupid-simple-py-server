# stupid-simple-py-server

This is a simple web server that allows you to prototype running Python code from any other major coding language.

If you have a program in something like C++, you can't just call python functions simply. You need libraries and a ton of specific code. [Here's documentation from the python website](https://docs.python.org/2/extending/embedding.html). While this is the best option in the long term, if you just need something quick and dirty, this is where this webserver comes in.

Simply install the requirements (pip3 -r requirements.txt) and run server.py just like any other python file (python3 server.py).

Look at the url the webserver tells you about, then send a HTTP get / post request to that webserver with json arguments. There are two required arguments: "file" and "function", where "file" is the python file you want run, and "function" is the function within that file. Along with those two required arguments, you can add as many other arguments as you want and they'll be passed directly to the function you want.

Here's an example, let's say we have the following code in a file called "test_functions.py":
```
def add(a, b):
  return a + b
```
We can call that function (once the server is running) from any language by making a POST request with the following JSON data:
```
{'file': 'test_functions',
 'function': 'add',
 'a': 5,
 'b': 15}
```
In python itself, this would look like the following:
```
output = (requests.post(url, json={'file': 'test_functions',
                                       'function': 'add',
                                       'a': 5,
                                       'b': 15}).json())
```

The files test_functions.py and tests.py have a variety more examples.
