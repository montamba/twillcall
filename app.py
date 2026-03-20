from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather

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
