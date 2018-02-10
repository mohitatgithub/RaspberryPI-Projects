#Verbal Calculator

import speech_recognition as sr
from sense_emu import SenseHat
from gtts import gTTS
import os

r = sr.Recognizer()

with sr.Microphone() as source:
    print ('Speak Binary Operation like "2 plus 2"')
    audio = r.listen(source)
    print ('Done')

text = r.recognize_google(audio)
l = text.split(' ')
if(l[1]=='+' or l[1]=='plus'):
    expr = int(l[0])+int(l[2])
elif(l[1]=='/' or l[1]=='divide' or l[1]=='by'):
    expr = int(l[0])/int(l[2])
elif(l[1]=='x' or l[1]=='X' or l[1]=='into' or l[1]=='times'):
    expr = int(l[0])*int(l[2])
elif(l[1]=='-' or l[1]=='minus'):
    expr = int(l[0])-int(l[2])
else: expr = "Not Found"

print(text)
print(expr)

sense = SenseHat()
sense.show_message(str(round(expr,2)))
tts = gTTS(text=str(round(expr,2)), lang='en')
tts.save("output.mp3")
os.system("mpg321 output.mp3")
