import random
import pyttsx3
import speech_recognition as sr
import webbrowser
import time
import pywhatkit

re = ['Hi', 'hello', 'hi friday', 'hello friday']
sp = ['hi ', 'hello']
x = random.choice(sp)
tt = 'is there any other work mam'





engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak('Hi this is friday, your personal assistant')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('recognisation.....')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')
    except Exception as e:
        print('Sorry say again....')
        speak('sorry say again')
        return 'none'
    return query






def que():
    while True:
        query = takeCommand().lower()

        if query in re:
            speak(x)
            print(x)

        elif 'open youtube' in query:
            speak('here is your youtube')
            webbrowser.open('https://www.youtube.com/')
            time.sleep(20)
            speak(tt)
            sd = takeCommand().lower()
            if 'yes' in sd:
                speak('what should i do')
            elif 'no' in sd:
                speak('can i exit')
                bp = takeCommand().lower()
                if 'yes' in bp:
                    break;
                elif 'no' in bp:
                    speak('ok what should i do')
                    return que()



        elif 'open gmail' in query:
            speak('opening Gmail')
            webbrowser.open('https://www.gmail.com/')
            time.sleep(20)
            speak(tt)
            sd = takeCommand().lower()
            if 'yes' in sd:
                speak('what should i do')
            elif 'no' in sd:
                speak('can i exit')
                bp = takeCommand().lower()
                if 'yes' in bp:
                    break;
                elif 'no' in bp:
                    speak('ok what should i do')
                    return que()


        elif "friday search" in query:
            speak('what should I search')
            st = takeCommand().lower()
            webbrowser.open(st)
            time.sleep(20)
            speak(tt)
            sd = takeCommand().lower()
            if 'yes' in sd:
                speak('what should i do')
            elif 'no' in sd:
                speak('can i exit')
                bp = takeCommand().lower()
                if 'yes' in bp:
                    break;
                elif 'no' in bp:
                    speak('ok what should i do')
                    return que()


        elif "thanks friday" in query:
            speak('your welcome')
            speak('Is there any other work mam')
            g = takeCommand().lower()
            if 'no' in g:
                break;
            elif 'yes' in g:
                speak('What should I do')
            return que()
        if 'exit' in query:
            speak('are you sure you want to exit')
            y = takeCommand().lower()
            if 'yes' in y:
                break;
            elif 'no' in y:
                return que()




if __name__ == '__main__':
    que()
