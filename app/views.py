from app import create_app
from flask import request

app = create_app()

@app.route("/")
def index():
    data = request.get_json()
    return {"Info":data}
