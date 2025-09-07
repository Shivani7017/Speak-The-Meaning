import pyttsx3
from PyDictionary import PyDictionary

class Speaking:
    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

class GFG:
    def Dictionary(self):
        speak = Speaking()
        dic = PyDictionary()
        speak.speak("Which word do you want to find the meaning of, sir?")
        
        query = input("Enter the word: ")
        word = dic.meaning(query)
        
        if word is None:
            print("Sorry, the meaning was not found.")
            speak.speak("Sorry, the meaning was not found.")
            return
        
        print(f"Found {len(word)} meanings for '{query}':")
        
        for meaning_type in word:
            print(f"{meaning_type}: {word[meaning_type]}")
            speak.speak(f"The meaning in {meaning_type} is {', '.join(word[meaning_type])}")

if __name__ == '__main__':
    gfg = GFG()
    gfg.Dictionary()
