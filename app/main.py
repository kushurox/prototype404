from flask import Flask, render_template, request, make_response
import json
import uuid

app = Flask(__name__)

cURL = ""

@app.route("/")
def index():
    rich = request.cookies.get('rich')
    print(rich)
    if not rich:
        print("Cookies Set")
        rich = 499
        resp = make_response(render_template("index.html", rich=int(rich), error=None))
        resp.set_cookie("rich", str(rich))
        return resp

    return render_template("index.html", rich=rich)

@app.route("/yuufoundyitwaw", methods=["POST"])
def nice():
    global cURL
    if request.json.get('code') == "flag{Kushurox_is_a_nice_guy}":
        cURL = uuid.uuid4().hex
        print("cURL set to", cURL)
        return json.dumps({"url": cURL, "success": True})
    else:
        return json.dumps({"url": None, "success": False})

@app.route("/<variable>")
def nextChallenge(variable):
    global cURL
    print(f"CURL = {cURL}, Variable = {variable}")
    if variable == cURL:
        return "You Win Now leave me Alone"
    else:
        return "400 Page Not found"

if __name__ == "__main__":
    app.run(debug=True)