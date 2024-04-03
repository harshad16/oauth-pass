from flask import Flask, request
import os

app = Flask(__name__)

@app.before_request
def log_request():
    app.logger.debug("Request Headers %s", request.headers)
    return None

@app.route("/")
def hello():
    return "Hello world!!"

@app.route("/hello")
def print_headers():
    print(request.headers)
    return "check print statement in logs"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)