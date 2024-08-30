import speech_recognition as sr
import pyttsx3

def listen_and_convert():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the source for input
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        # Listen for 5 seconds and create the ambient noise energy level
        recognizer.adjust_for_ambient_noise(source, duration=5)
        print("Microphone calibrated")
        
        print("Listening...")
        # Capture the audio from the microphone
        audio_data = recognizer.listen(source)
        print("Audio captured, processing...")

        # Recognize the speech in the audio
        try:
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None

def text_to_audio(text):
    if text:
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()
        
        # Speak the text
        engine.say(text)
        engine.runAndWait()
    else:
        print("No text to convert to audio")

# Example usage
text = listen_and_convert()
text_to_audio(text)
