from pytube import YouTube

url = "https:/www.youtube.com/watch?v=hzTg4zPBtDU"

video = YouTube(url)
print('Downloading The File !')
audio = video.streams.filter(only_audio=True)
audio[0].download("C:\\Users\\win7\\Music\\Downloads")
print('File Downloaded !')
