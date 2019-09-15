import json

class VideoProperties:
    def __init__(self, file):
        self.file = file

    def get_youtube_video_properties(self):
        with open('video_data.json') as json_file:
            data = json.load(json_file)

        self.title = self.get_video_title(data, 0)
        self.description = self.get_video_description(data)
        self.category = 20
        self.keywords = self.get_tags(data)
        self.privacyStatus = "public"

    def get_video_title(self, data, index):
        title = data["clips"][index]["title"].upper()
        title += " - MONKAS DAILY {} HIGHLIGHTS".format(data["clips"][index]["game"].upper())
        if len(title) > 100:
            title = title[:97] + "..."
        return title

    def get_video_description(self, data):
        description = """\n
        PLEASE READ\n\n\n
        MonkaS Highlights is an automated channel that gets and curates the top
        twitch clips of the day. This is so you have a method of catching up 
        with the happenings of your favourite game without needing to spend all
        the extra time looking through the twitch clips database. It's all here!
        None of these clips in the video are of the property of MonkaS Highlights.
        \n\nClip Credits and Timestamps:\n\n"""
        seconds = 0
        minutes = 0
        for clips in data["clips"]:
            description += "Title: {}\n".format(clips["title"])
            description += "Views: {}\n".format(str(clips["views"]))
            description += "Timestamp: {}:{:02d}\n".format(minutes, seconds)
            description += "Channel: {} - {}\n".format(clips["broadcaster"]["display_name"], clips["broadcaster"]["channel_url"])
            description += "Clip link: {}\n\n".format(clips["url"])
            seconds += round(clips["duration"])
            if seconds > 60:
                minutes += seconds // 60
                seconds -= (seconds // 60) * 60

        description += """
        Thanks for watching! If you have any feedback for this bot, please leave
        a comment and I'll try and use the criticism to improve the video!"""
        description.replace('<', ' ')
        description.replace('>', ' ')
        return description

    def get_tags(self, data):
        tags = data["clips"][0]["game"].lower()
        tags += ",monkas,highlights,daily"
        for clips in data["clips"]:
            tags += ",{}".format(clips["broadcaster"]["display_name"].lower())

        return tags
    