import os
import json
from flask import Flask
from flask import request
import requests as r
app = Flask(__name__)

NOMIE_API_KEY = os.environ.get("NOMIE_API_KEY")
TODOIST_USER_TOKEN = os.environ.get('TODOIST_USER_TOKEN')
print NOMIE_API_KEY
nomie_api_head = "https://api.nomie.io/v2/"

def load_project(project_id):
    project_data = json.loads(r.get('https://todoist.com/API/v7/projects/get?token=' + TODOIST_USER_TOKEN + '&project_id=' + project_id).text)
    return project_data

def tap_tracker(name, value):
    url = nomie_api_head + 'push/' + NOMIE_API_KEY + '/action=track/label=' + name + '/value=' + value
    print url
    r.get(url)

@app.route("/")
def main():
    return "I'm online"

@app.route("/todoist", methods=['POST'])
def parse_request():
    if request.json['event_name'] == 'item:completed':
        data = request.json['event_data']
        priority = str(data['priority'])
        project_id = str(data['project_id'])
        project_data = load_project(project_id)
        project = project_data['project']['name']
        tap_tracker(project, priority)
    return '{"status": "success"}'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1492))
    app.run(host='0.0.0.0', port=port, debug=True)
