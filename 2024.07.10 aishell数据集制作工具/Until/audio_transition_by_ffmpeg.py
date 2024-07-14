import os


def audio_formet_transition_by_ffmpeg(file_path, directory, target_format):
    """

    :param file_path: 原始音频的文件路径
    :param directory: 转换后音频文件的保存目录
    :param target_format: 需要转换后的音频格式
    :return: 命令执行结果 0:成功  1:失败
    """
    file_name = os.path.split(file_path)[1].split('.')[0]  # 路径拆分，文件名和文件格式拆分，获取文件名
    # ffmpeg命令,w4a转换wav
    command = f'ffmpeg -i "{file_path}" -ac 1 -ar 160000 "{os.path.join(directory, file_name)}.{target_format}"'
    # print(command)
    res = os.system(command)  # 执行命令, 成功返回0，失败返回1
    return res

