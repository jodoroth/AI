import os
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig
import eel
import datetime
import pywhatkit
import wikipedia
import webbrowser

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

def searchapplications(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        text_to_speech("This is what I found on google")

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            text_to_speech(result)

        except:
            text_to_speech("No speakable output available")

def searchYoutubes(query):
    if "youtube" in query:
        text_to_speech("This is what I found for your search!") 
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        query = query.replace("jarvis","")
        web  = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        text_to_speech("Done")

def searchWikipedias(query):
    if "wikipedia" in query:
        text_to_speech("Searching from wikipedia....")
        query = query.replace("wikipedia","")
        query = query.replace("search wikipedia","")
        query = query.replace("jarvis","")
        results = wikipedia.summary(query,sentences = 2)
        text_to_speech("According to wikipedia..")
        print(results)
        text_to_speech(results)
