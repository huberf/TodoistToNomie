# Todoist to Nomie

This Python service couples with [IFTTT](http://ifttt.com/) to allow one to sync
tasks finished on Todoist with Nomie Pro via its API.

## Setup
* First, login/register with IFTTT and make sure the Todoist channel has been
  linked.
* Now create an Applet for the event "New Completed Task" with it set to fire
  for any project.
* For the "then" config, we will create a placeholder Maker event to accept the
  task data.
* Now to get the Python service running you will have to wait until I further
  embellish the instructions.

## Todoist OAuth
* First create a Todoist application in the dasbhoard (instructions coming soon).
* Now have you user visit https://todoist.com/oauth/authorize?client_id=appId&scope=data:read,data:delete&state=appSecret
* Now take the "code" value of the redirected URL and visit POST https://todoist.com/oauth/access_token?client_id=appId&client_secret=appSecret&code=theCode
* Now pluck the "access_token" from the response and you are ready.
