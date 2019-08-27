#from api import *
from moviepy.editor import VideoFileClip, concatenate_videoclips

#download_files()

video_names = open("video_names.txt", "w+")

for i in range(len([1, 2, 3, 4, 5, 5])):
    if (i + 1) % len([1, 2, 3, 4, 5, 5]) != 0:
        video_names.write("Hello" + "\n")
    else:
        video_names.write("Hello")

video_names.close()


