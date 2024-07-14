import sys
import time
import os
from Until.change_audio_title import change_audio_title  # m4a标题修改工具
from Until.files_rename import file_rename  # 音频文件重命名工具
from Until.get_audio_duration import get_audio_duration  # 获取录音时长
from Until.scan_files import scan_file  # 文件扫描工具
from tqdm import tqdm


#  菜单
def menu():
    print("{:-^100}".format("查看语音功能菜单↓"))
    print("1. 音频格式转换")
    print("2. 音频时长统计")
    print("3. 文件重命名")
    print("4. 修改音频文件标题")
    print("0. 退出程序！")
    print("{:-^100}".format("查看语音功能菜单↑"))
    return input("请选择功能：")


def default_config_information():
    default_original_directory = r"./original directory"
    default_original_format = "m4a"
    default_target_format = "wav"
    default_save_directory = r"./save directory"
    default_rename_path = r"./original directory/renamed.txt"
    return {"original_directory": default_original_directory,
            "target_format": default_target_format,
            "original_format": default_original_format,
            "save_directory": default_save_directory,
            "rename_path": default_rename_path}


def config_information():
    print("{:-^100}".format("修改配置信息↓"))
    original_directory = input("请输入原音频文件存放目录路径（[Enter] 忽略此设置）：")
    original_format = input("请输入原音频文件格式（[Enter] 忽略此设置）：")
    target_format = input("请输入转换后音频文件格式（[Enter] 忽略此设置）：")
    save_directory = input("请输入转换后音频文件保存目录（[Enter] 忽略此设置）：")
    rename_path = input("请输入重命名文本文件路径（[Enter] 忽略此设置）：")
    print("{:-^100}".format("修改配置信息↑"))
    return {"original_directory": original_directory, "target_format": target_format,
            "original_format": original_format, "save_directory": save_directory,
            "rename_path": rename_path}


def user_choose():

    while True:
        choose = input("[info : input ] 是否修改配置信息(y or n): ")
        if choose == 'y':
            infor = config_information()
            return infor

        # n时，使用默认配置
        elif choose == 'n':
            infor = default_config_information()
            return infor

        else:
            print("[info: failure ] 输入有误，请重新输入！")
            continue


# 音频时长统计
def audio_duration_statistics(file_path, file_format):
    total_duration = 0  # 总时长
    total_size = 0  # 统计文件大小
    files_list_proc = tqdm(scan_file(file_path, file_format))
    for file in files_list_proc:
        file_size = os.path.getsize(file)
        file_name = os.path.basename(file)
        files_list_proc.set_postfix({"正在统计": file_name})
        file_duration = get_audio_duration(file)
        second = file_duration.split(":")[2]  # 得到秒
        total_duration += float(second)
        total_size += file_size
        # print(file, file_duration)

    res = time.strftime('%H:%M:%S', time.gmtime(total_duration))

    print("=========================================")
    print("音频: {}条, 总时长: {}, 共大小{:.2f}MB".format(len(files_list_proc), res, total_size / (1024*1024)))
    print("=========================================")


def batch_change_audio_title(file_path, file_format):
    files_list = scan_file(file_path, file_format)
    for file in files_list:
        # 使用os.path.splitext来分割文件名和扩展名
        file_name_without_extension, file_extension = os.path.splitext(os.path.basename(file))
        # print(file, file_name_without_extension)
        change_audio_title(file, file_name_without_extension)


def batch_file_rename(file_path, file_format, rename_txt_path):
    """
    :param file_path: 文件路径
    :param file_format: 文件格式
    :param rename_txt_path: 重命名文本文件路径
    :return: 无
    """
    file_list = scan_file(file_path, file_format)  # 需要重命名的文件
    rename_txt_list = []  # 存放新文件名
    with open(rename_txt_path, 'r', encoding='utf-8') as file:
        for line in file:
            save_path = os.path.join(file_path, line.strip() + ".m4a")
            rename_txt_list.append(save_path)

    print("[info: ] 请检查 ")
    for old, new in zip(file_list, rename_txt_list):
        print(old, "\t", new)

    num = input("请输入: [n/y]")
    if num == "y":
        for old, new in zip(file_list, rename_txt_list):
            file_rename(old, new)
        print("[info: success] OK! ")


