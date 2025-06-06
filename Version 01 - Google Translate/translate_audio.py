from pydub import AudioSegment
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os

def translate_audio(audio_path, target_lang):
    """
    Translates speech from an audio file into a target language and saves the translated audio.
    
    Parameters:
    - audio_path (str): Path to the input MP3 audio file.
    - target_lang (str): Target language code for translation (e.g., 'si' for Sinhala).
    """
    # Convert MP3 to WAV for speech recognition
    sound = AudioSegment.from_mp3(audio_path)
    wav_path = "converted.wav"
    sound.export(wav_path, format="wav")

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_path) as source:
        audio = recognizer.record(source)

    try:
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        print(f'Original Text: {text}')

        # Translate the text
        translator = Translator()
        text_translate = translator.translate(text, dest=target_lang)
        print(f'Translated Text: {text_translate.text}')

        # Convert translated text to speech
        tts = gTTS(text_translate.text, lang=target_lang)
        tts.save("Translated.mp3")

        print("Audio Translated and saved as Translated.mp3")

    except Exception as e:
        print("Error Occurred:", e)

    finally:
        # Clean up temporary wav file
        if os.path.exists(wav_path):
            os.remove(wav_path)


if __name__ == "__main__":
    # Example usage: translate sample1.mp3 to Sinhala ('si')
    translate_audio("sample1.mp3", "si")
