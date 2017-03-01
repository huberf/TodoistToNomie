import os
from flask import Flask
from flask import request
import requests as r
app = Flask(__name__)

@app.route("/")
def main():
    return "I'm online"

@app.route("/todoist", methods=['POST'])
def parse_request():
    content = request.form['content']
    priority = request.form['priority']
    return '{"status": "success"}'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 4000))
    app.run(host='0.0.0.0', port=port, debug=True)
