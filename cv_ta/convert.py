import os
import shutil
import moviepy.editor as mp
import time

path = [r"C:\YoutubeVideosDownloader", r"C:\tutto\yd"]

def  video_to_audio(src):
    global root
    path = os.listdir(src)
    for mp4 in path:
        if mp4.endswith('.mp4'):
            nom = mp4.split('.')
            video = mp.VideoFileClip(r"{}\{}".format(root,mp4))
            video.audio.write_audiofile(r"C:\Users\pavilion-250\Music\{}.mp3".format(nom[0]))
            print(f"\nla vidéo -> {mp4} est convertise avec succé :) ")

for root in path:
    video_to_audio(root)
