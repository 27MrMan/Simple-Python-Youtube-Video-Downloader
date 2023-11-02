#importing various modules...
from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import *
import time

downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")
downloads_path = os.path.normpath(downloads_path) + "/"
downloads_path = str(downloads_path)
print(" Video will be downloaded to ", downloads_path)

#program start 
time.sleep(1)

link = input("Enter the full youtube URL ")
SkipVideoDownload = input("Do you want to download the video? Reply with Y or N, to split Audio. ")
if  SkipVideoDownload == "Y":
    yt = YouTube(link, on_progress_callback=on_progress)
    ytstreams = yt.streams
    mp4streams = ytstreams.filter(file_extension='mp4')
    print(mp4streams.get_highest_resolution())
    HighRes = mp4streams.get_highest_resolution()
    HighRes.download(output_path=downloads_path)
    print("Download is completed successfully")

elif SkipVideoDownload == "N":
    yt = YouTube(link, on_progress_callback=on_progress)
    ytstreams = yt.streams
    mp4streams = ytstreams.filter(file_extension='mp4')

    print(mp4streams.get_lowest_resolution())
    lowres = mp4streams.get_lowest_resolution()
    lowres.download(output_path=downloads_path, filename="Video+AudioDownload.mp4")
    print("Download Completed Successfully")
    video = VideoFileClip(filename=downloads_path+"Video+AudioDownload.mp4")
    audio = video.audio
    audio.write_audiofile(filename=downloads_path+"AudioOnlyDownload.wav", codec="pcm_s32le")
    print("File has been converted")

else:
    print("Type it exactly as 'Y' or 'N' (without the quotes). Run the program agian")

print("Completed, closing...")
time.sleep(5)
