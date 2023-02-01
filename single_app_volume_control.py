# credits: Matias Pedelhez
# 
# This code is used to control the volume 
# of an audio instance using hotkeys.
# In this case scenario, it is adapted
# to the process "Spotify.exe", but you can
# use it with whatever process that creates an audio instance
# in Windows. Tested on Windows 11 and 10 on 2/1/2023.


from pycaw.pycaw import AudioUtilities
import time
import keyboard
import json


with open("./config.json") as config_file:
    configs = json.load(config_file)


class AudioController:
    def __init__(self, process_name):
        self.process_name = process_name
        self.volume = self.process_volume()
        self.exists = self.process_exists()

    def decrease_volume(self, decibels):
        # Decreases volume of process_name audio instance
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                self.volume = max(0.0, self.volume - decibels)
                interface.SetMasterVolume(self.volume, None)
                print("Volume reduced to", self.volume) # debug

    def increase_volume(self, decibels):
        # Increases volume of process_name audio instance
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                self.volume = min(1.0, self.volume + decibels)
                interface.SetMasterVolume(self.volume, None)
                print("Volume raised to", self.volume) # debug

    def process_volume(self):
        # Returns the volume value of process_name audio instance
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            interface = session.SimpleAudioVolume
            if session.Process and session.Process.name() == self.process_name:
                print("Volume:", interface.GetMasterVolume()) # debug
                return interface.GetMasterVolume()

    def process_exists(self):
        # Returns True if process_name does have an audio instance running
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process and session.Process.name() == self.process_name:
                return True
        return False
        

def keyboardListener(audio_controller):
    # Assigning a hotkey to increase_volume and decrease_volume methods
    keyboard.add_hotkey(configs["increase_volume"], lambda: audio_controller.increase_volume(0.05))
    keyboard.add_hotkey(configs["decrease_volume"], lambda: audio_controller.decrease_volume(0.05))
    keyboard.wait()

def loopUntilProcessOpen(process):
    processUnavailable = True

    while True:

        # Waits for audio instance to exist.
        while processUnavailable:
            audio_controller = AudioController(process)
            if(audio_controller.exists): 
                keyboardListener(audio_controller)
                processUnavailable = False
            else:
                del audio_controller

            time.sleep(1)

        # If the audio instance is closed while runtime, resume the above loop.
        if(audio_controller.exists == False):
            processUnavailable = True
            del audio_controller
        
        time.sleep(1)

if __name__ == "__main__":
    loopUntilProcessOpen('Spotify.exe')