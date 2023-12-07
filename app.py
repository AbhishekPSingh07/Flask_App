from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Gather

app = Flask(__name__)


@app.route("/voice", methods=['GET', 'POST'])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Hello!")
    gather = Gather(input = "speech")
    
    

    return str(gather)

# if __name__ == "__main__":
#     app.run(debug=True)