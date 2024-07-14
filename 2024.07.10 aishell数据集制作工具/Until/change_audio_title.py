import os

from mutagen.mp4 import MP4


def change_audio_title(file_path, new_title):
    audio = MP4(file_path)
    # 修改标题（'©nam'是.m4a文件中标题的标签）
    audio['\xa9nam'] = new_title
    audio.save()
    print("[info: success] 文件标题修改成功", new_title)


