from app import app
from flask import request


@app.route("/", methods=["POST"])
def index():
    data = request.get_json()
    return {"Info":data}
