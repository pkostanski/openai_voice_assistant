import openai
import speech_recognition as sr

openai.api_key = "your_openai_api_key_here"


def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            print("Recording finished")
        except sr.WaitTimeoutError:
            print("Wait timeout exceeded")
            return None

    return audio


def transcribe_audio(audio):
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio, language='pl-PL')
        return text
    except Exception as e:
        print("Transcription error:", e)
        return None


def query_gpt(text):
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": text}]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=260,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].message['content'].strip()


def main():
    audio = record_audio()
    text = transcribe_audio(audio)
    print("Transcription text:", text)

    if text:
        gpt_response = query_gpt(text)
        print("GPT response:", gpt_response)


if __name__ == "__main__":
    main()
