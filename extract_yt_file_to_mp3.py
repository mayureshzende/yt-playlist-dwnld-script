# require dependancies to install 
import os
from pytube import Playlist, YouTube
from moviepy.editor import *
import re



def download_playlist(playlist_url, resolution):
    playlist = Playlist(playlist_url)
    playlist_name = re.sub(r'\W+', '-', playlist.title)

    if not os.path.exists(playlist_name):
        os.mkdir(playlist_name)

    for index, v in enumerate(playlist.videos, start=1):
        video = YouTube(v.watch_url, use_oauth=True)

        # get a specific resolution of  the video.
        video_resolution = video.streams.filter(resolution=resolution).first()
        video_filename = f"{index}. {video_resolution.default_filename}"
        print(video_resolution)
        print(video_filename)
        print(" --- -- - -- - -- ")

        # to create a path to find later and do manipulation on it.
        video_path = os.path.join(playlist_name, video_filename)
        print("video path= ", video_path)

        # to check if the video path exisits or not
        if os.path.exists(video_path):
            print(f"{video_filename} already exists")
            continue

        print(
            f"Downloading {video_filename} in {video_resolution.resolution}")
        # video_resolution.download(filename=video_filename) # to download videos only
        audio_res = video.streams.get_audio_only() # to get only the audio of the video
        audio_res.download(output_path="E:/@pple/cOol $oNgS/mix tape/season 3/", filename=f"{video_filename.split(sep='.mp4')[0]}.mp3")

        print("----------------------------------")

"""
    extra code to do something if needed as per the wish 
        video_path = os.path.join(playlist_name, video_filename)
        if os.path.exists(video_path):
            print(f"{video_filename} already exists")
            continue

        video_streams = video.streams.filter(res=resolution)

        if not video_streams:
            highest_resolution_stream = video.streams.get_highest_resolution()
            video_name = highest_resolution_stream.default_filename
            print(
                f"Downloading {video_name} in {highest_resolution_stream.resolution}")
            highest_resolution_stream.download(filename=video_path)

        else:
            video_stream = video_streams.first()
            video_name = video_stream.default_filename
            print(f"Downloading video for {video_name} in {resolution}")
            video_stream.download(filename="video.mp4")
            
            audio_stream = video.streams.get_audio_only()
            print(f"Downloading audio for {video_name}")
            audio_stream.download(filename="audio.mp4")
            
            os.system(
                "ffmpeg -y -i video.mp4 -i audio.mp4 -c:v copy -c:a aac final.mp4 -loglevel quiet -stats")
            os.rename("final.mp4", video_path)
            os.remove("video.mp4")
            os.remove("audio.mp4")

        print("----------------------------------")

= == = = = == == = =
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()

# Extract the audio
video = VideoFileClip('filename.mp4')
audio = video.audio
audio.write_audiofile('filename.mp3')
"""


playlist_url = "url_goes_here_from_yt"

download_playlist(playlist_url=playlist_url, resolution="1080p")