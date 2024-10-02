from flask import Flask,jsonify
from datetime import date

app = Flask(__name__)

about_developer = {
    'name': 'peter',
    'role': 'software engineer',
}

about_project = {
    'name': 'eigress',
    'start': date.fromisoformat('2024-09-17')
}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/project")
def get_data():
    return jsonify(about_project)

@app.route("/dev")
def get_developer():
    return jsonify(about_developer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)