import os


def file_rename(old_file_name, new_file_name):
    """
    
    """

    # 使用os.rename()方法重命名文件
    # 检查文件是否存在
    if os.path.exists(old_file_name):
        # 尝试重命名文件
        try:
            os.rename(old_file_name, new_file_name)
            print("[info: success] 文件已成功重命名为", new_file_name)
        except Exception as e:
            print("[info: failure] 重命名文件时出错：", e)
    else:
        print("[info: failure] 找不到名为", old_file_name, "的文件")


