import datetime
import operator
import os
import PyPDF2
import azure.cognitiveservices.speech as speechsdk
from bs4 import BeautifulSoup
import cv2
import pyautogui
import speedtest
from pywikihow import WikiHow, search_wikihow
import pywikihow
import psutil
import pywintypes
import pythoncom
import pywhatkit as kit
from requests import get
import requests
import win32com.client
import wikipedia
import webbrowser
import datetime 
import random
import webbrowser
import time  
import pyjokes
import sys

speech_key = "6a7cc72526ce4a5188d885b1f5543952"  # Replace with your Speech service key
service_region = "eastus2"  

def text_to_speech(text):
# Replace with your Speech service region
    # Create a speech configuration object
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    # Create a speech synthesizer object
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)
    # Synthesize the text and save it to a file
    result = synthesizer.speak_text_async(text).get()
    
   # result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted
    audio_data = result.audio_data
    
    return audio_data


def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    #print("Speak into your microphone.")
    print("Listening...")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    print("Recognizing...")
    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return (speech_recognition_result.text.lower())
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
    return ""

def news():
 main_url='http://newsapi.org/v2/top-headlines?sources=techcrunch&apikey=76359ed23ffe4b7caebf5357d44fab0c'
 main_page=requests.get(main_url).json()
 articles=main_page["articles"]
 head=[]
 day=["first","second","third","fourth","sixth","seventh","eight","ninth","tenth"]
 for ar in articles:
    head.append(ar["title"])
 for i in range(len(day)):
    text_to_speech(f"today's {day[i]} news is {head[i]}")

def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds) 

def test_internet_speed():
    try:
        st = speedtest.Speedtest()
        # Perform the download speed test
        download_speed = st.download() / 1000000  # Convert to Mbps

        # Perform the upload speed test
        upload_speed = st.upload() / 1000000  # Convert to Mbps

        # Print the results
        text_to_speech(f"we have {download_speed} Mbps downloading speed and {upload_speed} Mbps uploading speed")

    except speedtest.SpeedtestException as e:
        print("An error occurred during the speed test:", str(e))

def pdf_reader():   
   
   file=open('Backend\\python.pdf','rb')
   reder=PyPDF2.PdfReader(file)
   totalPages=len(reder.pages)
   text_to_speech(f"Total numbers of pages in this book {totalPages}")
   text_to_speech("Tell me the page number I have to read")
   pagenumber=int(input("Please enter the page number:"))
   page1=reder.pages[2]
#print(page1.extract_text())
   pdfdata=page1.extract_text()
   text_to_speech(pdfdata)

  

def wish():
    hour  = int(datetime.datetime.now().hour)
    c = datetime.datetime.now().time()
# Displays Time
    current_time = c.strftime('%H:%M')
    if hour>=0 and hour<=12:
        text_to_speech("Good Morning Joyce")
        text_to_speech(f"Its, {current_time} AM")
    elif hour >12 and hour<=18:
        text_to_speech("Good Afternoon Joyce")
        text_to_speech(f"Its, {current_time} PM")

    else:
        text_to_speech("Good Evening Joyce")
        text_to_speech(f"Its, {current_time} PM")
    text_to_speech("I am Quanta, How can I help you ?")

    

    
