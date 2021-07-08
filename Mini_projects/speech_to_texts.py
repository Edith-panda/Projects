import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as sorce:
    print("SPEAK.....")
    audio = r.listen(source)
    print(r.recognize_google(audio))
    