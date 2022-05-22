import speech_recognition
import pyttsx3
import webbrowser
import wikipedia
import pyjokes
import os
import ctypes
import datetime
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


def music():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'Shuffling Your Playlist')
    speak('shuffling playlist')
    music_dir = 'C:\\Users\\win7\\Music\\My_Music'
    songs = os.listdir(music_dir)
    totalfiles = 0
    for base, dirs, files in os.walk(music_dir):
        for Files in files:
            totalfiles += 1

    for i in range(totalfiles):
        os.startfile(os.path.join(music_dir, songs[i]))


def music1():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'Shuffling Your Playlist')
    speak('shuffling playlist')
    codePath = "C:\\Users\\win7\\Music\\My_Music\\Playlist.xspf"
    os.startfile(codePath)


def google():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+"opening google bro")
    speak("opening google bro")
    webbrowser.open("google.com")


def youtube():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+"Opening youtube bro")
    speak("opening youtube bro")
    webbrowser.open("youtube.com")


def github():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'opening github')
    speak("opening github brother")
    webbrowser.open("github.com")


def greet():
    print(f"{Fore.YELLOW}{Style.BRIGHT}" +
          "I Am Good Bro, What Can I Do For You")
    speak("i am good bro, waht can i do for you")


def joke():
    x = pyjokes.get_joke()
    print(f"{Fore.YELLOW}{Style.BRIGHT}" + x)
    speak(x)


def quit():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+"Exiting Brother")
    speak("exiting brother")
    exit()


def code():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'Opening Code Bro')
    speak('opening code bro')
    codePath = "C:\Program Files\Microsoft VS Code\Code.exe"
    os.startfile(codePath)


def search(query):
    query = query.replace("search", "")
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+"Searching {}".format(query))
    webbrowser.open_new_tab(
        "https://www.google.com.tr/search?q={}".format(query))


def time():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+f"Bro, the time is {strTime}")
    speak(f"Bro, the time is {strTime}")


def downloads():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'Opening Downloads Directory')
    speak('Opening Downloads Directory')
    down_dir = 'C:\\Users\\win7\\Downloads'
    downloads = os.listdir(down_dir)
    os.startfile(os.path.join(down_dir))


def location(query):
    query = query.replace("where is", "")
    query = query.replace("locate", "")
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+"Locating", end="")
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+query)

    speak("locating")
    speak(query)
    webbrowser.open(
        "https://www.google.nl/maps/place/" + query + "")


def pause(query):
    import time
    speak('waiting 10 sec')
    time.sleep(10)
    return None


def createnote():
    speak("What should i write, bro")
    note = listen()
    file = open('jassa.txt', 'w')
    # with open("jassa1.txt") as file:
    speak("Bro, Should i include date and time")
    snfm = listen()
    if 'han' in snfm or 'yes' in snfm or 'sure' in snfm:
        strTime = datetime.datetime.now().strftime("% H:% M:% S")
        file.write(strTime)
        file.write(" :- ")
        file.write(note)
    else:
        file.write(note)
    speak('done bro')


def shownote():
    speak("Showing Notes")
    file = open("jassa.txt", "r")
    content = file.read()
    print("Note: ", content)
    speak(content)


def chrome():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'Opening Chrome Bro')
    speak('opening chrome')
    Path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    os.startfile(Path)


def excel():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'Opening Excel')
    speak('opening excel')
    Path = "C:\\Program Files (x86)\\Microsoft Office\\Office14\\EXCEL.exe"
    os.startfile(Path)


def powerpoint():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'Opening Powerpoint')
    speak('opening powerpoint')
    Path = "C:\\Program Files (x86)\\Microsoft Office\\Office14\\POWERPNT.exe"
    os.startfile(Path)


def word():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'Opening Word')
    speak('opening word')
    Path = "C:\\Program Files (x86)\\Microsoft Office\\Office14\\WINWORD.exe"
    os.startfile(Path)


def oracle():
    print(f"{Fore.YELLOW}{Style.BRIGHT}"+'Opening Oracle')
    speak('opening oracle database')
    Path = "C:\\oraclexe\\app\\oracle\\product\\10.2.0\\server\\BIN\\"
    os.startfile(Path)


