# Autor : MAKAN LEBOSS
# Email : makan.dianka@hotmail.com
# This script convert the text to audio file.mp3. It required the module gtts

from gtts import gTTS 
import os 

def text_to_audio(path, text):
    objet = gTTS(text=text, lang='fr', slow=False)
    objet.save(r"{}".format(path))
    print("\nAudio Saved in this path: {}".format(path))

print("\nEnter the full path to save your audio file. (ex: c:\path\audio.mp3)")

with open('c:/tutto/q_charlotte.txt', 'r') as q:
    read_line = q.read()
    path = input("Audio's path : ")
    text = read_line               #input("Enter your text : ")
    text_to_audio(path, text)