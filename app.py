from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)


app = Flask(__name__)

@app.route("/answer", methods=["POST"])
def answer():
    response = """
<Response>
    <Say voice="female">Hello. Your call has been answered.</Say>
</Response>
"""
    return Response(response, mimetype="text/xml")

if __name__ == "__main__":
    app.run(port=5000)

@app.route("/call", methods=["GET", "POST"])
def call():
    res = VoiceResponse()
    gather = Gather(input="speech", timeout=300)
    gather.say("Hello, this is a test")
    res.append(gather)
    return str(res)

@app.route("/hello")
def hello():
    return "Helllo po"
