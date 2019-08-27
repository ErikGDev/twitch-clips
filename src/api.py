import requests
import json
import urllib
import ssl
import urllib.request
import sys

def dl_progress(count, block_size, total_size):
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%" % percent)
    sys.stdout.flush()

def dl_mp4(url, file_path, file_name):
    full_path = file_path + file_name + '.mp4'
    print(url, full_path)
    urllib.request.urlretrieve(url, full_path, reporthook=dl_progress)
    return full_path

def request_clips():
    url = "https://api.twitch.tv/kraken/clips/top"
    querystring = {"game":"Fortnite","period":"day","limit":"20","language":"en"}

    headers = {
        'Accept': "application/vnd.twitchtv.v5+json",
        'Client-ID': "hxr54hwv54czdb0ycy1knyo67tquqv",
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
    return data

def get_clip_parameters(clip):
    title = clip["title"]
    title = title.replace(' ', '_')
    thumbnail = clip["thumbnails"]["small"]
    slide_index = thumbnail.index("-preview-")
    download_url = thumbnail[:slide_index] + ".mp4"

    return (title, download_url)

def download_files():
    #Creates certificate for urllib request
    ssl._create_default_https_context = ssl._create_unverified_context
    data = request_clips()
    video_names = open("video_names.txt", "w+")

    for i, clip in enumerate(data["clips"]):
        title, download_url = get_clip_parameters(clip)
        print("Download URL for clip: {} is: {}".format(clip["slug"], download_url))
        full_path = dl_mp4(download_url, 'video_files/', title)

        if (i + 1) % len(data["clips"]) != 0:
            video_names.write(full_path + "\n")
        else:
            video_names.write(full_path)

    video_names.close()

download_files()