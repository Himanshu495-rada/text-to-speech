from gtts import gTTS
file = open("mySpeech.txt","r")
text = file.read()
tts = gTTS(text)
tts.save('test.mp3')
