import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import speech_recognition as sr

def record_audio(filename="sample.wav", duration=5, fs=16000):
    print(f"Recording {duration} seconds of audio... Speak now!")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    
    # Convert float32 array to int16 for proper WAV format
    recording_int16 = np.int16(recording * 32767)
    write(filename, fs, recording_int16)
    
    print(f"Recording saved as {filename}")
    return filename

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "[Could not understand audio]"
    except sr.RequestError as e:
        return f"[API request failed: {e}]"

if __name__ == "__main__":
    filename = record_audio(duration=5)
    print("\nTranscribing audio...\n")
    transcription = transcribe_audio(filename)
    print("--- Transcription ---")
    print(transcription)
