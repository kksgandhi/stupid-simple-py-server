"""
This is the main server and only required part of the whole project
"""
import importlib
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

modules = {}

@app.route("/", methods=["GET", "POST"])
def gateway():
    """
    This is the function that is run on any request to root
    """
    arguments = request.json
    # set up an output variable that we can later return
    output    = {"information": [],
                 "return":      {}}

    # quickly add information to the output
    def information(*info):
        output["information"] += info
        return jsonify(output)

    if 'file' not in arguments:
        return information("No file passed")
    if 'function' not in arguments:
        return information("No function passed")

    try:
        file_name = arguments["file"]
        # we want to import the file if we don't have it cached
        if file_name not in modules:
            modules[file_name] = importlib.import_module(file_name)
        # get the function from the file
        requested_function = getattr(modules[file_name], arguments["function"])
    except ModuleNotFoundError:
        return information("file not found")
    except AttributeError:
        return information("function not found within file")

    try:
        # we want to remove 'file' and 'function' from the arguments
        modified_arguments = ({key: value
                               for key, value in arguments.items()
                               if key not in ['file', 'function']})
        # actually call the function
        output["return"] = requested_function(**modified_arguments)
    except:
        # if there was any sort of error, return it
        import traceback
        return information(traceback.format_exc().split('\n'))
    try:
        return jsonify(output)
    except TypeError:
        # can't jsonify the return? Say that in the information
        output["return"] = {}
        return information("Your return value was unable to be converted to json")

if __name__ == "__main__":
    app.run(debug=False)
