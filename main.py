#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   main.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/4/28 15:41
@Description  Python version-3.10

"""
import datetime
import time

from func.ExcelFunc import get_workbook, get_debate_scores_data, get_teacher_scores_data, close_workbook


def start():
    # 数据文件地址
    # wb = get_workbook("D:\\Projects\\Python\\ThesisSummarizing\\template\\rating-information.xlsx")
    # get_debate_scores_data(wb)
    # get_teacher_scores_data(wb)
    # get_debate_scores_data(wb)
    # close_workbook(wb)

    print(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d-%H-%M-%S"))


if __name__ == "__main__":
    start()
