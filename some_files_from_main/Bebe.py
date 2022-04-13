import speech_recognition
import pyttsx3
import colorama
from colorama import Fore, Back, Style

recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 110)
colorama.init(autoreset=True)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greet(audio):
    engine.setProperty('volume', 1)
    engine.setProperty('rate', 250)
    engine.say(audio)
    engine.runAndWait()


def listen():
    global recognizer
    try:
        with speech_recognition.Microphone() as mic:
            print("\a")

            recognizer.adjust_for_ambient_noise(mic, duration=0.5)

            audio = recognizer.listen(mic)
            query = recognizer.recognize_google(audio, language='en-in')
            query = query.lower()
            print('\t\t\t\t\t\t', end="")
            print(f"{Fore.BLUE}{Style.BRIGHT}"+query)

            return query

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
        print(Fore.WHITE+'Exiting')
        speak('exiting')
        exit()


if __name__ == "__main__":
    speak('kidha')
    greet('jhass a')

    while True:
        query = listen()

        if query == 'hello':
            speak("kidha meri jaan")
