"""
These functions are to be used by main.py
"""
import requests
import json
import urllib
import ssl
import urllib.request
import sys
import os


def request_clips(client_id):
    """
    Using the client_id from client_id.txt, send a GET request to twitch.tv using the API. This
    creates a json file with all clip data, and then returns the json contents
    """
    #Change these values to alter what clips you want to download
    #DEFAULT: Top 15 Fortnite clips from the last day, langauge is English
    LIMIT = 3
    GAME = "Fortnite"
    PERIOD = "day"
    LANGUAGE = "en"

    url = "https://api.twitch.tv/kraken/clips/top"
    querystring = {"game":GAME,"period":PERIOD,"limit":LIMIT,"language":LANGUAGE}

    headers = {
        'Accept': "application/vnd.twitchtv.v5+json",
        'Client-ID': client_id,
        'User-Agent': "PostmanRuntime/7.15.2",
        'Cache-Control': "no-cache",
        'Postman-Token': "f6d559cc-ab05-41b3-bd3e-9a1b7085d71f,f6a304f1-4a9b-4f5b-a5b8-43036157f866",
        'Host': "api.twitch.tv",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    with open('video_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return data


def get_clip_parameters(clip):
    """
    Using a clip object as the argument, this function returns the 'slug' (AKA a unique identifier),
    and the download url for the clip.
    """
    #'slug' is a naming mechanism used by Twitch. Each slug is unique.
    slug = clip["slug"]
    slug = slug.replace(' ', '_')
    thumbnail = clip["thumbnails"]["small"]
    slide_index = thumbnail.index("-preview-")
    download_url = thumbnail[:slide_index] + ".mp4"

    return (slug, download_url)


def dl_progress(count, block_size, total_size):
    """
    Event handler which shows the percentage downloaded for each twitch clip
    """
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()


def dl_mp4(url, file_path, file_name):
    """
    Takes in the url, file path, and file_name as arguments. Each clip (as mp4 files) is then
    downloaded from the URL, and the full_path is returned
    """
    full_path = file_path + file_name + '.mp4'

    if not os.path.exists(file_path):
        os.makedirs(file_path)

    try: 
        urllib.request.urlretrieve(url, full_path, reporthook=dl_progress)
        return full_path
    
    except:
        print("There was an error downloading the file at: {}".format(url))
        return None


def get_client_id():
    """
    Returns client_id from 'client_id.txt'
    """
    with open("client_id.txt") as infile:
        return infile.read().strip()


def download_files():
    """
    Downloads files and writes down the names of each file into video_names.txt for future
    concatenation
    """
    #Creates certificate for urllib request
    ssl._create_default_https_context = ssl._create_unverified_context

    client_id = get_client_id()
    data = request_clips(client_id)
    
    #File consisting of the names of each clip for concatenation
    video_names = open("video_names.txt", "w+")

    for i, clip in enumerate(data["clips"]):
        title, download_url = get_clip_parameters(clip)
        print("\n\nDownloading clip: {}\nFrom: {}".format(clip["slug"] + '.mp4', download_url))
        full_path = dl_mp4(download_url, 'video_files/', title)

        if (i + 1) % len(data["clips"]) != 0:
            video_names.write(full_path + "\n")
        else:
            video_names.write(full_path)

    video_names.close()
