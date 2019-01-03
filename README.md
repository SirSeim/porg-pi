# Porg Pi
Trigger a Porg from Slack using a Raspberry Pi.

## Prerequisites
* pipenv

## Setup
1. `pipenv install`
1. Set Slack keys inside `pipenv shell`
   ```bash
   export SLACK_SIGNING_SECRET='*secret_key*'
   ```
1. Inside Slack App, setup slash command eg. `/porg` with request url: `https://[ngrok address]/slack`
1. Run Flask app
   ```bash
   pipenv run flask run
   ```

## Usage
In Slack channel, use slash command to activate porg.
