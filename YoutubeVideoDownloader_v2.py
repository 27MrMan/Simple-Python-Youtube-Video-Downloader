#importing, if doesnt work, check readme
from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *
import time
    
link = input("Enter the full youtube URL ")
SkipVideoDownload = input("Do you want to download the video as an MP4? Reply with Y or N ")
if  SkipVideoDownload == "Y":
    yt = YouTube(link, on_progress_callback=on_progress)
    ytstreams = yt.streams
    mp4streams = ytstreams.filter(file_extension='mp4')
    print(mp4streams.get_highest_resolution())
    HighRes = mp4streams.get_highest_resolution()
    HighRes.download(output_path="D:/")
    print("Download is completed successfully")

elif SkipVideoDownload == "N":
    yt = YouTube(link, on_progress_callback=on_progress)
    ytstreams = yt.streams
    mp4streams = ytstreams.filter(file_extension='mp4')

    print(mp4streams.get_lowest_resolution())
    lowres = mp4streams.get_lowest_resolution()
    lowres.download(output_path="D:/", filename="tobeconverted.mp4")
    print("Download Completed Successfully")
    video = VideoFileClip(filename="tobeconverted.mp4")
    video.audio.write_audiofile(filename="convertedfile.wav", codec="pcm_s32le")

else:
    print(" Type 'Y' or 'N' ")
    
print("Completed")
time.sleep(5)
