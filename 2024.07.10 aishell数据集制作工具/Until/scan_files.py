import os
import sys


# 遍历文件
def scan_file(file_path, file_format):
    """

    :param file_path: 需要遍历文件的文件夹
    :param file_format: 需要遍历文件的类型
    :return: 遍历后的文件列表
    """
    ans_file = []  # 函数返回结果
    for filenames in os.listdir(file_path):  # 遍历文件
        if filenames.split('.')[1] == file_format:
            ans_file.append(os.path.join(file_path, filenames))
    return ans_file


if __name__ == "__main__":

    file_path = "E:\\yang\\专业\\Python Code\\Script\\test"
    file_format = "m4a"
    for f in scan_file(file_path, file_format):
        print(f)

