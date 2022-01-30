import speech_recognition as sr
import datetime
import webbrowser
import playsound
import os
import random
from gtts import gTTS
import tkinter as tk
from PIL import Image, ImageTk

# Beginning of Interface
root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=300)

canvas.grid(columnspan=6, rowspan=3)

def sayWhat():

    print('yes')

def runBot():
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
                runBot()
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
        # instructions = tk.Label(root, text=audio_string)
        # instructions.grid( column=0, row=1)
        os.remove(audio_file)

    def response(voice_command):
        if 'what is your name' in voice_command:
            doBot_speak('My name is THE DO BOT')
            instructions = tk.Label(root, text='My name is the DO BOT')
            instructions.grid(column=0, row=1)


        if 'what time is it' in voice_command:
            doBot_speak(datetime.datetime.now())

        if 'Google' in voice_command:
            search = record_audio('What do you want to search for?')
            url = 'https://google.com/search?q=' + search
            webbrowser.get().open(url)
            instructions = tk.Label(root, text='Results for '+search)
            instructions.grid(column=0, row=1)

            doBot_speak('I hope these are the results expected for ' + search)

        if 'place' in voice_command:
            location = record_audio('What Place do you want to find?')
            doBot_speak(f'Finding {location} . . . ')
            url = 'https://google.com/maps/place/' + location
            webbrowser.get().open(url)
            doBot_speak('I hope I did a good job finding ' + location)

        if 'YouTube' in voice_command:
            videoWanted = record_audio('What Video do you want to find on YouTube')
            url = 'https://www.youtube.com/results?search_query=' + videoWanted
            webbrowser.get().open(url)
            videodata = tk.Label(root, text='YouTube results for '+videoWanted)
            videodata.grid(column=0, row=2)

    doBot_speak('Tell me how I can help you')

    voice_data = record_audio()
    print(voice_data)
    saidWords = tk.Label(root, text=f'User\'s words: {voice_data}')
    saidWords.grid(column=0, row=0)

    response(voice_data)


# Button to run chatBot
text = tk.StringVar()
runButton = tk.Button(root, textvariable=text, command=lambda: runBot(), )
text.set("RUN BOT")
runButton.grid(column=2, row=2)

# the end of the window object
root.mainloop()



