from flask import Flask, render_template, request, redirect
import speech_recognition as sr
from scipy.io import wavfile

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ""
    if request.method == "POST": 
        print("FORM DATA RECEIVED")
        if "file" not in request.files:  # no file uploaded
            print(" Cannot find file")
            return redirect(request.url)  # redirect the user to the home page

        file = request.files['file']  # if file exist, give that file
        if file.filename == "":  # if file is empty, return to the main page
            print(" Uploaded file is empty")
            return redirect(request.url)

        if file:
            print(" Your file successfully uploaded")
            recognizer = sr.Recognizer()  # initilaize instance of the speech recognition class
            audioFile = sr.AudioFile(file)  # pass in the file
            with audioFile as source:  # read the file
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)  # using Google API

    return render_template('index.html', transcript=transcript)

if __name__ == '__main__':
    app.run(port='2207', debug=True, threaded=True)  # multiple requests at the same time for the file
