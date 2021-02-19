import pyttsx3  # install using pip install pyttx3
import datetime  # built-in module
import speech_recognition as sr  # install pip install SpeechRecognition
import wikipedia #pip install wikipedia
import webbrowser # built-in module
import os # built-in module
import smtplib # built-in module
import cv2 #pip install opencv-python

engine = pyttsx3.init('sapi5')  # Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices')

# 0 for male voice (David) 1 for female voice (Zira)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)  # engine will say audio
    engine.runAndWait()  # fumctiom

#this method just open the camera
def opencamera():
    # define a video capture object 
    vid = cv2.VideoCapture(0)
    
    while(True): 
        
        # Capture the video frame 
        # by frame 
        ret, frame = vid.read() 
    
        # Display the resulting frame 
        cv2.imshow('frame', frame) 
        
        """ the 'x' button is set as the 
        quitting button you may use any 
        desired button of your choice 
         """
        if cv2.waitKey(1) & 0xFF == ord('x'): 
            break
    
    
    # After the loop release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows() 


def takeCommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # adjust the threshhold eneergy background sound
        r.adjust_for_ambient_noise(source)
        print("Listening.......")
        # seconds of non-speaking audio before a phrase is considered complete
        r.pause_threshold = 0.8

        audio = r.listen(source)
    try:
        print("Recognizing.......")
        # query = r.recognize_google(audio, language='en-in')
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

#this will wish you according to time
def wishing():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:  # between 0 to 12 which means morning time
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon")
    else:
        speak("Good Evening")

    speak("Hey Fifi How may I help You:")


if __name__ == "__main__":
    wishing()
    while True:
        query = takeCommand().lower()

        # logic for task on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        

        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")
        
        elif 'camera' in query:
            try:
                opencamera()
            except Exception as e:
                print(e)
                speak("Sorry I don't get you")


        elif 'play music' in query:
            music = 'C:\\Users\\Dell\\Desktop\\gues\\AI BOT\\music'
            songs = os.listdir(music)
            print(songs)
            # paly first music in the list
            os.startfile(os.path.join(music, songs[0]))

        elif 'time' in query:
            starttime = datetime.datetime.now().strftime("%M:%S:%H")  # time in string
            speak(f"The current time is : {starttime}")

        elif 'vs code' in query:
            pathh = '"C:\\Users\\Dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"'
            os.startfile(pathh)

        elif 'email to ' in query:

            try:
                speak("What should I say?")
                content = takeCommand()
                to = "yourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry I cannot send mail")
