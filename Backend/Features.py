from calendar import calendar
import ctypes
from datetime import datetime, time
import os
import random
import webbrowser
from bs4 import BeautifulSoup
from playsound import playsound # type: ignore
import eel
import pywhatkit
from ctypes import *
import smtplib

from email.message import EmailMessage

import requests

from Backend.command import recognize_from_microphone, text_to_speech
from Backend.config import ASSISTANT_NAME


def playAssistantSound():
    music_dir="Frontend\\assests\\playsound\\mixkit-technology-computer-calculations-3122.wav"
    playsound(music_dir)

@eel.expose
def playClickSound():
    music_dir="Frontend\\assests\\playsound\\mixkit-select-click-1109.wav"
    playsound(music_dir)   
    

def openCommand(query):
    query=query.replace(ASSISTANT_NAME,"")
    queryrep=query.replace("open","")
    query.lower()
    
    
    if "open" in query:
        text_to_speech("Opening"+ queryrep)
        from Backend.Dictapp import openappweb
        openappweb(query)
    if "go to sleep" in query:
        text_to_speech("Ending the program")
    if "bye" in query:
        text_to_speech("bye")
    if "how are you" in query:
        text_to_speech("Doing good")
    if "thank you" in query:
        text_to_speech("Welcome") 
    if "close" in query:
        from Dictapp import closeappweb
        closeappweb(query)
    if "google" in query:
        from Backend.Applications import searchapplications
        searchapplications(query)
    if "youtube" in query:
        from Backend.Applications import searchYoutubes
        searchYoutubes(query)
    if "wikipedia" in query:
        from Backend.Applications import searchWikipedias
        searchWikipedias(query)     
    elif "temperature" in query:
        search = "temperature in",query
        url = f"https://www.google.com/search?q={search}"
        r  = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temp = data.find("div", class_ = "BNeawe").text
        text_to_speech(f"current{search} is {temp}")
    elif "where is" in query:
                ind = query.lower().split().index("is")
                location = query.split()[ind + 1:]
                url = "https://www.google.com/maps/place/" + "".join(location)
                speak = speak + "This is where " + str(location) + " is."
                webbrowser.open(url)

    elif "what is the weather in" in query:
                key = ""
                weather_url = "http://api.openweathermap.org/data/2.5/weather?"
                ind = query.split().index("in")
                location = query.split()[ind + 1:]
                location = "".join(location)
                url = weather_url + "appid=" + key + "&q=" + location
                js = requests.get(url).json()
                if js["cod"] != "404":
                    weather = js["main"]
                    temperature = weather["temp"]
                    temperature = temperature - 273.15
                    humidity = weather["humidity"]
                    desc = js["weather"][0]["description"]
                    weatherResponse = " The temperature in Celcius is " + str(temperature) + " The humidity is " + str(
                        humidity) + " and The weather description is " + str(desc)
                    speak = speak + weatherResponse
                else:
                    speak = speak + "City Not Found"
    elif "date" in query or "day" in query or "month" in query:
                strTime = datetime.datetime.now()
                date_now=datetime.datetime.today()
                week_now=calendar.day_name[date_now.weekday()]
                month_now=strTime.month
                day_now=strTime.day
                months=['January', 'February', 'March', 'April', 'May', 'June', 
                        'July', 'August', 'September', 'October', 'November', 'December']
                days=['1st','2nd','3rd','4th','5th','6th','7th','8th','9th','10th','11th','12th','13th','14th','15th','16th',
                    '17th','18th','19th','20th','21st','22nd','23rd','24th','25th','26th','27th','28th','29th','30th','31st']
                
                text_to_speech(f'Today is {week_now},{months[month_now-1]} the {days[day_now-1]}')  
    elif "time" in query:
                now = datetime.datetime.now()
                meridiem = ""
                if now.hour >= 12:
                    meridiem = "p.m"
                    hour = now.hour - 12
                else:
                    meridiem = "a.m"
                    hour = now.hour

                if now.minute < 10:
                    minute = "0" + str(now.minute)
                else:
                    minute = str(now.minute)
                speak = speak + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."  
                text_to_speech(speak)  
    elif "Sleep" in query:
                text_to_speech("Going to sleep")
                exit()
    elif "shutdown the system" in query:
                text_to_speech("Are You sure you want to shutdown")
                shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                if shutdown == "yes":
                    os.system("shutdown /s /t 1")
                elif shutdown == "no":
                    print("")
    elif "who are you" in query or "define yourself" in query:
                speak = speak + "Hello, I am Quanta. Your Virtual Assistant. I am here to make your life easier. You can command me to perform various tasks such as asking questions or opening applications etcetera"

    elif "your name" in query:
                speak = speak + "My name is Quanta"

    elif "who am I" in query:
                speak = speak + "You must probably be a human"

    elif "how are you" in query:
                speak = speak + "I am doing good, Thank you"
                speak = speak + "\nHow are you?"

    elif "fine" in query or "good" in query:
                speak = speak + "It's good to know"

    elif "don't listen" in query or "stop listening" in query or "do not listen" in query:
                text_to_speech("for how many seconds do you want me to sleep")
                a = int(recognize_from_microphone().lower())
                time.sleep(a)
                speak = speak + str(a) + " seconds completed. Now you can ask me anything"
                text_to_speech(speak)

    elif "change background" in query or "change wallpaper" in query:
                img = r"C:\Users\jodoroth\Desktop\New folder"
                list_img = os.listdir(img)
                imgChoice = random.choice(list_img)
                randomImg = os.path.join(img, imgChoice)
                ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
                text_to_speech("Background changed successfully")

    elif "exit" in query or "quit" in query:
                exit()
    elif "play music" in query or "play song" in query:
                text_to_speech("Here you go")
                import playsound
                var_audiodir="frontend\\Documents\\playsound\\RiseUp.mp3"
                playsound(var_audiodir)
    elif "empty recycle bin" in query:
                winshell.recycle_bin().empty( # type: ignore
                    confirm=True, show_progress=False, sound=True
                )
                text_to_speech("Recycle Bin Emptied")
    elif "joke" in query:
                speak = speak + pyjokes.get_joke()   # type: ignore
    elif "make a note" in query:
                text_to_speech("What would you like me to write down?")
                note_text = recognize_from_microphone()
                note(note_text) # type: ignore
                text_to_speech("I have made a note of that.")     
    elif "email to computer" in query or "gmail to computer" in query:
                try:
                    text_to_speech("What should I say?")
                    content = recognize_from_microphone()
                    to = "Receiver email address"
                    send_email(to, content) # type: ignore
                    text_to_speech("Email has been sent !")
                except Exception as e:
                    print(e)
                    text_to_speech("I am not able to send this email")
    elif "send whatsapp" in query:
                pywhatkit.sendwhatmsg('+91 9094562087',"hello from pythonnnnnn",15,13)
 
    elif "mail" in query or "email" in query or "gmail" in query:
                try:
                    text_to_speech("What should I say?")
                    content = recognize_from_microphone()
                    text_to_speech("whom should i send")
                    to = input("Enter To Address: ")
                    send_email(to, content) # type: ignore
                    text_to_speech("Email has been sent !")
                except Exception as e:
                    print(e)
                    text_to_speech("I am not able to send this email")

    
    
    