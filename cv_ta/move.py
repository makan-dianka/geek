import os
import shutil
import moviepy.editor as mp
import time

path = [r"C:\YoutubeVideosDownloader", r"C:\tutto\yd"]

def move_file(src):
    path = os.listdir(src)
    for sv in path:
        if sv.endswith('.mp4'):
            shutil.move(f"{src}\{sv}", r"C:\Users\pavilion-250\Videos\{}".format(sv))
            print(f"\nle fichier -> {sv} est deplacé :)")
            
for root in path:            
    move_file(root)