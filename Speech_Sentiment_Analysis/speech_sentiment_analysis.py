#Speech Sentiment Analysis

import speech_recognition as sr
from sense_emu import SenseHat
import textblob

r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Speak...')
    audio = r.listen(source)
    print ('Done!')

text = r.recognize_google(audio)

analysis = textblob.TextBlob(text)
sentiment = analysis.sentiment.polarity

sense = SenseHat()

w = [255, 255, 255]
g = [0, 255, 0]
r = [255, 0, 0]
e = [0, 0, 0]

smile = [
e,e,e,e,e,e,e,e,
e,e,g,e,e,g,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,g,e,e,e,e,g,e,
e,e,g,g,g,g,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

sad = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,r,e,e,r,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,r,r,e,e,e,
e,e,r,e,e,r,e,e,
e,e,e,e,e,e,e,e
]

neutral = [
e,e,e,e,e,e,e,e,
e,e,w,e,e,w,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,w,w,w,w,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

print(text)
print("polarity: "+str(sentiment))

sense.clear()
if(sentiment > 0.1):
  sense.set_pixels(smile)
elif(sentiment < -0.1):
  sense.set_pixels(sad)
else:
  sense.set_pixels(neutral)
