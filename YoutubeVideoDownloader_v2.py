from pytube import YouTube
from moviepy.editor import *
import time

def Download(link):
    youtubeObject = YouTube(link).streams
    try:
        mp4streams = youtubeObject.filter(file_extension='mp4')
        print(mp4streams.get_highest_resolution())
        HighRes = mp4streams.get_highest_resolution()
        HighRes.download(output_path="D:/")
    except:
        print("Emotional Damage")
    print("Download is completed successfully")

def AudioDownload(link):
    youtubeObject = YouTube(link).streams
    try:
        mp4streams = youtubeObject.filter(file_extension='mp4')
        print(mp4streams.get_highest_resolution())
        HighRes = mp4streams.get_highest_resolution()
        HighRes.download(output_path="D:/")
        VideoNamed = YouTube(link).streams[0].title
        VideoName = VideoNamed + ".mp4"
        print(VideoName)
        video = VideoFileClip(VideoName)
        audio = video.audio
        audio.write_audiofile(VideoName[:-3]+"mp3")
    except:
        print("Emotional Damage")
    print("Download Completed Successfully")
        
LDigits = input("Enter the full youtube URL")
link = LDigits
SkipVideoDownload = input("Do you want to download the video as an MP4? You have 5 seconds to answer. Reply with Y or N")
time.sleep(5)
if  SkipVideoDownload == "Y":
    Download(link)
else:
    AudioDownload(link)
print("Completed")
time.sleep(5)