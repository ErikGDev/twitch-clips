from moviepy.editor import VideoFileClip, concatenate_videoclips
from api import *
from datetime import date
from concatenate import *
from video_properties import VideoProperties
from youtube import *


if __name__ == "__main__":

    today = date.today()
    download_files()
    create_file(today)
    args = VideoProperties(
        "top_fortnite_clips_2019-09-13.mp4",
        "56 dmg pickaxe gg's only",
        "Test123 123",
        20,
        "hello,world,yeet",
        "private"
    )

    upload_video_to_youtube(args)
