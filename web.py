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

@app.route("/")
def main():
    return "I'm online"

@app.route("/todoist", methods=['POST'])
def parse_request():
    if request.json['event_name'] == 'item:completed':
        data = request.json['event_data']
        priority = data['priority']
        project_id = data['project_id']
        project_data = json.loads(r.get('https://todoist.com/API/v7/projects/get?token=' + TODOIST_USER_TOKEN + '&project_id=' + project_id).text)
        project = project_data['project']['name']
        url = nomie_api_head + 'push/' + NOMIE_API_KEY + '/action=track/label=' + project + '/value=' + priority
        print url
        r.get(url)
    return '{"status": "success"}'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 1492))
    app.run(host='0.0.0.0', port=port, debug=True)
