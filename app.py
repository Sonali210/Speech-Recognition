from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from scipy.io import wavfile

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ""
    if request.method == "POST":  # if we posted the form
        print("FORM DATA RECEIVED")
        # here are 2 forms to make sure this file exist :
        if "file" not in request.files:  # no file exist/ uploaded
            print(" Debug: Line 1")
            return redirect(request.url)  # redirect the user to the home page

        file = request.files['file']  # if file exist it will give me that file
        if file.filename == "":  # if file is blank/empty, return to the main page
            print(" Debug: Line 2")
            return redirect(request.url)

        if file:
            print(" Debug: Line 3")
            recognizer = sr.Recognizer()  # initilaize instance of the speech recognition class
            audioFile = sr.AudioFile(file)  # pass in the file
            with audioFile as source:  # reading the file
                data = recognizer.record(source)  # through the recognizer
            transcript = recognizer.recognize_google(data, key=None)  # using Google API will return the text

    return render_template('index.html', transcript=transcript)

if __name__ == '__main__':
    app.run(port='2207', debug=True, threaded=True)  # multiple requests at the ame time for the file
