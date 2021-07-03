import sys
import datetime
from pytube import YouTube

# youtube_video_url = 'https://youtu.be/8uJ-wOljP_s'

youtube_video_urls = [<<list of youtube video URLs>>]


def progress_function(chunk, file_handle, bytes_remaining):
    global filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write(' ↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()


count = 2

for youtube_video_url in youtube_video_urls:

    try:
        yt_obj = YouTube(youtube_video_url, on_progress_callback=progress_function)

        highest_resolution_stream = yt_obj.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

        itag = highest_resolution_stream.itag

        filesize = highest_resolution_stream.filesize

        video_title = yt_obj.title

        video_title_trimmed = video_title.split('|')[0].strip()

        video_name = str(count)+". "+video_title_trimmed

        print(f"Downloading \'{video_name}\'.....")

        print(datetime.datetime.now().strftime("%H:%M:%S"))

        highest_resolution_stream.download(output_path='/home/username/folder', filename=video_name)
        print('Video Downloaded Successfully at', datetime.datetime.now().strftime("%H:%M:%S"))
    except Exception as e:
        print(e)

    count = count + 1