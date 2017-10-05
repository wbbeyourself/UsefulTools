# coding=utf-8
"""
@author: beyourself
@time: 2017/10/5 23:17
"""

import os


class Scanner(object):
    # To be improved
    BUILT_IN = ['sys', 'time', 'os', 'json', ]

    def __init__(self, file_path):
        self.file_path = None
        if os.path.isdir(file_path):
            self.file_path = file_path

    def get_local_modules(self):
        return []

    def get_pip_list(self):
        return {'Flask': 'Flask==0.12.2'}