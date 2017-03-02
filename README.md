# Todoist to Nomie
*This is a work in progress but is functional*

This Python service couples with the [Todoist API](https://developer.todoist.com/?shell#api-overview) and the [Nomie Pro API](https://connect.nomie.io/) to sync over your completed task history.

## Setup
* This service needs two things: a Todoist developer app key with your user
  token and a Nomie Pro API key
* First, you will need to follow the "Todoist Oath" instructions to get an
  `access_token`. Once completed put this value in an environent variable called
  `TODOIST_USER_TOKEN`.
* Now, put your Nomie Pro API key in an environment variable called
  `NOMIE_API_KEY`
* Run the web.py script with Python 2.7 by executing `python web.py` in the
  project directory.
* Now configure your Todoist API app to accept webhooks at
  `http://[YOUR_HOST_NAME].com/todoist` for the hook `item:added`
* Live long and prosper.

## Todoist OAuth
* First create a Todoist application in the dasbhoard at the [app console](https://developer.todoist.com/appconsole.html).
* Now insert your client_id and client_secret into the `todoist_auth.py` file.
* Then, run `python todoist_auth.py` and follow the instructions.
* Now pluck the "access_token" from the response and jump back to the setup
  steps.

## Contributing and Bugs
If you spot a bug or have a feature request, feel free to open an issue, or if
you are feeling particularly adventerous, open a PR and I'll add it in shortly.
