import os
from moviepy.editor import VideoFileClip
import speech_recognition as sr
import googletrans

def extract_audio(video_path, output_audio_path="temp_audio.wav"):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)
    print(f"Audio extracted to {output_audio_path}")
    return output_audio_path

def generate_captions(audio_path, language="en"):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        print("Processing audio for transcription...")
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language=language)
        print("Transcription complete.")
        return text
    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Error with the speech recognition service: {e}")
    return ""

video_path = r"C:\Users\amrit\Desktop\for_selenium\test videos and images\jord.mp4"
audio_path = extract_audio(video_path)
captions = generate_captions(audio_path)

print("Generated Captions:\n", captions)
