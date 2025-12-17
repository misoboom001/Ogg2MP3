import os
import sys
from pydub import AudioSegment

dir_path = sys.argv[1]
if not dir_path.endswith('\\'):
    dir_path = dir_path + '\\'

files_file = [
    f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and os.path.join(dir_path, f).endswith('.ogg')
]


for sound_file in files_file:
    sound_file_path = dir_path + sound_file
    ogg_audio = AudioSegment.from_ogg(sound_file_path)

    sound_file = os.path.splitext(sound_file)[0] + '.mp3'
    sound_file_path = dir_path + sound_file
    ogg_audio.export(sound_file_path, format="mp3")
    print(sound_file_path + ':変換完了')