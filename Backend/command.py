import os
import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.speech import SpeechConfig, SpeechRecognizer, AudioConfig
import eel

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

@eel.expose
def recognize_from_microphone():
    # This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
    speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)
    speech_config.speech_recognition_language="en-US"

    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    #print("Speak into your microphone.")
    print("Listening...")
    eel.DisplayMessage("Listening...")
    speech_recognition_result = speech_recognizer.recognize_once_async().get()
    print("Recognizing...")
    eel.DisplayMessage("Recognizing...")
    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        eel.DisplayMessage("Recognized...")
      # text_to_speech(speech_recognition_result.text.lower())
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
    
@eel.expose
def allcommands():
    query=recognize_from_microphone()
    from Backend.Features import openCommand
    openCommand(query)
   
 
     
   