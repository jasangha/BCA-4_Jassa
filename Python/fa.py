from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3
import sys

recognizer = speech_recognition.Recognizer()

speaker = pyttsx3.init('espeak')
speaker.setProperty('rate', 50)

todo_list = ['Gym Janna', 'Roti Khani']


def some_function():
    print('satshriakaal g ,   Kida Jass ke haal a terraa')


mappings = {'greeting': some_function}


def create_note():
    global recognizer

    speaker.say('what do you want to write onto your note?')
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)

                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say('Choose a Filename!')
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say('File Has Been Created With Name{filename}')
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say('I Did Not Understand You!, Please Try Again!')
            speaker.runAndWait()


def add_todo():
    global recognizer

    speaker.say('What do you wanna add?')
    speaker.runAndWait()

    done = False

    while not done:
        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                item = recognizer.recognize_google(audio)
                item = item.lower()

                todo_list.append(item)
                done = True

                speaker.say('{item} Has Been Added to the todo list!')
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say('I Did Not Understand You!, Please Try Again!')
            speaker.runAndWait()


def show_todos():
    speaker.say('the items on your to do list are the following')
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def hello():
    speaker.say('hello. what can i do for you?')
    speaker.runAndWait()


def quit():
    speaker.say('chl changa,  bye')
    speaker.runAndWait()
    sys.exit(0)


mappings = {
    "greetings": hello,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "exit": quit
}

assistant = GenericAssistant('intents.json')
assistant.train_model()

while True:

    try:
        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            message = recognizer.recognize_google(audio)
            message = message.lower()

        assistant.request(message)
    except speech_recognition.UnknownValueError:
        recognizer = speech_recognition.Recognizer()
