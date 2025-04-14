
import pyttsx3
import speech_recognition as sr
import random 
import webbrowser
import datetime
import pyautogui
import wikipedia
from plyer import notification
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # Getting details of current voice

for voice in voices:
    engine.setProperty('voice', voices[0].id)  # Changing index, changes voices. 0 for male
    engine.setProperty('rate', 120)

def speak(comand):
    engine.say(comand)
    engine.runAndWait()

# Obtain audio from mic
def micaudio():
    query = " "
    while query == " ":
        r = sr.Recognizer()  
        with sr.Microphone() as source:  # Define source
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language='en-in')
            print("Recognizing...")
            print(f"User said: {query}\n")
        except Exception as e:
            print("Say that again, please...")
            return "None"  

        return query  

def main_process():
    while True:
        req = micaudio().lower()
        if "hey windows" in req:
            speak("Welcome, How i can help you.....")
        elif "play music" in req:
            speak("Okay Anshul I'm playing music")
            song = random.randint(1,5)
            if song == 1:
                webbrowser.open("https://music.youtube.com/watch?v=5IdGjLg6m5Q")
            elif song == 2:
                webbrowser.open("https://music.youtube.com/watch?v=opwZ_PJ-F_E")
            elif song == 3:
                webbrowser.open("https://music.youtube.com/watch?v=2FhgKp_lfJQ&list=OLAK5uy_liSXghGab9NDc_RKomomCDP4CrNLwadeM")
            elif song == 4:
                webbrowser.open("https://music.youtube.com/watch?v=fZZFKVbQpoE&list=OLAK5uy_lAcMlUZLqvtX29195rALpoAHypnkM2y_o")
            elif song == 5:
                webbrowser.open("https://music.youtube.com/watch?v=opwZ_PJ-F_E")
        elif "what time is it now" in req:
                time = datetime.datetime.now().strftime("%H:%M")
                speak("Current time is " + str(time))
        elif "what date is it today" in req:
                time = datetime.datetime.now().strftime("%d:%m")
                speak("Current date is " + str(time))
        elif "add" in req.lower():  # Convert to lowercase for better matching
            task = req.replace("add", "")# Remove "new task" and strip spaces
            if task:  # Ensure task is not empty
                speak("Adding task: " + task)
                with open("todo.txt", "a") as file:
                    file.write(task + "\n")  # Write task with a new line
        elif "speak task" in req:
            with open ("todo.txt", "r") as file:
                speak("Work we have to do today is: " + file.read())
        elif "show work" in req:
            with open ("todo.txt", "r") as file:
                tasks = file.read()
            notification.notify(
                title = "Today's work",
                message = tasks
            ) 
        elif "open youtube" in req:
            webbrowser.open("www.youtube.com") 
        elif "open" in req:
            query = req.replace("open","")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.press("enter")
        elif "wikipedia" in req:
            query = req.replace("jarvis","")
            query = req.replace("search wikipedia","")
            print(req)
            result =  wikipedia.summary(req, sentences=2) 
            print(result)
            speak(result)
        elif "search" in req:
            query = req.replace("search", req)
            webbrowser.open("https://www.google.com/search?q="+ query)
        elif "find song" in req:
            query = req.replace("find this song", " ")
            webbrowser.open("https://www.youtube.com/results?search_query="+ query)
main_process()