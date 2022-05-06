#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   ExceptionModels.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/5/5 21:23
@Description  Python version-3.10

"""


class InvalidRatingRecordException(ValueError):
    """无效评分记录Exception"""
    pass


class DuplicatedRatingRecordException(ValueError):
    """重复评分记录Exception - 依据 学生学号 """
    pass


class StudentRatingRecordIncompleteException(ValueError):
    """不完整学生评分记录Exception - 不同时拥有三表评分记录 """
    pass


