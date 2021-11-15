import pyttsx3
import datetime
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import playsound



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good AfterNoon!")
    elif hour>=17 and hour<20:
        speak("Good Evening!")
    else:
        speak("Good Night!")
    speak("I am vitual assistant of SOURAV So how may I help you")

def takeCommand():
    #it takes input from user voice
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        #query = r.recognize_google(audio, language='hi-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please")

        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("sdas99579@gmail.com", 'Souravdas@1')
    server.sendmail('sdas99579@gmail.com', to, content)
    server.close()


if __name__=="__main__":
    # speak("This is a virtual Assistant")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().upper()

    #logic based on tasks queries
        if 'WHO ARE YOU' in query:
            speak("I am a Virtual Assistant")
        elif 'WHO CREATED YOU' in query:
            speak("Saurav created me!")
        elif 'HOW ARE YOU' in query:
            speak("I am good, and what about you")
        elif 'PLAY' in query:
            query = query.replace("PLAY", "")
            speak(f"Playing {query}")
            pywhatkit.playonyt(query)
        elif 'WIKIPEDIA' in query:
            try:
                speak('Searching wikipedia...')
                query = query.replace("WIKIPEDIA", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                speak("Unable to catch please speak again")
        elif 'OPEN YOUTUBE' in query:
            webbrowser.open("https://youtube.com/")
        elif 'OPEN GOOGLE' in query:
            webbrowser.open("https://www.google.co.in/")
        elif 'OPEN HACKERRANK' in query:
            webbrowser.open("https://www.hackerrank.com/")
        elif 'OPEN STACK OVERFLOW' in query:
            webbrowser.open("https://stackoverflow.com/")
        elif 'OPEN GEEKS FOR GEEKS' in query:
            webbrowser.open("https://www.geeksforgeeks.org/")
        elif 'OPEN HACKEREARTH' in query:
            webbrowser.open("https://www.hackerearth.com/")
        elif 'OPEN CODECHEF' in query:
            webbrowser.open("https://www.codechef.com/")
        # elif 'PLAY MUSIC' in query:
        #     music_dir = 'E:\\downloads'
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))
        elif 'THE TIME' in query:
            stringTime = datetime.datetime.now().strftime("%I:%M:%S %p")
            speak(f"Sir the time is: {stringTime}")
        elif 'OPEN CODE BLOCKS' in query:
            codeBlocks = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
            os.startfile(codeBlocks)
        elif 'OPEN ECLIPSE' in query:
            eclipse = "C:\\Users\\d_sourav\\eclipse\\java-2021-06\\eclipse\\eclipse.exe"
            os.startfile(eclipse)
        elif 'OPEN GIT BASH' in query:
            gitBash = "C:\\Program Files\\Git\\git-bash.exe"
            os.startfile(gitBash)
        elif 'OPEN WAMP' in query:
            wamp = "C:\\wamp64\\wampmanager.exe"
            os.startfile(wamp)
        elif 'OPEN PYCHARM' in query:
            pyCharm = "C:\\Program Files\\JetBrains\\PyCharm 2021.2.3\\bin\\pycharm64.exe"
        elif 'A JOKE' in query:
            speak(pyjokes.get_jokes())
        elif 'EMAIL TO SAURAV' in query:
            try:
                speak("what should I say?")
                content = takeCommand()
                to = "sdas99579@gmail.com"
                sendEmail(to,content)
                speak("The email has been send")
            except Exception as e:
                speak("sorry I am unable to send this email due to some error")

        elif 'QUIT' in query or 'abort' in query or 'EXIT in query':
            speak("Thank you...bye..bye")
            exit(0)
        speak('Next Command! Sir!')




