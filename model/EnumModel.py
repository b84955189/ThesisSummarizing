#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   EnumModel.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/5/1 15:42
@Description  Python version-3.10

"""
from enum import IntEnum,unique


@unique
class SheetType(IntEnum):
    """表类型 - 枚举"""
    COMMENT_SCORES_SHEET = 1,
    DEBATE_SCORES_SHEET = 2,
    TEACHER_SCORES_SHEET = 3

