from moviepy.editor import *

mp4_file = 'C:\\Users\\win7\\Downloads\\video.mp4'
# mp3_file = 'C:\\Users\\win7\\Downloads'


videoclip = VideoFileClip(mp4_file)

audioclip = videoclip.audio
videoclip.write_videofile(mp4_file, fps=30, threads=1, codec="libx264")
# audioclip.write_audiofile(mp3_file, fps=30, codec="pcm_s16le")

audioclip.close()
videoclip.close()

# mp4	libx264
# ogv	libtheora
# webm	libvpx
# ogg	libvorbis
# mp3	pcm_s16le
# wav	libvorbis
# m4a	libfdk_aac
