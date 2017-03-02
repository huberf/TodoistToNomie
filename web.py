import os
from flask import Flask
from flask import request
import requests as r
app = Flask(__name__)

NOMIE_API_KEY = os.environ.get("NOMIE_API_KEY")
print NOMIE_API_KEY
nomie_api_head = "https://api.nomie.io/v2/"

@app.route("/")
def main():
    return "I'm online"

@app.route("/todoist", methods=['POST'])
def parse_request():
    content = request.form['content']
    rawPriority = request.form['priority']
    priority = rawPriority[9:]
    project = request.form['project']
    url = nomie_api_head + 'push/' + NOMIE_API_KEY + '/action=track/label=' + project + '/value=' + priority
    print url
    r.get(url)
    return '{"status": "success"}'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1492))
    app.run(host='0.0.0.0', port=port, debug=True)
