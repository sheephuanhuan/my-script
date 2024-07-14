import sys

from Until import scan_files, audio_transition_by_ffmpeg
from tools import (menu, default_config_information, config_information,
                   audio_duration_statistics, batch_file_rename,
                   batch_change_audio_title, user_choose)

# 先加载默认配置
infor = default_config_information()
print("{:-^100}".format("查看当前配置信息↓"))
print("[info : default config] 原音频文件存放目录: ", infor['original_directory'])
print("[info : default config] 原音频文件格式: ", infor['original_format'])
print("[info : default config] 转换后的音频格式: ", infor['target_format'])
print("[info : default config] 转换后的音频保存目录: ", infor['save_directory'])
print("[info : default config] 重命名文本文件: ", infor['rename_path'])
print("{:-^100}".format("查看当前配置信息↑"))

infor = user_choose()

while True:
    num = eval(menu())
    if num == 1:
        print("{:-^100}".format("查看当前配置信息↓"))
        print("[info : ] 原音频文件存放目录：", infor['original_directory'])
        print("[info : ] 原音频文件格式：", infor['original_format'])
        print("[info : ] 转换后的音频格式：", infor['target_format'])
        print("[info : ] 转换后的音频报错目录：", infor['save_directory'])
        print("{:-^100}".format("查看当前配置信息"))
        infor = user_choose()

        while True:
            print("{:-^30}".format("再次确认当前配置信息"))
            print("[info : ] 原音频文件存放目录：", infor['original_directory'])
            print("[info : ] 原音频文件格式：", infor['original_format'])
            print("[info : ] 转换后的音频格式：", infor['target_format'])
            print("[info : ] 转换后的音频报错目录：", infor['save_directory'])
            print("{:-^30}".format("-"))
            choose = input("[info : input ] 是否执行【音频格式转换】该操作(y or n): ")
            if choose == 'y' or choose == "Y":
                files = scan_files.scan_file(infor['original_directory'], infor['original_format'])
                for f in files:
                    audio_transition_by_ffmpeg.audio_formet_transition_by_ffmpeg(f, infor['save_directory'],
                                                                                 infor['target_format'])
                break
            else:
                print("[info : failure ] 已取消【音频格式转换】操作")
                break

    elif num == 2:
        print("{:-^30}".format("查看当前配置信息"))
        print("[info : ] 需要统计音频的文件目录是：", infor['original_directory'])
        print("[info : ] 需要统计音频的格式是：", infor['original_format'])
        print("{:-^30}".format("-"))
        infor = user_choose()

        while True:
            print("{:-^30}".format("再次确认当前配置信息"))
            print("[info : ] 需要统计音频的文件目录是：", infor['original_directory'])
            print("[info : ] 需要统计音频的格式是：", infor['original_format'])
            print("{:-^30}".format("-"))
            choose = input("[info : input ] 是否执行【音频统计】操作(y or n): ")
            if choose == 'y' or choose == "Y":
                audio_duration_statistics(infor['original_directory'], infor['original_format'])
                break
            else:
                print("[info : failure ] 已取消【音频统计】操作")
                break

    elif num == 3:
        print("{:-^30}".format("查看当前配置信息"))
        print("[info : ] 需要重命名音频文件目录是：", infor['original_directory'])
        print("[info : ] 需要重命名音频格式是：", infor['original_format'])
        print("[info : ] 需要重命名文本文件路径是：", infor['rename_path'])
        print("{:-^30}".format("-"))
        infor = user_choose()
        while True:
            print("{:-^30}".format("再次确认配置信息"))
            print("[info : ] 需要重命名音频文件目录是：", infor['original_directory'])
            print("[info : ] 需要重命名音频格式是：", infor['original_format'])
            print("[info : ] 需要重命名文本文件路径是：", infor['rename_path'])
            print("{:-^30}".format("-"))
            choose = input("[info : input ] 是否执行【文件重命名】操作(y or n): ")
            if choose == 'y' or choose == "Y":
                batch_file_rename(infor['original_directory'], infor['original_format'], infor['rename_path'])
                break
            else:
                print("[info : failure ] 已取消【文件重命名】操作")
                break

    elif num == 4:
        print("{:-^30}".format("查看当前配置信息"))
        print("[info : ] 需要改变标题的音频文件目录是：", infor['original_directory'])
        print("{:-^30}".format("-"))
        infor = user_choose()
        while True:
            print("{:-^30}".format("再次确认当前配置信息"))
            print("[info : ] 需要改变标题的音频文件目录是：", infor['original_directory'])
            print("{:-^30}".format("-"))
            choose = input("[info : input ] 是否执行【修改音频文件标题】操作(y or n): ")
            if choose == 'y' or choose == "Y":
                batch_change_audio_title(infor['original_directory'], infor['original_format'])
                break
            else:
                print("[info : failure ] 已取消【修改音频文件标题】操作")
                break

    elif num == 0:
        print("Bye~")
        sys.exit()
    else:
        print("输入有误")
