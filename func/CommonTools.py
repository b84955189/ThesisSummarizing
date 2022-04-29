#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   CommonTools.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/4/29 15:57
@Description  Python version-3.10
常用工具类
"""


def is_empty_or_none(s):
    """
    判断字符串是否有效
    True - 无效值
    False - 有效值
    @param s: 字符串
    @return: bool
    """
    return s is None or len(s.strip()) == 0


def test():
    """
    测试方法
    @return:
    """
    s = None
    print(is_empty_or_none(s))


if __name__ == "__main__":
    test()

