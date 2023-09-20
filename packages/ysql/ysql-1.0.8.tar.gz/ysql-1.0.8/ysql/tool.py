# -*- coding: utf-8 -*-
import os
import shutil


def get_example():
    """复制本文件的工具函数"""
    # 获取当前文件的路径
    src = os.path.join(os.path.dirname(__file__), 'example.py')
    dst = "ysql_example.py"
    shutil.copy(src, dst)
    print('已生成示例文件：ysql_example.py')


if __name__ == '__main__':
    get_example()
