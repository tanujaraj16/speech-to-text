import argparse
import speech_recognition as sr
import sys

def transcribe_file(path):
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)   # Uses Google Web Speech API
        return text
    except sr.UnknownValueError:
        return "[Could not understand audio]"
    except sr.RequestError as e:
        return f"[API request failed: {e}]"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", help="WAV file to transcribe", required=True)
    args = parser.parse_args()

    print("Transcribing file:", args.file)
    print("\n--- Transcription ---\n")
    print(transcribe_file(args.file))
