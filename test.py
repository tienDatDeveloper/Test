from flask import Flask, redirect, url_for, render_template, controller
import speech_recognition
 
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)






































#-------------------------------------------
# from re import M
# import speech_recognition as sr
# r= sr.Recognizer()
# with sr.Microphone() as source2:
#     r.adjust_for_ambient_noise(source2)

#     audio = r.listen(source2)
#     MyText = r.recognize_google(audio)
#      # MyText = MyText.lower()
#     print(MyText)