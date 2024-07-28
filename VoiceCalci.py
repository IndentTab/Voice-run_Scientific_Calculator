import pyttsx3
import speech_recognition as sr
import wolframalpha

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

wolfprimeaplahe_app = <insert your API key>

def audio(audio_text):
    engine.say(audio_text)
    engine.runAndWait()

def welcomeInst():
    print('Welcome to Calculator :)')
    audio('Welcome to Calculator :)')
    print('If you want to calculate something, please say "calculate" followed by your expression')
    audio('If you want to calculate something, please say "calculate" followed by your expression')
    print('For example, "calculate 7 plus 8" or "calculate sin 30 plus cot 20"')
    audio('For example, "calculate 7 plus 8" or "calculate sin 30 plus cot 20')

def _takeCommand():
    with sr.Microphone() as source:
        print("Listening....")
        audio("Listening...")
        listener.adjust_for_ambient_noise(source, duration=1)
        audio_data = listener.listen(source)

    try:
        print("Recognizing...")
        audio("Recognizing...")
        query = listener.recognize_google(audio_data, language='en-In')
        print(query)
        return query

    except Exception as e:
        print("Didn't understand you...\nCan you repeat?...")
        return "NONE"

def _calculate():
    client = wolframalpha.Client(wolfprimeaplahe_app)
    query = _takeCommand().lower()
    
    if 'calculate' in query:
        query = query.replace('calculate', '')
        res = client.query(query)
        try:
            answer = next(res.results).text
            print("The answer is " + answer)
            audio("The answer is %s" % answer)
        except StopIteration:
            print("No valid answer found for the given query.")
            audio("No valid answer found for the given query.")
    else:
        print("No valid calculation request found.")
        audio("No valid calculation request found.")




def confirm_exit():
    while True:
        print("Do you want to exit? Type 'yes' or 'no' and press Enter.")
        user_response = input().lower()
        if 'yes' in user_response:
            print("Goodbye!")
            audio("Goodbye!")
            exit()
        elif 'no' in user_response:
            return
        else:
            print("Sorry, I didn't understand. Please type 'yes' or 'no' and press Enter.")

welcomeInst()

while True:
    _calculate()
    confirm_exit()
