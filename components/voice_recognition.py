import streamlit as st
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    
    # Display a button for recording speech
    st.write("Click below and start speaking:")
    if st.button("Record"):
        with sr.Microphone() as source:
            st.write("Listening...")
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            
            try:
                text = recognizer.recognize_google(audio)
                st.write("You said: ", text)
                return text
            except sr.UnknownValueError:
                st.write("Sorry, I could not understand your speech.")
                return None
            except sr.RequestError:
                st.write("Sorry, there was an issue with the speech recognition service.")
                return None
