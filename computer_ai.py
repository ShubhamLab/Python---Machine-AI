import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir, how may i help u ??")

    elif hour>=12 and hour<18:
        speak("good afternoon sir, how may i help u ??")   

    else:
        speak("good evening sir, how may i help u ??")          

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishMe()
    while True:
  
        query = takeCommand().lower()

        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('http://youtube.com', new=2)
            

        elif 'open google' in query:
            webbrowser.open('http://google.com',new=3)

        elif 'play arcade' in query:
            webbrowser.open('https://www.youtube.com/watch?v=PNozaFzqOvI',new=4)


        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com/",new=5)

        elif 'open my mail' in query:
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox",new=6)

        elif 'open maps' in query:
            webbrowser.open("https://www.google.com/maps/",new=7)

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        

            
