from moviepy.editor import VideoFileClip, concatenate_videoclips
from api import *
from datetime import date
from concatenate import *
from video_properties import VideoProperties
from youtube import *
import os



if __name__ == "__main__":

    today = date.today()

    download_files()

    filename = create_file(today)
    args = VideoProperties(filename)
    args.get_youtube_video_properties()

    #upload_video_to_youtube(args)

    os.remove(filename)