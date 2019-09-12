"""
These functions are to be used only in main.py
"""
from moviepy.editor import VideoFileClip, concatenate_videoclips
from api import *

def create_file(today):
    list_of_clips = []
    clip_file = open("video_names.txt")
    lines = clip_file.readlines()

    for line in lines:
        list_of_clips.append(VideoFileClip(line.strip()))

    final_clip = concatenate_videoclips(list_of_clips, method='compose')
    final_clip.write_videofile("top_fortnite_clips_" + str(today) + ".mp4")


