from pytube import YouTube
from moviepy.editor import *
import time

def Download(link):
    youtubeObject = YouTube(link).streams
    try:
        mp4streams = youtubeObject.filter(file_extension='mp4')
       # !!! BUGFIX! if you get keyError [StreamingData], then go to C:\Users\<insertusername>\AppData\Local\Packages\PythonSoftwareFoundation.Python.3, etc, \LocalCache\local-packages\Python3XX\site-packages\pytube\innertube.py
       #then, change line 78 to     def __init__(self, client='WEB', use_oauth=False, allow_cache=True): #(the client='ANDROID' should be client='WEB'
        print(mp4streams.get_highest_resolution())
        HighRes = mp4streams.get_highest_resolution()
        HighRes.download(output_path="D:/")
    except:
        print("Emotional Damage")
    print("Download is completed successfully")

def AudioDownload(link):
    youtubeObject = YouTube(link).streams
    try:
        #CHECK THE BUGFIX ABOVE
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
SkipVideoDownload = input("Do you want to download the video as an MP4? Reply with Y or N")
if  SkipVideoDownload == "Y":
    Download(link)
else:
    AudioDownload(link)
print("Completed")
time.sleep(5)
