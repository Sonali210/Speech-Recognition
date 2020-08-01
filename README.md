# Speech-Recognition
This is a flask framework based web appllication that allows users to transcribe speech by uploading a wav file.

# How speech-recognition really works?
In order to decode the speech into text, groups of vectors are matched to one or more phonemes—a fundamental unit of speech. This calculation requires training, since the sound of a phoneme varies from speaker to speaker, and even varies from one utterance to another by the same speaker. A special algorithm is then applied to determine the most likely word (or words) that produce the given sequence of phonemes.

But hey! since you are a Python programmer, you don’t have to worry about any of this. A number of speech recognition services are available for use online through readily available API.

# How to design the program for recognition
1. Create an audio file from the file initially created
2. Then initialize an instance from the speech recognition class
3. Then pass that audio file into the record function of the recognizer module which will parse the audio file
and convert it to understandable format which allows us to apply our function: recognize

# How to run this repo on your local
1.You need to install dependencies by using pip install-r requirements.txt in your command prompt
2.Run app.py file
3.Copy the URL obtained in your web browser and here you go.
4.Upload your own wav file or choose one from 'Recording' named folder of this repository.(Remember only files with .wav extentions are to be uploaded.)
5.Click on transcribe.

Congratulations! your speech has been converted to text.
Try using different speeches and see the results:)
