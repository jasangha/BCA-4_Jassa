import speech_recognition
import GenericAssistant  # neuralintents
import pyttsx3
import webbrowser
import wikipedia
import pyjokes
from urllib.request import urlopen
import random
import os


recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def listen0():
    global recognizer
    try:
        with speech_recognition.Microphone() as mic:
            winsound.Beep(440, 500)
            print("Listening.......")

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)

            audio = recognizer.listen(mic)
            query = recognizer.recognize_google(audio)
            query = query.lower()

            print("\aRecognizing......")

    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
    print(query)
    return query


def listen1():
    clip = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        winsound.Beep(440, 500)
        clip.pause_threshold = 1
        audio = clip.listen(source)

    try:
        print('\a')
        print("Recognizing...")
        query = clip.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Didn't Understand Bro,Dobara Bolio...")
        return "None"
    return query.lower()


def music():
    music_dir = 'E:\Music\[Punjabi Songs]'
    songs = os.listdir(music_dir)
    m = random.randrange(400)
    for i in range(m):
        os.startfile(os.path.join(music_dir, songs[i]))


def google():
    speak("opening google bro")
    webbrowser.open("google.com")


def youtube():
    speak("here you go to youtube bro")
    webbrowser.open("youtube.com")


def github():
    speak("opening github")
    webbrowser.open("github.com")


def website(url):
    speak("opening", str(url))
    webbrowser.open(url)


def greet():
    speak("i am good bro, tell me how are you?")


def joke():
    speak(pyjokes.get_joke())


def exit():
    speak("exciting our conversation bro")
    exit()


mappings = {
    "music": music,
    "google": google,
    "youtube": youtube,
    "github": github,
    "greet": greet,
    "joke": joke,
    "website": website
}

assistant = GenericAssistant('intents1.json')  # model_name = "test_model")
assistant.train_model()
# assistant.save_model()

if __name__ == "__main__":

    speak('Ready to search Bro')
    # engine.say("kidha meri jaan")  # :)

    query = listen0()
    assistant.request(query)
    # if query == 'play music' or query == 'music' or query == 'songs' or query == 'play songs':
    #     music()
