from flask import Flask
from twilio.twiml.voice_response import Gather, VoiceResponse

app = Flask(__name__)

@app.route("/call", methods=["GET", "POST"])
def call():
    response = VoiceResponse()

    gather = Gather(input="speech")
    gather.say("Hello, this is a test")

    response.append(gather)

    return str(response)