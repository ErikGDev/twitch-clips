"""
These functions are to be used only in main.py
"""
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, TextClip
from api import *
import json

def create_file(today):
    with open('video_data.json') as json_file:
        data = json.load(json_file)
    list_of_clips = []
    clip_file = open("video_names.txt")
    lines = clip_file.readlines()

    for i, line in enumerate(lines):
        clip = data["clips"][i]
        video = VideoFileClip(line.strip(), target_resolution=(None, 720))
        title = TextClip(txt=clip["broadcaster"]["display_name"] + ": " + clip["title"], font='Amiri-regular', color='white', fontsize=50).set_duration(5)
        title_pos = title.set_pos((0.05, 0.8), relative=True)
        resize = CompositeVideoClip([video, title_pos])
        list_of_clips.append(resize)

    filename = "top_fortnite_clips_" + str(today) + ".mp4"

    final_clip = concatenate_videoclips(list_of_clips, method='compose')
    final_clip.write_videofile(filename)

    return filename


