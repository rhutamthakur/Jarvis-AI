import pyttsx3
import speech_recognition as s
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greeting():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        print("Good Afternoon!")
        speak("Good Afternoon!")

    else:
        print("Good Evening!")
        speak("Good Evening!")

    print("I am Jarvis, sir. Please let me know how may I help you")
    speak("I am Jarvis Sir. Please let me know how may I help you")

def acceptCommand():
    r = s.Recognizer()
    with s.Microphone() as source:
        print("\nListening to command..")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing said command...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Unable to process request. Please repeat command...\n")
        return "None"
    return query

def wikipediaResults(query):
    try:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        print(f"The results are as follows:\n\n{results}")
        speak(results)
    except Exception as e:
        print("No matches found!")
        return "None"

def openBrowser(query):
    try:
        if 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'gmail' in query:
            webbrowser.open("gmail.com")
    except Exception as e:
        print("No such websites found!")
        return "None"

def playMusic():
    music_dir = 'D:\Python Project work\Songs'
    songslist = os.listdir(music_dir)
    n = random.randint(0, len(songslist) - 1)
    os.startfile(os.path.join(music_dir, songslist[n]))

def displayTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time as of now is {strTime}")
    print(f"Sir, the time as of now is {strTime}")

def openIDE():
    codePath = "C:\\Users\\Rhutam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

def emailSender(receiver, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    f=open('Details.txt','r')
    UN=f.readline()
    PW=f.readline()
    server.login(UN, PW)
    server.sendmail('pyproject21@gmail.com', receiver, body)
    server.close()

def emailQuery(choice):
    if choice==1:
        try:
            speak("What should I say?")
            body = acceptCommand()
            receiver= "pyproject21@gmail.com"
            emailSender(receiver, body)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry Sir. I am not able to send this email")
    elif choice==2:
        try:
            speak("What should I say?")
            body = input("Enter content of email:\n")
            receiver= "pyproject21@gmail.com"
            emailSender(receiver, body)
            speak("Email has been sent!")
        except Exception as e:
            print(e)
            speak("Sorry Sir. I am not able to send this email")

if __name__ == "__main__":
    greeting()
    while True:
        choice=int(input("\nChoose:\n1. Voice Recognition\n2. Menu Driven\n3. Exit Program\nEnter your choice:"))
        if choice==1:
           while True:
                query = acceptCommand().lower()
                if 'wikipedia' in query:
                    wikipediaResults(query)
                elif 'website' in query:
                    openBrowser(query)
                elif 'music' in query:
                    playMusic()
                elif 'the time' in query:
                    displayTime()
                elif 'open vs code' in query:
                    openIDE()
                elif 'email' in query:
                    emailQuery(choice)
                elif 'stop' in query:
                    break
                else:
                    speak("Unable to process request. Please repeat command")
        elif choice==2:
            while True:
                print("1. Search On Wikipedia\n2. Open Google/Youtube/Gmail website\n3. Play Music\n4. Find out Current Time\n5. Open VS Code\n6. Write email\n7. End Program\n\n")
                inp=int(input("Enter command to be followed from the menu:"))
                if inp==1:
                    query=input("Enter subject:")
                    wikipediaResults(query)
                elif inp==2:
                    query = input("Enter website name:")
                    openBrowser(query)
                elif inp==3:
                    playMusic()
                elif inp==4:
                    displayTime()
                elif inp==5:
                    openIDE()
                elif inp==6:
                    emailQuery(choice)
                elif inp==7:
                    break
                else:
                    speak("Unable to process request. Please repeat command")
        elif choice==3:
            break