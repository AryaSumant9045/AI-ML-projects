import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('nsss')
voices = engine.getProperty('voices')
# print(voices[1].id)

# //assigning voice
engine.setProperty('voice', voices[6].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12:
        speak("good Morning")

    if hour >=12 and hour<=18:
        speak("Good afernoon")

    else:
        speak("good evening")

    speak("Hi , I am jarvis sir, How i may help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say that again please")
        return "None"
    return query

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing task based on query
        