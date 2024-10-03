from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from info import details

class Base(DeclarativeBase):
    pass 

db = SQLAlchemy(model_class=Base)

app = Flask(__name__)

@app.route("/flask/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/flask/project")
def get_data():
    return jsonify(details.set_developer())

@app.route("/flask/dev")
def get_developer():
    return jsonify(details.set_project())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)