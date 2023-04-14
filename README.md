# Voice Assistant with OpenAI GPT-3.5 Turbo and Google Speech Recognition

This is a simple voice assistant application that uses OpenAI GPT-3.5 Turbo for generating responses and Google Speech Recognition for converting speech to text. The application listens to the user's voice input, transcribes it to text, and sends the text to GPT-3.5 Turbo. The AI model then generates a response, which is printed in the console.

## Requirements

- Python 3.6 or newer
- openai
- SpeechRecognition

## Installation

1. Clone the repository:

```bash
git clone https://github.com/pkostanski/openai_voice_assistant.git
```

2. Navigate to the project directory:

```bash
cd openai_voice_assistant
```

3. Install the required libraries using the requirements.txt file:
    
```bash
pip install -r requirements.txt
```

4. Replace the openai.api_key value in the script with your own OpenAI API key.


## Usage

Run the main() function in the script to start the voice assistant:

```bash
python voice_assistant.py
```

The application will prompt you to speak. After you finish speaking, it will transcribe your speech and send the text to GPT-3.5 Turbo for processing. The AI-generated response will be displayed in the console.

## Important notes

- The application uses the default OpenAI GPT-3.5 Turbo model. You can change the model by replacing the model value in the script with the name of the model you want to use.
- The application uses the default OpenAI GPT-3.5 Turbo completion parameters. You can change the parameters by replacing the parameters value in the script with the parameters you want to use.
- This application uses the Google Speech Recognition API for speech-to-text conversion. The audio is sent to Google's servers for processing. Make sure to comply with the API's terms of use and privacy policy.
- The OpenAI API key is sensitive information. Be careful not to share it or expose it in publicly accessible repositories.
