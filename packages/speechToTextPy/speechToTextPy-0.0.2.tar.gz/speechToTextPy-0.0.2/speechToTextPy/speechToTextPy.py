from  googletrans import Translator 
import speech_recognition as sr

def listen(language: str = None):
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold=1
        audio=r.listen(source,0,8) #Listening Mode.......
    try:
        print("Recongnizing......")
        query=r.recognize_google(audio,language=language)
    except:
        return ""
    query=str(query).lower()
    
    return query



def TranslationHinEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You: {data}")

    return data

#tyime to exicution
def MiceExicution():
    query=listen()
    data=TranslationHinEng(query)
    return data


