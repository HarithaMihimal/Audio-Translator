# Audio Translator

A simple Python script to translate speech from an audio file into another language and save the translated speech as audio.

## Features

- Converts MP3 audio to WAV for processing
- Uses Google's Speech Recognition to extract text from audio
- Translates extracted text into the target language using Google Translate API
- Converts translated text back to speech and saves as an MP3 file

## Requirements

- Python 3.6+
- `pydub`
- `speechrecognition`
- `googletrans==4.0.0rc1` (latest stable unofficial version)
- `gtts`
- `ffmpeg` installed and accessible in your system PATH (required by pydub)

## Installation

1. Clone the repository or download the `translate_audio.py` file.

2. Install the required Python packages:

```bash
pip install pydub speechrecognition googletrans==4.0.0rc1 gtts
