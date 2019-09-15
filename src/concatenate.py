"""
These functions are to be used by main.py
"""
from moviepy.editor import VideoFileClip, concatenate_videoclips, CompositeVideoClip, TextClip
import json
import os


def create_file(today):
    """
    Creates VideoFileClips for each twitch clip, and concatenates them together.
    Returns the file name as a string.
    """
    list_of_clips = []

    with open("video_names.txt") as clip_file:
        read_file = clip_file.read()
        lines = read_file.splitlines()

    clip_file = open("video_names.txt")
    
    for line in lines:
        #Creates video in 720p - keeps original aspect ratio
        video = VideoFileClip(line, target_resolution=(720, None))
        list_of_clips.append(video)

        os.remove(line)

    filename = "top_fortnite_clips_" + str(today) + ".mp4"

    final_clip = concatenate_videoclips(list_of_clips, method='compose')
    final_clip.write_videofile(filename)

    return filename

#Replace create_file with this definition to implement title text clip on
#top of clip. REQUIRES IMAGEMAGICK - https://imagemagick.org/index.php

"""
def create_file(today):
    with open('video_data.json') as json_file:
        data = json.load(json_file)

    list_of_clips = []

    with open("video_names.txt") as clip_file:
        lines = clip_file.readlines()

    clip_file = open("video_names.txt")
    
    for i, line in enumerate(lines):
        
        video = VideoFileClip(line.strip(), target_resolution=(720, None))

        
        clip = data["clips"][i]
        title = TextClip(txt=clip["broadcaster"]["display_name"] + ": " + clip["title"], font='Impact', color='white', fontsize=50).set_duration(5)
        title_pos = title.set_pos((0.05, 0.8), relative=True)
        resize = CompositeVideoClip([video, title_pos])

        list_of_clips.append(video)
        os.remove(line.strip())

    filename = "top_fortnite_clips_" + str(today) + ".mp4"

    final_clip = concatenate_videoclips(list_of_clips, method='compose')
    final_clip.write_videofile(filename)

    return filename
    """