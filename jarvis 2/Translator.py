# from fnmatch import translate
# from time import sleep
# from googletrans import Translator
# import googletrans #pip install googletrans
# from gtts import gTTS
# import googletrans
# import pyttsx3
# import speech_recognition 
# import os
# from playsound import playsound
# import time

# engine = pyttsx3.init("sapi5")
# voices = engine.getProperty("voices")
# engine.setProperty("voice", voices[0].id)
# rate = engine.setProperty("rate",170)

# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()

# def takeCommand():
#     r = speech_recognition.Recognizer()
#     with speech_recognition.Microphone() as source:
#         print("Listening.....")
#         r.pause_threshold = 1
#         r.energy_threshold = 300
#         audio = r.listen(source,0,4)

#     try:
#         print("Understanding..")
#         query  = r.recognize_google(audio,language='en-in')
#         print(f"You Said: {query}\n")
#     except Exception as e:
#         print("Say that again")
#         return "None"
#     return query

# def translategl(query):
#     speak("SURE SIR")
#     print(googletrans.LANGUAGES)
#     translator = Translator()
#     speak("Choose the language in which you want to translate")
#     b = input("To_Lang :- ")   
#     text_to_translate = translator.translate(query,src = "auto",dest= b,)
#     text = text_to_translate.text
#     try : 
#         speakgl = gTTS(text=text, lang=b, slow= False)
#         speakgl.save("voice.mp3")
#         #playsound("voice.mp3")
        
#         time.sleep(5)
#         os.remove("voice.mp3")
#     except:
#         print("Unable to translate")




















import pyttsx3
import speech_recognition as sr
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import os
import time

# Initialize pyttsx3 TTS engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, timeout=4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return "None"
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return "None"
    return query

def translategl(query):
    speak("SURE SIR")
    print(LANGUAGES)
    
    translator = Translator()
    speak("Choose the language in which you want to translate")
    
    b = input("To_Lang (language code): ").strip().lower()
    
    if b not in LANGUAGES.values():
        speak("Invalid language code. Please enter a valid code.")
        print("Invalid language code. Please enter a valid code.")
        return
    
    try:
        # Perform the translation
        text_to_translate = translator.translate(query, src="auto", dest=b)
        text = text_to_translate.text
        
        # Convert translated text to speech
        speakgl = gTTS(text=text, lang=b, slow=False)
        speakgl.save("voice.mp3")
        
        # Uncomment to play the sound
        # playsound("voice.mp3")
        
        time.sleep(5)  # Allow time for playback
        os.remove("voice.mp3")  # Remove the file after playback
        
    except Exception as e:
        print(f"Unable to translate: {e}")
        speak(f"Unable to translate: {e}")

# Example usage
if __name__ == "__main__":
    command = takeCommand()
    if command != "None":
        translategl(command)
