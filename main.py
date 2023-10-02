#from playsound import playsound
#import keyboard  
#while True:  
#        if keyboard.read_key() == "enter":
#            playsound("bell.wav")
#        else:
#            print(keyboard.read_key())
#            playsound("keystroke1.wav")
#
import threading
from playsound import playsound
from pynput import keyboard

def on_press(key):
    print(key)
    if key == keyboard.Key.enter:
        threading.Thread(target=playsound, args=('bell.wav',), daemon=True).start()
        threading.Thread(target=playsound, args=('carriage-return.wav',), daemon=True).start()
    else:
        threading.Thread(target=playsound, args=('keystroke3.wav',), daemon=True).start()
    #playsound("keystroke1.wav")

listener = keyboard.Listener(on_press=on_press)
listener.start()

while True:
    continue

