# 桌面归档程序

import os
import shutil

path = '/Users/fangzhiyang/Desktop'

desktop_file_list = os.listdir(path)

file_type_set = set()

# 新建一个函数，名称get_file_type，获取文件类型
def get_file_type(filename):
    index = filename.rfind('.')
    file_type = filename[index + 1:]
    return file_type

# 1、按个判断每个文件
for file in desktop_file_list:
    # 2、跳过，不处理.DS_Store
    if file == '.DS_Store':
        continue

    # 3、如果是文件，不是文件夹，就把文件类型加入file_type_set
    # file如123.docx
    if file.rfind('.') != -1:
        file_type_set.add(get_file_type(file))

# 4、看一下我们有哪些文件类型
index = 1
for type in file_type_set:
    print(index, ':文件类型:', type)
    index += 1

# 5、以相应的文件类型创建文件夹，把相应文件移入
# pdf
for type in file_type_set:
    for filename in desktop_file_list:
        # 6、如果文件名以某种类型结尾
        if filename.endswith(type):
            # 以pdf命名的文件夹
            # path = '/Users/fangzhiyang/Desktop'
            # file_type = 'pdf'
            # /Users/fangzhiyang/Desktop/pdf
            # 7、如果目录不存在，就创建
            if os.path.exists(path + '/' + type):
                pass
            else:
                os.mkdir(path + '/' + type)

            # 8、移动文件到指定文件夹
            shutil.move(path + '/' + filename,
                        path + '/' + type + '/' + filename)

print("文件归档完成！")