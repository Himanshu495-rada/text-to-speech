import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

file = open("MySpeech.txt","r")
text = file.read()

engine.save_to_file(text, "MySpeech.mp3")
engine.runAndWait()
