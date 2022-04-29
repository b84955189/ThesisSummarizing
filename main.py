#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   main.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/4/28 15:41
@Description  Python version-3.10

"""
from gui.gui import start
from pathlib import Path

# 模板路径
TEMPLATE_PATH = Path(__file__).parent / Path("./template")
RATING_INFORMATION_FILE_PATH = TEMPLATE_PATH / Path("./rating-information.xlsx")


def main():
    start()


if __name__ == "__main__":
    main()
