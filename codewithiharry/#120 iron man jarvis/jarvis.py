import os
from time import *
import webbrowser
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import re
from random import randint
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = datetime.datetime.now().hour
    if 0 >= hour < 12:
        speak("Good Morning! Sir")
    elif 12 <= hour > 18:
        speak("Good AfterNoon! Sir")
    else:
        speak("Good Evening Sir")


def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source_of_listening:
        print("Listening Your Voice........")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source_of_listening)

    try:

        print("Recognizing....")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You Said --> {query}\n")

    except Exception as error:
        print("I Can't Understand, Say That Again Please!\n")
        return "none"

    except ConnectionError as connection_error:
        print("Please Connect To Internet!")
        speak("Please Connect To Internet!")
        return "none"

    return query


def youtube_player():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source_of_listening:
        speak("Which Song Do You Want To Hear?")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source_of_listening)
    user_want = recognizer.recognize_google(audio, language='eng-in')
    speak(f"Done! Playing {user_want}")
    kit.playonyt(user_want)


def number_finder_from_string():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source_of_listening:
        speak("How Much Minutes Can i Take a Break?")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source_of_listening)
    user_speaked = recognizer.recognize_google(audio, language='en-in')
    finder = re.findall('[0-9]+', user_speaked)

    return int(finder[0])


def conform_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source_of_listening:
        speak("Are You Sure Boss?")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source_of_listening)
    user_command = recognizer.recognize_google(audio, language='en-in')
    return user_command


if __name__ == '__main__':
    contact = {'chanchal': +917665836763}
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            try:
                speak("Searching WikiPedia....")
                query = query.replace("wikipedia", " ")
                results = wikipedia.summary(query, sentences=2)
                speak("According To WikiPedia..")
                print(results)
                speak(results)

            except wikipedia.exceptions.PageError as page_not_found:
                print(f"Cannot Find About ---> {query}")
                speak(f"Cannot Find About {query}")

        elif 'open facebook ' in query:
            speak("Ok! Copied That")
            webbrowser.open('facebook.com')

        elif 'open spotify' in query:
            speak("Done!")
            webbrowser.open("spotify.com")

        elif 'open github' in query:
            speak("Opening Your Git Account Boss!")
            webbrowser.open('github.com')

        elif 'play song' in query:
            youtube_player()
            continue

        elif 'play a song on youtube' in query:
            youtube_player()
            continue

        elif 'take a break' in query:
            time_in_minutes = number_finder_from_string() * 60
            print(f"Ok Sir! I Am Going To Sleep For {time_in_minutes} Seconds")
            speak(f"Ok Sir! I am Going To Sleep For {time_in_minutes} Seconds")
            sleep(time_in_minutes)
            speak("Hello Boss! I Am Back Again")

        elif 'the time' in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir The Time Is {time}]")

        elif 'play music' in query:
            folder = "E:/NEW SONGS/song/mp3"
            music = os.listdir(folder)
            first_random = randint(0, len(music))
            random_number = randint(0, first_random)
            os.startfile(os.path.join(folder, music[random_number]))

        elif 'play video song' in query:
            folder = "E:/NEW SONGS/song"
            list_of_files = os.listdir(folder)
            number_of_files = len(list_of_files)
            random = randint(0, number_of_files)
            os.startfile(os.path.join(folder, list_of_files[random]))

        elif 'my name' in query:
            speak("Boss! Your Name Is Kuldeep Saini")

        elif 'you are smart' in query:
            speak("ohhh Sir Thank You! i am shey")

        elif 'send whatsapp message' in query:
            kit.sendwhatmsg("+917665836763", 'This is the message', 22 , 28)

        elif 'send a whatsapp message' in query:
            kit.sendwhatmsg("+917665836763", 'This is the message', 22, 00)