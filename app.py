from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

@app.route("/voice", methods=["POST"])
def voice():
    response = VoiceResponse()

    gather = response.gather(
        input="speech",
        action="/process",
        speechTimeout="auto"
    )

    gather.say("Hello, what is your question?")

    return str(response)


@app.route("/process", methods=["POST"])
def process():
    speech = request.form.get("SpeechResult")

    print("Caller said:", speech)

    response = VoiceResponse()
    response.say(f"You said {speech}")

    return str(response)