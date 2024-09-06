import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import webbrowser


listener = sr.Recognizer()
engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

engine.say('hey boss')
engine.runAndWait()




def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command =command.lower()  
            print(command)
            return command
    
    except Exception as e:
        print(e)
        return None
def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def serve():
    command=take_command()
    if command:
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time=datetime.datetime.now().strftime('%I:%M %p')
            talk("it's " + time)
        elif 'google' in command:
            command=command.replace('google','')
            talk('googling '+ command)
            google_search_url = f'https://www.google.com/search?q={command}'
            webbrowser.open_new_tab(google_search_url)
            info=wikipedia.summary(command,78)
            talk(info)
        else:
            info=wikipedia.summary(command,30)
            talk(info)
        
    else:
        talk("please say the command again")

serve()