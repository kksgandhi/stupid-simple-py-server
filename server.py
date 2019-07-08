from flask import Flask, request, jsonify
app = Flask(__name__)
import importlib

@app.route("/")
def gateway():
    arguments = request.args
    output    = {"information": [],
                 "return":      {}}

    def information(error):
        output["information"].append(error)
        return jsonify(output)

    if 'file' not in arguments:
        return information("No file passed")
    if 'function' not in arguments:
        return information("No function passed")

    try:
        module = importlib.import_module(arguments["file"])
    except ModuleNotFoundError:
        return jsonify("ModuleNotFoundError")

    modified_arguments = {k: v for (k, v) in arguments.items() if k not in ["file", "function"]}
    requested_function = getattr(module, arguments["function"])
    output["return"]   = requested_function(**modified_arguments)
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