def TaskExecution():
    wish()
    dictapp = {"commandprompt":"cmd","paint":"paint","notepad":"notepad","notepad++":"Notepad++","edge":"msedge","mspaint":"mspaint","snipping tool":"Snipping Tool","Outlook":"Outlook","case Buddy":"CaseBuddy","onenote":"OneNote","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt"}
    while True:
        query=recognize_from_microphone().lower()
        if 'open' in query:
          #  npath="C:\\Windows\\System32\\notepad.exe"
           # os.startfile(npath)
        #elif 'open' in query:
            keys = list(dictapp.keys())
            for app in keys:
                if app in query:
                    os.system(f"start {dictapp[app]}")
        elif "open command prompt" in query:
	        os.system("start cmd")
        elif "open camera" in query:
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()            
        elif "close" in query:
            keys = list(dictapp.keys())
            for app in keys:
                if app in query:
                    os.system(f"taskkill /f /im {dictapp[app]}.exe")            
        elif "play music" in query:	
            music_dir="Frontend\\assests\\playsound\\"
            songs=os.listdir(music_dir)
            #rd=random.choice(songs)
            for song in songs:
	            if song.endswith('.mp3'):
		            os.startfile(os.path.join(music_dir,song))
        
        elif "ip address" in query:
            ip=get('https://api.ipify.org').text
            text_to_speech(f"your IP address is {ip}")
        elif "read pdf" in query:
	        pdf_reader()
	
        elif "wikipedia" in query:
            text_to_speech("Searching wikipedia....")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 2)
            text_to_speech("According to wikipedia..")
            print(results)
            text_to_speech(results)
        
        elif "Youtube" in query:
            text_to_speech("This is what I found for your search!") 
            query = query.replace("youtube search","")
            query = query.replace("youtube","")
            web  = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            kit.playonyt(query)
            text_to_speech("Done")
   

        elif "open facebook" in query:
	        webbrowser.open("https://www.facebook.com")
        
        elif "hide all files" in query or "hide this folder" in query:
            try:    
                os.system("attrib +h /s /d")
                text_to_speech("All the files in this folder are now hidden")
            except:
                text_to_speech("No directory found.")
        elif "visible" in query:
            try:    
                os.system("attrib -h /s /d")
                text_to_speech("All the files in this folder are now visible")
            except:
                text_to_speech("No directory found.")
        elif "open stackoverflow" in query:
	        webbrowser.open("www.stackoverflow.com")
        elif "do some calculations" in query or "can you calculate" in query:
            text_to_speech("What do you want me to calculate")
            print("Listening...")
            query=recognize_from_microphone().lower()
            def get_operator_fn(op):
                return{
                '+':operator.add,
                '-':operator.sub,
                '*':operator.mul,
                'divided':operator._truediv_,
                     }[op]
            def eval_binary_expr(op1,oper,op2):
                 op1,op2=int(op1),int(op2)
                 return  get_operator_fn(oper)(op1,op2)
            text_to_speech("Result is")
            text_to_speech(eval_binary_expr(*(query.split())))
         
        elif "open google" in query:
            text_to_speech("What should I search on google")
            cm=recognize_from_microphone().lower()
            webbrowser.open(f"{cm}")
        elif "send message" in query:
                kit.sendwhatmsg('+91 9094562087',"hello from python",12,00)   
        elif "play song on youtube" in query:
	            kit.playonyt("See you again") 
        elif "set alarm" in query:
            alarmtime=int(datetime.datetime.now().hour)
            if alarmtime==22:
                music_dir="Frontend\\assests\\playsound\\"
                songs=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir,songs[0]))
        elif "tell me a joke" in query:
                joke=pyjokes.get_joke()
                text_to_speech(joke)
        elif "shut down the system" in query:
	            os.system("shutdown /s /t 5")
        elif "restart the system" in query:
	            os.system("shutdown /r /t 5")
        elif 'switch the window' in query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
        elif "tell me news" in query:
                text_to_speech("Fetching the latest News..")
                news()
        elif  "sleep the system" in query:
            	os.system("rundll32.exe powrprof.dll.SetSuspendState 0,1,0")
        elif "send e-mail" in query:
            try:
                ol=win32com.client.Dispatch("outlook.application")
                olmailitem=0x0 #size of the new email
                newmail=ol.CreateItem(olmailitem)
                newmail.Subject= 'Followup-Email'
                newmail.To='jodoroth@microsoft.com'
                text_to_speech("what is the Content..")
                mailbody=recognize_from_microphone().lower()
                newmail.Body= mailbody

                # attach='C:\\Users\\admin\\Desktop\\Python\\Sample.xlsx'
                # newmail.Attachments.Add(attach)

                # To display the mail before sending it
                # newmail.Display() 

                newmail.Send()
            except Exception as e:
                print(e)
                text_to_speech("Sorry Email couldnt be sent")
        elif  "where we are" in query:
            text_to_speech("Let me check")
            try:
                ip_request=requests.get('https://get.geojs.io/v1/ip.json')
                ipAdd=ip_request.json()['ip']
                url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_request=requests.get(url)
                geo_data=geo_request.json()

                #ipAdd=requests.get('https://api/ipify.org').text
                #print(ipAdd)
                #url='https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                #geo_requests=requests.get(url)
                #geo_data=geo_requests.json()
                city=geo_data['city']
                country=geo_data['country']
                text_to_speech(f"we are in {city} city of{country}")
            except Exception as e:
                text_to_speech(f"Due to network issue I am not able to find where you are")
                pass     
        elif "take screenshot" in query or "take a screenshot" in query:
                text_to_speech("Please tell me the name of the screenshot file")
                name=recognize_from_microphone().lower()
                text_to_speech("hold the screen for few seconds, taking screenshot")
                time.sleep(3)
                img=pyautogui.screenshot()
                img.save(f"{name}png")
                text_to_speech("Screenshot is saved in main folder")   
        elif "temperature" in query:
                text_to_speech("In which City?")
                city = recognize_from_microphone().lower()
                search = f"temperature in {city} "
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                text_to_speech(f"Current {search} is {temp}")    
        elif "read pdf" in query:
            	pdf_reader()
        elif "go to sleep" in query:
                text_to_speech("Ending the program")
        elif "bye" in query:
                text_to_speech("bye")
        elif "how are you" in query:
                text_to_speech("Doing good")
        elif "thank you" in query:
                text_to_speech("Welcome") 
        elif "play some other song" in query:
            text_to_speech("What song you want me to play")
            getdata=recognize_from_microphone().lower()
            if "song of your choice" in getdata:
                text_to_speech("Okay")
                music_dir ='Backend\\songs'
                songs = os.listdir(music_dir)
                song = random.randint(0,len(songs))
                os.startfile(os.path.join(music_dir, songs[0]))
        elif 'activate how to do' in query:
            text_to_speech('how-to-do mode activated')
            #while True:
            text_to_speech('Ask the query')
            how = recognize_from_microphone()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            text_to_speech(how_to[0].summary)
                #except Exception as e:
                #	text_to_speech("Sorry, Not able to find the results")
        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
                battery=psutil.sensors_battery()
                percentage=battery.percent
                text_to_speech(f"System has {percentage} percent battery")
                if percentage>=75:
                    text_to_speech("we have enough power to continue the work")
                elif percentage>=40 and percentage<=75:
                    text_to_speech("we should connect the system to charging point")
                elif percentage>=15 and percentage<=30:
                    text_to_speech("we don't have enough power to work,connect the system to charging point")
                elif percentage<=15:
                    text_to_speech("we have very low power, the system will shutdown soon")
        elif "internet speed" in query:
                test_internet_speed()
        elif 'alarm' in query:
            text_to_speech("please tell me the time to set alarm. for instance, set alarm to 6:00 am")
            tt=recognize_from_microphone()
            tt=tt.replace("set alarm to ","")
            tt=tt.replace(".","")
            tt=tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)
        elif 'volume up' in query:
	        pyautogui.press("volumeup")
        elif 'volume down' in query:
	        pyautogui.press("volumedown")
        elif 'volume mute' in query or 'mute' in query:	
	        pyautogui.press("volumemute")
        elif "no thanks" in query:
                text_to_speech("Sure! Have a great day")
                sys.exit()

        text_to_speech("Do you need any other help")

if __name__ == "__main__":
    while True:
        permission=recognize_from_microphone()
        if 'wake up' in permission:
            TaskExecution()
        elif "goodbye" in permission:
            text_to_speech("Thank you for using me! Have a great day")
            sys.exit()
     
   