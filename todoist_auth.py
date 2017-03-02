import webbrowser
import requests as r

scope = "data:read"
client_id = ""
client_secret = ""

webbrowser.open("https://todoist.com/oauth/authorize?client_id=" + client_id + "&scope=" + scope + "&state=" + client_secret)

code = raw_input(":> ")

resp = r.post("https://todoist.com/oauth/access_token",
        {"client_id": client_id,
            "client_secret": client_secret,
            "code": code
            }
        )

print resp.text
