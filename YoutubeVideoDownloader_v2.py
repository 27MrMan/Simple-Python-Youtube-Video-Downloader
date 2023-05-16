from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *
import time

#Check bottom of file.

link = input("Enter the full youtube URL")
SkipVideoDownload = input("Do you want to download the video as an MP4? Reply with Y or N")
if  SkipVideoDownload == "Y":
    yt = YouTube(link, on_progress_callback=on_progress)
    ytstreams = yt.streams
    mp4streams = ytstreams.filter(file_extension='mp4')
    print(mp4streams.get_highest_resolution())
    HighRes = mp4streams.get_highest_resolution()
    HighRes.download(output_path="D:/")
    print("Download is completed successfully")

else:
    yt = YouTube(link)
    ytstreams = yt.streams
    mp4streams = ytstreams.filter(file_extension='mp4')
    print(mp4streams.get_lowest_resolution())
    lowres = mp4streams.get_lowest_resolution()
    lowres.download(output_path="D:/", filename="tobeconverted.mp4")
    print("Download Completed Successfully")
    VideoNamed = yt.title
    print(VideoNamed)
    video = VideoFileClip(filename="tobeconverted.mp4")
    VideoName = VideoNamed+".mp3"
    audio = video.audio
    audio.write_audiofile(filename=VideoName, codec="aac",)
#FIX!!! codec has been changed to aac due to some random videos defaulting to libx256 or something
print("Download Completed Successfully")
print("Completed")
time.sleep(5)
#Line 78 of innertube.py in pytube folder must be changed from ANDRIOD to WEB.
#Progress bar does not work due to some issues with Pytube.
