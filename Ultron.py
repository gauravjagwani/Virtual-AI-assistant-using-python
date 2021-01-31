import pyttsx3
import datetime
import speech_recognition as sr
import os
import webbrowser
import wikipedia
# import smtplib
import pyautogui
import time

MASTER="Gaurav"

engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    print (hour)
    if hour >=0 & hour<12:
        speak("Good morning"+ MASTER)

    elif hour>=12 & hour<18:
        speak("Good Afternoon"+ MASTER)

    else:
        speak("Good evening!"+MASTER)

    speak("I am Ultron, Your virtual desktop assistant, please tell me sir how may I help you")

def takecommand():
    #Takes microphone input from users

    r= sr.Recognizer()
    with sr.Microphone() as source:
        print ("Listening...")
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query =r.recognize_google(audio,language="en-in")
        print(f"User said:{query}\n")

    except Exception as e:
        print("Say that again please")
        query="None"

    return query

# def sendEmail(to,content):
#     server= smtplib.SMTP('smtp.gmail.com')


# Main programm

def main():
    speak("Initializing Ultron...")
    wishme()
    # takecommand()
    query = takecommand()

    # Logic for excecuting task
# For launching Wikipedia.com
    if "wikipedia" in query.lower():
        speak('Searching wikipedia...')
        query= query.replace("wikipedia", "")
        results= wikipedia.summary(query,sentences=2)
        print(results)
        speak(results)
# For launching Youtube.com
    elif 'open youtube' in query.lower():
        speak('Opening Youtube')
        url='https://www.youtube.com/'
        # Windows
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
# For launching Flipkart.com
    elif 'open flipkart' in query.lower():
        speak('Opening Flipkart')
        url='https://www.flipkart.com/?gclid=EAIaIQobChMI4dXx1Zq67QIVRw4rCh1_egoTEAAYASAAEgLPc_D_BwE&ef_id=EAIaIQobChMI4dXx1Zq67QIVRw4rCh1_egoTEAAYASAAEgLPc_D_BwE:G:s&s_kwcid=AL!739!3!354086747743!e!!g!!flipkart&gclsrc=aw.ds&&semcmpid=sem_8024046704_brand_city_goog'
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
# For launching Amazon.com
    elif 'open amazon' in query.lower():
        speak('Opening Amazon')
        url='https://www.amazon.in/ref=nav_logo'
        # Windows
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
# For launching Google.com
    elif 'open google' in query.lower():
        speak('Opening Google')
        url='https://www.google.com/'
        # Windows
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)


    # elif 'play music' in query.lower():
        # songs = os.listdir()

    elif 'the time' in query.lower():
        strTime =datetime.datetime.now().strftime("%H,%M:%S")
        speak(f"The time is {strTime}")
        
# For opening VS code 
    elif 'open code' in query.lower():
        speak('Opening VS code')
        codepath=" " # put file location here
        os.startfile(codepath)
        
# For opening music app 
    elif 'open music' in query.lower():
        codepath=""# put file location here
        os.startfile(codepath)
        
# For taking Screeshots
    elif "take screenshot" in query.lower() or "take a screenshot" in query.lower():
        speak("Sir please tell me the name of this screenshot file")
        name=takecommand().lower()
        speak("Sir please hold the screen for few seconds, i am taking screenshot ")
        time.sleep(3)
        img=pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("Iam Done sir, screenshot has been saved in our main folder")

        


    elif 'thank you' in query.lower():
        speak(f"Your welcome {MASTER}")
main()




