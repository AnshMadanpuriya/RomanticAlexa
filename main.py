import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listner=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    command=""
    try:
        with sr.Microphone() as source:
            print("Listnenig...")
            voice=listner.listen(source)
            command=listner.recognize_google(voice)
            command=command.lower().strip()
            if "alexa" in command:
                command=command.replace("alexa","").strip()
                print("User command :",command)

    except Exception as e:
        print("Error:", e)
        pass
    return command

def run_alexa():
    command=take_command()
    print(command)
    if "hi" in command:
        talk("I am Fine What's about you")

    if "play" in command:
        song = command.replace("play","")
        talk("playing"+song)
        pywhatkit.playonyt(song)

    elif "time" in command:
        time=datetime.datetime.now().strftime("%H:%M %p")
        print(time)
        talk("Current time is "+time)

    elif "who is" in command.lower():
        person = command.lower().replace("who is", "").strip()
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif "how are you" in command:
        talk("I am Fine What's about you")

    elif "are you single" in command:
        talk("I am relationship with wifi")

    elif "i am also fine" in command:
        talk("that's fine, How can i help you")

    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "stop answering" in command:
        talk("Okay, stopping now. Goodbye!")
        exit()
    else:
        talk("sorry,Please say the command again")
while True:
    run_alexa()