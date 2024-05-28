import pyjokes
from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

app.json.sort_keys = False
app.json.ensure_ascii = False

@app.route("/")
def index():
    return redirect("/docs/")

@app.route("/docs")
@app.route("/docs/")
def docs():
    api_routes = {
        "routes": {
            "/": {
                "description": "Redirects to the docs page."
            },
            "/docs": {
                "description": "Shows the routes for this api."
            },
            "/joke": {
                "description": "Tells a random joke.",
                "parameters": {
                    "lang": {
                        "description": "Specifies the language of the joke.",
                        "valid_options": "'en', 'de', 'es', 'gl', 'eu'', 'it'"
                    }
                }
            }
        }
    }

    return jsonify(api_routes), 200

@app.route("/joke/")
def jokeredirect():
    return redirect("/joke")

@app.route("/joke", methods=["GET"])
def joke():
    lang = "en" if request.args.get("lang") is None else request.args.get("lang")
    if lang.lower() not in ["en", "de", "es", "gl", "eu", "it"]:
        return jsonify({"error": "Invalid lang value. Valid options are 'en', 'de', 'es', 'gl', 'eu', or 'it'"}), 400
    try:
        joke = pyjokes.get_joke(language=lang)
        return jsonify({"joke": joke}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)