from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *
import time
    
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
    yt = YouTube(link, on_progress_callback=on_progress)
    ytstreams = yt.streams
    mp4streams = ytstreams.filter(file_extension='mp4')
    print(mp4streams.get_lowest_resolution(), "Download with start soon...")
    lowres = mp4streams.get_lowest_resolution()
    lowres.download(output_path="D:/")
    VideoNamed = yt.title
    VideoName = VideoNamed + ".mp4"
    print(VideoName)
    video = VideoFileClip(VideoName)
    audio = video.audio
    audio.write_audiofile(VideoName[:-3]+"mp3")
print("Download Completed Successfully")
print("Completed")
time.sleep(5)
#Line 78 of innertube.py in pytube folder has been changed from ANDRIOD to WEB. As soon as fix is found, fix it.
