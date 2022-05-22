from gtts import gTTs
import os

msg = "you hve been hacked"
language = 'en'

obj = gTTs(text=msg, lang=language, slow =False)
obj.save('virus.mp4')
for i in range(5):
    os.system('mpg321 Virus.mp4')