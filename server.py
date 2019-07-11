from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import importlib

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

    modified_arguments = _modify_arguments(arguments)
    try:
        output["return"]   = requested_function(**modified_arguments)
    except:
        import traceback
        return information(traceback.format_exc().split('\n'))
    return jsonify(output)

def _modify_arguments(arguments):
    def parse_argument(kv):
        key, value = kv
        try:
            return key, int(value)
        except ValueError:
            pass
        try:
            return key, float(value)
        except ValueError:
            pass
        if key in ["file", "function"]:
            return None
        return kv

    return dict(
           filter(lambda x: x is not None,
           map(parse_argument,
           arguments.items())))

if __name__ == "__main__":
    app.run(debug=False)
