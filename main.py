import speech_recognition as sr
import datetime
import webbrowser
import playsound
import os
import random
from gtts import gTTS
# create a variable and initialize it with a recognizer
r = sr.Recognizer()


def record_audio(ask=False):
    # to use the microphone as our source
    with sr.Microphone() as source:
        if ask:
            doBot_speak(ask)
        # use the recogniser object with the listen() to say something said to the bot
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            doBot_speak('Please say that again, I did not get that')
        except sr.RequestError:
            doBot_speak('OPPS!! MY SPEECH SERVICE IS DOWN')

        return voice_data


def doBot_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    rn = random.randint(1, 10000)
    audio_file = 'audio-' + str(rn) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def response(voice_command):
    if 'what is your name' in voice_command:
        doBot_speak('My name is THE DO BOT')
    if 'what time is it' in voice_command:
        doBot_speak(datetime.datetime.now())

    if 'search Google' in voice_command:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        doBot_speak('I hope these are the results expected for ' + search)

    if 'find location' in voice_command:
        location = record_audio('What Place do you want to find?')
        doBot_speak('Finding location . . . ')
        url = 'https://google.nl/maps/place/' + location
        webbrowser.get().open(url)
        doBot_speak('I hope I did a good job finding ' + location + '/&amp;')


doBot_speak('Tell me how I can help you')
voice_data = record_audio()
print(voice_data)

response(voice_data)
