from pytube import YouTube

video = YouTube('https://www.youtube.com/watch?v=Ewmg1Z94mks')

# video.streams.all()

print(video.streams.filter(file_extension = "mp4").all())

video.streams.get_by_itag(18).download()