import subprocess
import time 


def get_audio_duration(file_path):
    """
    获取音频文件的时长

    :param file_path: 音频文件的路径
    :return: 返回音频文件的时长，格式为 'HH:MM:SS'
    """
    # 使用ffprobe命令获取音频文件的时长
    cmd = f"ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 {file_path}"
    # 执行命令并获取结果
    result = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
    # 将结果转换为浮点数
    duration = float(result)
    # 将时长转换为 'HH:MM:SS' 格式并返回
    return time.strftime('%H:%M:%S', time.gmtime(duration))

