import sounddevice as sd
import numpy as np
import streamlit as st
import speech_recognition as sr
import wikipedia
import wavio  # To save recorded audio for processing

# Function to record audio using sounddevice
def record_audio(duration=5, sample_rate=44100, channels=1):
    st.write(f"Recording for {duration} seconds...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype="int16")
    sd.wait()  # Wait for the recording to finish
    return audio_data, sample_rate

# Function to save recorded audio as a WAV file
def save_audio(filename, audio_data, sample_rate):
    wavio.write(filename, audio_data, sample_rate, sampwidth=2)  # Save as a 16-bit WAV file

# Main function for Streamlit app
def main():
    st.title("Voice Search Wikipedia")
    st.write("Click the button below to start voice search.")

    if st.button("Start Voice Search"):
        # Step 1: Record audio
        duration = 5  # Adjust duration as needed
        audio_data, sample_rate = record_audio(duration=duration)
        temp_audio_file = "temp_audio.wav"
        save_audio(temp_audio_file, audio_data, sample_rate)

        # Step 2: Transcribe audio using SpeechRecognition
        recognizer = sr.Recognizer()
        with sr.AudioFile(temp_audio_file) as source:
            st.write("Processing the audio...")
            audio = recognizer.record(source)

        try:
            # Convert speech to text
            query = recognizer.recognize_google(audio)
            st.write(f"Recognized Query: **{query}**")

            # Step 3: Search Wikipedia
            st.write("Searching Wikipedia...")
            summary = wikipedia.summary(query, sentences=3)
            st.success(summary)

        except sr.UnknownValueError:
            st.error("Could not understand the audio. Please try again.")
        except sr.RequestError:
            st.error("Speech recognition service is unavailable.")
        except wikipedia.DisambiguationError as e:
            st.error(f"Your query is ambiguous. Suggestions: {e.options}")
        except wikipedia.PageError:
            st.error("No Wikipedia page found for your query.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
