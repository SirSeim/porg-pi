import hashlib
import hmac
import os
import time

from flask import Flask, request
from gpiozero import LED

SLACK_SIGNING_SECRET = os.environ['SLACK_SIGNING_SECRET']
PI_PIN = 4

app = Flask(__name__)
porg = LED(PI_PIN)


@app.route('/slack', methods=['POST'])
def verify_slack_signing():
    request_body = request.get_data()
    slack_timestamp = request.headers.get('X-Slack-Request-Timestamp')
    slack_signature = request.headers.get('X-Slack-Signature')

    if abs(time.time() - int(slack_timestamp)) > 60 * 5:
        # if request timestamp is more than 5 minutes from local time, could be an attack
        return

    sig_basestring = ('v0:' + str(slack_timestamp) + ':').encode('utf-8') + request_body
    my_signature = 'v0=' + hmac.new(SLACK_SIGNING_SECRET.encode('utf-8'), sig_basestring, hashlib.sha256).hexdigest()

    if hmac.compare_digest(my_signature, slack_signature):
        # Request is now fully authenticated
        # command = request.form.get('text', None)
        porg.on()
        time.sleep(1)
        porg.off()
        return 'Working!!'


if __name__ == "__main__":
    app.run(debug=True)
