import importlib
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

modules = {}

@app.route("/")
def gateway():
    arguments = request.args
    output    = {"information": [],
                 "return":      {}}

    def information(*info):
        output["information"] += info
        return jsonify(output)

    if 'file' not in arguments:
        return information("No file passed")
    if 'function' not in arguments:
        return information("No function passed")

    try:
        file_name = arguments["file"]
        if file_name not in modules:
            modules[file_name] = importlib.import_module(file_name)
        else:
            importlib.reload(modules[file_name])
        requested_function = getattr(modules[file_name], arguments["function"])
    except ModuleNotFoundError:
        return information("file not found")
    except AttributeError:
        return information("function not found within file")

    try:
        modified_arguments = ({key: json.loads(value) 
                              for key, value in arguments.items()
                              if key not in ['file', 'function']})
    except json.decoder.JSONDecodeError:
        return information("An argument could not be converted to json.")
    try:
        output["return"] = requested_function(**modified_arguments)
    except:
        import traceback
        return information(traceback.format_exc().split('\n'))
    try:
        return jsonify(output)
    except TypeError:
        output["return"] = {}
        return information("Your return value was unable to be converted to json")

if __name__ == "__main__":
    app.run(debug=False)
