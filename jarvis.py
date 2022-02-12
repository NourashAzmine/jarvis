import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import smtplib
import os


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour <= 6:
        speak("Good Afternoon")
    else:
        speak("Good Night")
    speak("Hello, I am jarvis. How I can help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}")
        return query
    except Exception as e:
        print(e)
        print("Please say that again.....")
        return "None"


def chrome_brow(url):
    chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"
    webbrowser.register(
        "chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get("chrome").open_new_tab(url)


def send_mail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("sdjnasx@gmail.com", "Na252577")
    server.sendmail("sdjnasx@gmail.com", to, content)
    server.close()


if __name__ == '__main__':

    while True:
        wishme()
        query = takeCommand().lower()
        if "wikipedia" in query:
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, 2)
            speak("According to wikipedia:")
            speak(result)
        elif "open youtube" in query:
            url = "youtube.com"
            chrome_brow(url)
        elif "open google" in query:
            url = "google.com"
            chrome_brow(url)
        elif "check mail" in query:
            url = "https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"
            chrome_brow(url)
        elif "time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Time is {time}")
        elif "open vs" in query:
            path = "C:\\Users\\noura\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        elif "send email" in query:
            try:
                speak("What should I send?")
                content = takeCommand()
                to = "nourashazmine@gmail.com"
                send_mail(to, content)
                speak("email has been send")
            except Exception as e:
                print(e)
                print("Sorry, I am not able to send this email")
        elif "sleep" or "stop" or "quit" or "exit" or "turn off jarvis" in query:
            speak("good bye!")
            exit()
