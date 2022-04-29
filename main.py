#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   main.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/4/28 15:41
@Description  Python version-3.10

"""


from pathlib import Path
from func.ExcelFunc import get_workbook, get_debate_scores_data, get_teacher_scores_data, get_comment_scores_data, close_workbook
from func.WordFunc import generate_word_to_file

# TODO: 增加GUI，使用户自定义选择数据文件位置
# 模板路径
TEMPLATE_PATH = Path(__file__).parent / Path("./template")
RATING_INFORMATION_FILE_PATH = TEMPLATE_PATH / Path("./rating-information.xlsx")


def start():
    print("文件生成中...")
    try:
        # 数据信息Excel文件地址
        wb = get_workbook(RATING_INFORMATION_FILE_PATH)
        # 生成Word
        for model in get_comment_scores_data(wb):
            generate_word_to_file(model)
        for model in get_teacher_scores_data(wb):
            generate_word_to_file(model)
        for model in get_debate_scores_data(wb):
            generate_word_to_file(model)
        # 关闭数据信息工作簿
        close_workbook(wb)
        print("生成完毕, 生成目录：", Path(__file__).parent / Path("./out"))
    except Exception as e:
        print("错误：", e)
    finally:
        print("程序退出....")


if __name__ == "__main__":
    start()
