from pydub import AudioSegment
from pydub.playback import play


playaudio = AudioSegment.from_file(
    "sant.mp3", format="mp3")
play(playaudio)
