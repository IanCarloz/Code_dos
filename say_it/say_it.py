# -*- coding: utf8 -*-
from flask import Flask
import voicerss_tts

app = Flask(__name__)

@app.route("/home")
def index():
    voice = voicerss_tts.speech({
        'key': '2003546d991645efae035c4a0aad883a',
        'hl': 'en-us',
        'src': 'Hello, world!',
        'r': '0',
        'c': 'mp3',
        'f': '44khz_16bit_stereo',
        'ssml': 'false',
        'b64': 'true'
    })

    print('<audio src="' + voice['response'] + '" autoplay="autoplay"></audio>')
    # return render_template("home.html")

# @app.route("/es/")
# def index():
#     return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)
