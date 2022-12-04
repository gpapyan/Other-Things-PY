from pytube import Playlist
import re


playlist = Playlist("YOUTUBE PLAYLIST LINK")
playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
print(f'Downloading: {playlist.title}')
for video in playlist.videos:
    print(f'Downloading  -->  {video.title} ------>  {video}')
    video.streams.filter(type='video',progressive=True,file_extension='mp4').\
        order_by('resolution').\
            desc().\
                first().\
                    download()