def subs():
    print(f"{Fore.RED}{Style.BRIGHT}COMMANDS : ")
    print(f"{Fore.WHITE}{Style.BRIGHT}--------------------------------------------------------------------------------")
    print(f"{Fore.GREEN}{Style.BRIGHT}* Open Google                           * Open Youtube\n* Open Github                           * Open Wikipedia\n* Open Code                             * Play Music\n* How Are You                           * Tell Me A Joke\n* Exit                                  * What Is The Time\n* I Don't Want To Talk To You           * Hey Bro, What Is Your Name\n* Open Downloads                        * Search\n* Lock The System                       * Shut The System\n* Where Is                              * Restart\n* Hibernate                             * Search On Wikipedia")
    print(f"{Fore.GREEN}{Style.BRIGHT}* I Love You                            * Who Am I\n* Write Note                            * Show Note\n* Where Is                              * Open Google\n* Open Word                             * Open Powerpoint\n* Open Excel                            * Open SQL Command Line\n* Wait Kar 2 Minute                     * Pause")
    print(f"{Fore.CYAN}{Style.BRIGHT}________________________________________________________________________________")
    print(f"{Fore.MAGENTA}{Style.BRIGHT}________________________________________________________________________________\n")


if __name__ == "__main__":
    os.system('cls')

    subs()

    speak('hello Berojgaar')
    # speak("kidha meri jaan")  # :)
    while True:
        query = listen()

        if query == 'play music' or query == 'music' or query == 'songs' or query == 'play songs':
            music()
        elif query == 'open google' or query == 'open google.com':
            google()
        elif query == 'open youtube' or query == 'open youtube.com':
            youtube()
        elif query == 'open github' or query == 'open github.com':
            github()
        elif query == 'how are you' or query == 'how are you peter' or query == 'kida' or query == 'kida peter':
            greet()
        elif query == 'tell me a joke' or query == 'joke' or query == 'make me laugh':
            joke()
        elif query == 'none' or query == 'exiting' or query == "exit the loop" or query == 'exit this loop' or query == 'exit' or query == 'quit this loop' or query == 'quit the loop' or query == 'quit' or query == 'shutup':
            quit()
        elif query == 'open code' or query == 'open vs code' or query == 'open visual studio' or query == 'open visual studio code':
            code()
        elif query == "what's the time" or query == "what is the time" or query == 'time':
            time()
        elif query == 'i want to exit' or query == 'i do not want to talk with you' or query == "i don't want to talk to you" or query == 'shut up bro' or query == 'shut up' or query == 'chup kar ja yar' or query == 'chup kar ja bro':
            import time

            print(f"{Fore.YELLOW}{Style.BRIGHT}" +
                  'Okay Okay, Do not cry like a baby i am going away')
            speak('Okay Okay  Do not cry like a baby i am going away')
            time.sleep(1)
            print(f"{Fore.YELLOW}{Style.BRIGHT}"+'bye bro')
            speak('bye bro')
            exit()
        elif query == 'what is your name' or query == 'what is your name bro' or query == 'hey bro what is your name' or query == 'hi bro what is your name' or query == 'hello bro what is your name' or query == 'hello what is your name':
            print(f"{Fore.YELLOW}{Style.BRIGHT}" +
                  'My Name Is Peterprakash AKA Peter')
            speak('my name is peterprakash aka peter')
        elif query == 'open downloads' or query == 'open download':
            downloads()
        elif 'search' in query or 'play' in query:
            search(query)
        elif 'lock the system' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query or 'shut the system' in query or 'shut the system down' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')
        elif 'wait' in query or 'pause' in query or 'wait kar' in query or 'wait kar do minute' in query:
            pause(query)
        elif "where is" in query or "locate" in query:
            location(query)
        elif "restart" in query or "restart system" in query or "restart the system" in query:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query or "sleep" in query or 'hibernate the system' in query or 'go to sleep' in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
        elif "i love you" in query:
            print(f"{Fore.YELLOW}{Style.BRIGHT}"+"Hahahahahahahahaha")
            speak("fuck you motherfucker")
        elif "who i am" in query or "who am i" in query:
            speak("you are a dumb ass")
        elif "write note" in query or "create note" in query or "write a note" in query or 'create a note' in query:
            createnote()
        elif 'search on wikipedia' in query or 'search wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("search on wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "show note" in query or 'show my note' in query or 'open note' in query or 'open my note' in query:
            shownote()
        elif query == 'open word' or query == 'open microsoft word':
            word()
        elif query == 'open powerpoint' or query == 'open microsoft powerpoint':
            powerpoint()
        elif query == 'open excel' or query == 'open microsoft excel':
            excel()
        elif query == 'open chrome' or query == 'open google':
            chrome()
        elif query == 'open oracle' or query == 'open oracle database' or query == 'open sql command line' or query == 'start sql command line':
            oracle()
        else:
            search(query)
