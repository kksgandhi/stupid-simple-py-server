from flask import Flask, request, jsonify
app = Flask(__name__)
import importlib

@app.route("/")
def gateway():
    arguments = request.args
    output    = {"information": [],
                 "return":      {}}
    if 'file' not in arguments:
        output["information"].append("No file passed")
        return jsonify(output)
    if 'function' not in arguments:
        output["information"].append("No function passed")
        return jsonify(output)

    module = importlib.import_module(arguments["file"])

    modified_arguments = {k: v for (k, v) in arguments.items() if k not in ["file", "function"]}
    return jsonify(getattr(module, arguments["function"])(**modified_arguments))

if __name__ == "__main__":
    app.run(debug=True)
