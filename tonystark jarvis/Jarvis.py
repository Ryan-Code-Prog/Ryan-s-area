import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import pyautogui
import sys
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Set the first voice (can change as needed)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception as e:
        speak("Could you please say that again?")
        return "none"
    return query.lower()

def wish():
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)

    if hour < 12:
        time_of_day = "morning"
    elif hour < 18:
        time_of_day = "afternoon"
    else:
        time_of_day = "evening"

    current_time = f"{hour}:{minute:02d}"  # Format minutes to always show two digits
    speak(f"Good {time_of_day}, it's {current_time}. I am online and ready, sir.")

if __name__ == "__main__":
    wish()  # Call wish to greet the user
    while True:
        query = take_command()  # Call take_command to listen for user input

        if "open notepad" in query:
            os.startfile("C:\\Windows\\system32\\notepad.exe")
        elif "open vscode" in query:
            os.startfile("C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif "open command prompt" in query:
            os.system("start cmd")
        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('Webcam', img)
                if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif "play music" in query:
            music_dir = "C:\\Users\\Admin\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        elif "what is my ip address" in query:
            ip = get("https://api.ipify.org").text
            speak(f"Your IP address is {ip}.")
        elif "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
            print(results)
        elif "open youtube" in query:
            webbrowser.open("https://www.youtube.com")
        elif "open google" in query:
            speak("What should I search on Google?")
            search_query = take_command()
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
        elif "play song on youtube" in query:
            kit.playonyt("Travis Scott, Playboi Carti - Telescope")
        elif "sleep jarvis" in query:
            speak("Goodbye sir.")
            sys.exit()
        elif "take screenshot" in query:
            speak("Please tell me the name of this screenshot file.")
            name = take_command().lower()
            speak("Please hold the screen for a few seconds; I am taking a screenshot.")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot taken.")
