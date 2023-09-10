from app import app
from flask import request


@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    print(data)
    return "Successful",200
