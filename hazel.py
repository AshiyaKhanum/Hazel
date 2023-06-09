import pyttsx3
import speech_recognition as sr # install speechRecognition
import datetime
import wikipedia #install
import webbrowser
import os 
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[2].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning!")
    elif hour >= 12 and hour<18:
        speak("Good Afternon!")
    else:
        speak("Good Evening")

    speak("I am Hazel Madam. Please tell me how may I help you")    

def takeCommand():
    # it takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio)
        print(f'User said: {query}')

    except Exception as e:
        print(e)
        print('Say that again....')
        return "None" 
    return query    

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("ashiyakhanum19@gmail.com", 'kutuydoggjoxlxpo')
    server.sendmail('20EC010@ssit.edu.in', to, content)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak("Speaking Wikipedia...")
            query =query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2) #if we want to read the sentences through online
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com') 

        elif 'open google' in query:
            webbrowser.open('google.com')  

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        # elif 'play music' in query:
        #     music_dr = path 
        #     songs = os.listdir(music_dr)
        #     print(songs)
        #     os.startfile(os.path.join(music_dr, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f'Madam, the time is {strTime}')

        elif 'open code' in query:
            codePath = "C:\\Users\\Ashiya Khanum\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)  
        
        elif 'thank you' in query:
            speak('Welcome chand')

        elif 'send mail to arshiya' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "ashiyakhanum19@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Ashiya. I am not able to send this email")  

        elif 'exit' in query:
            exit()    


