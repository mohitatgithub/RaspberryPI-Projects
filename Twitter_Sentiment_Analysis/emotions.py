#Emotions

#from sense_hat import SenseHat
from sense_emu import SenseHat
import sentiment_analysis

if __name__ == "__main__":
    sense = SenseHat()

    w = [255, 255, 255]
    g = [0, 255, 0]
    r = [255, 0, 0]
    e = [0, 0, 0]

    smile = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,g,e,e,g,e,e,
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
    e,e,r,r,r,r,e,e,
    e,r,e,e,e,e,r,e,
    e,e,e,e,e,e,e,e
    ]

    neutral = [
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,w,e,e,w,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e,
    e,e,w,w,w,w,e,e,
    e,e,e,e,e,e,e,e,
    e,e,e,e,e,e,e,e
    ]

    sentiment = sentiment_analysis.collectSentiment()
    if(sentiment > 0.1):
      sense.set_pixels(smile)
    if(sentiment < -0.1):
      sense.set_pixels(sad)
    else:
      sense.set_pixels(neutral)
