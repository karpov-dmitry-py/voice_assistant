import playsound
from gtts import gTTS
import speech_recognition as sr
import os

audio_file_counter = 0

def listen():

    return input('Введите Ваш текст >>>')
    voice_recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Скажите что-то >>> ")
        audio = voice_recognizer.listen(source)

    try:
        voice_text = voice_recognizer.recognize_google(audio, language="ru")
        print(f"Вы сказали: {voice_text}")
        return voice_text
    except sr.UnknownValueError:
        return "Ошибка распознавания аудио"
    except sr.RequestError:
        return "Ошибка соединения"

def say(text):
    global audio_file_counter
    voice = gTTS(text, lang="ru")
    unique_file = f'google_audio_data_{str(audio_file_counter)}.mp3'
    audio_file_counter += 1
    voice.save(unique_file)

    playsound.playsound(unique_file)
    os.remove(unique_file)

    print(f"Ассистент: {text}")

def handle_command(command):

    command = command.lower()

    if command == "привет":
        say("Привет и тебе тоже")
    elif command == "как дела":
        say("Сидим на карантине")
    elif command == "пока":
        stop()
    else:
        say("Не понятно, повторите")

def stop():
    say("Счастливо")
    exit()

def start():
    print("Запуск ассистента...")

    while True:
        command = listen()
        handle_command(command)

def main():

    try:
        start()
    except KeyboardInterrupt:
        stop()

if __name__ == '__main__':
    main()