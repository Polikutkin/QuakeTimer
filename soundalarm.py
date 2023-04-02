import os
from gtts import gTTS
from playsound import playsound
from threading import Thread

sound_folder = 'sounds'
sound_files = {
    'mega': 'sounds\\mega_alarm.mp3',
    'heavy': 'sounds\\heavy_alarm.mp3',
}


def init(seconds):
    if not os.path.exists(sound_folder):
        os.makedirs(sound_folder)

    for name, path in sound_files.items():
        message = name + ' in ' + str(seconds)
        tts = gTTS(message)
        tts.save(path)


def play_sound(name):
    sound = sound_files.get(name)
    if sound and os.path.exists(sound):
        Thread(target=playsound, args=(sound,), daemon=True).start()


def destroy():
    for name, path in sound_files.items():
        os.remove(path)
