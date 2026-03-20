from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather
import os
app = Flask(__name__)

@app.route("/call", methods=["GET", "POST"])
def call():
    res = VoiceResponse()
    gather = Gather(input="speech")
    gather.say("Hello, this is a test")
    res.append(gather)
    return str(res)

@app.route("/hello")
def hello():
    return "Helllo po"


if __name__ == "__main__":
    # Railway provides the PORT in an environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)