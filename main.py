import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import sys

voice_recognize = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


talk("Hello Human... please identify yourself : ")
name = input("ID ? ")

for n in name:
    if "oracle" in name:
        talk(f"Welcome back {name}...it's good to see you again")
        print(f"Welcome back {name}...it's good to see you again")
        break
    else:
        talk("Please enter the authentication key")
        auth_key = input(print("Please enter the authentication key"))
        if ("pie" in auth_key) or ("sugar" in auth_key):
            talk("Authentication Successful....you can continue now")
            print("Authentication Successful...you can continue now")
            break
        else:
            talk("Authentication failed...wrong key")
            talk("Run the program again to retry")
            print("Authentication failed...wrong key")
            print("Run the program again to retry")
            exit()


def take_command():
    try:
        with sr.Microphone() as source:
            talk('..listening')
            print('Listening...')
            voice = voice_recognize.listen(source)
            command = voice_recognize.recognize(voice)
            command = command.lower()
            return command
    except:
        print(f"Sorry {name} could not process the audio...please run the program again")
        talk(f"Sorry {name} could not process the audio...please run the program again")
        return command


def run_jarvis():
    command = take_command()
    print(command)

    if command is None:
        print("No Command")

    elif 'play' in command:
        talk(f"Please wait a moment {name}")
        print("playing...")
        pywhatkit.playonyt(command)

    elif 'how are you' in command:
        talk(f"I am fine {name}...how are you?")
        print(f"I am fine {name}...how are you?")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M:%S %p')
        talk(f"Current time is {time}")
        print(f"Current time => {time}")

    elif 'wikipedia' in command:
        info = wikipedia.summary(command, 2)
        print(info)
        talk(info)

    elif'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    elif 'password' in command:
        import PassGen
        print(PassGen.final_password)

    elif 'spotify' in command:
        import os
        talk("Opening Spotify")
        os.system("Spotify Free")

    elif 'notepad' in command:
        import os
        talk("Opening Notepad")
        os.system("Notepad")

    elif ('chrome' in command) or ('google' in command):
        from colorama import Fore, Style
        print(Fore.BLUE + "Please specify the website name...")
        print()

        talk("Please specify the website name...")
        print(Style.RESET_ALL)
        web_page = input(talk(f"{name} what site do you want to navigate to?"))
        url = web_page
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)

    elif ("my" in command) or ("class" in command):
        print("Opening my class")
        talk("Opening my class")
        url = 'https://myclass.lpu.in/'
        webbrowser.register('chrome',
                            None,
                            webbrowser.BackgroundBrowser(
                                "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
        webbrowser.get('chrome').open(url)

    else:
        print("Please repeat your command again")
        talk("Please repeat your command again")


while True:
    talk("Please press <y> to continue...or <n> to terminate the program: ")
    answer = input('Please press <y> to continue...or <n> to terminate the program: ')
    if answer.lower().startswith("y"):
        talk("A moment please")
        run_jarvis()
    elif answer.lower().startswith("n"):
        talk(f"Bye {name} have a good day!!!")
        print(f"Bye {name} have a good day!!!")
        exit()
