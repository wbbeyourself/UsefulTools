# coding=utf-8
# python 3.x

"""
@author: beyourself
@time: 2019/6/25 13:55
@file: tools.py
"""
import os
import pickle
import string

# 递归新建文件夹
def makedirs(filename):
    dir_path = os.path.dirname(os.path.abspath(filename))
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        print('makedirs %s' % dir_path)

# 将数据保存为pickle文件
def save_pickle_file(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    print('saved pkl file ', filename)


# 加载pickle文件
def load_pickle_file(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data


# 把content列表保存成文本文件
def save_file(filename, content):
    """
    :param filename: 输出文件名
    :param content: 句子列表 默认每个元素自带换行啊
    :return:
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(content)
    print('save file %s successful!' % filename)


# 给定文件名，和待pickle的对象，用新文件将其覆盖
def overwrite_pkl_file(filename, data):
    tmp_filename = filename + '.swp'
    save_pickle_file(data, tmp_filename)
    if os.path.exists(filename):
        os.rename(filename, filename + '.old.' + datetime2str())
    os.rename(tmp_filename, filename)
    print('overwrite %s successful!' % filename)


# 给定文件名，和待保存的字符串列表，用新文件将其覆盖
def overwrite_txt_file(filename, data):
    tmp_filename = filename + '.swp'

    save_file(tmp_filename, data)
    if os.path.exists(filename):
        os.rename(filename, filename + '.old.' + datetime2str())
    os.rename(tmp_filename, filename)
    print('overwrite %s successful!' % filename)


# 读取文件的每一行, 返回列表
def get_lines(filename):
    with open(filename, encoding='utf-8') as f:
        return f.readlines()


# 判断一个词语是不是纯中文词语，即不包含汉字以外的其他符号
def is_chinese_word(word):
    for c in word:
        if not ('\u4e00' <= c <= '\u9fa5'):
            # print(word)
            return False
    return True


# 判断一个字符是不是中文字符
def is_chinese_char(c):
    if len(c.strip()) == 1 and '\u4e00' <= c <= '\u9fa5':
        return True
    return False


# 判断一个单词是否只含有大小写字母
def is_letters(word):
    for c in word:
        if (c >= '\u0041' and c <= '\u005a') or (c >= '\u0061' and c <= '\u007a'):
            continue
        return False
    return True


# 判断一个单词是否只含有大写字母
def is_upper_letters(word):
    for c in word:
        if c >= '\u0041' and c <= '\u005a':
            continue
        return False
    return True


def is_upper_letters(word):
    for c in word:
        if c not in string.ascii_uppercase:
            return False
    return True


# 判断一个短语/单词，是不是纯英文短语/单词，即只含有26个大小写字母和空格
def is_pure_english_phrase(word):
    for c in word:
        if (c >= '\u0041' and c <= '\u005a') or (c >= '\u0061' and c <= '\u007a') or c == ' ':
            continue
        return False
    return True


def datetime2str():
    from datetime import datetime
    return datetime.now().strftime('%Y%m%d-%H%M%S')


# 计算从start到现在花费的时间
def time_cost(start):
    import time
    cost = int(time.time() - start)
    h = cost // 3600
    m = (cost % 3600) // 60
    print('')
    print('%s : cost %s hours %s mins' % (datetime2str(), h, m))


# 将 content_list 追加到filename中
def append_file(filename, content_list):
    if not content_list:
        return
    with open(filename, 'a+', encoding='utf-8') as f:
        f.writelines(content_list)
    print('append_file %s successful!' % filename)


if __name__ == '__main__':
    print(is_upper_letters('ADFFF') is True)
    print(is_upper_letters('Agfdg') is False)
    pass
