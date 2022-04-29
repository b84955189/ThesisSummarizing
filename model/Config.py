#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   Config.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/4/26 10:07
@Description  Python version-3.10
# TODO: 项目配置信息汇总移植
"""


class Configs:
    # GUI
    default_welcome_tips = ""
    default_app_name = ""
    # #Refresh second
    default_refresh_second = 0

    def __init__(self,
                 default_app_name="论文汇总 v1.0",
                 default_welcome_tips="Hello World!\nLYU...",
                 default_refresh_second=0.2
                 ):
        # GUI
        self.default_app_name = default_app_name
        self.default_welcome_tips = default_welcome_tips
        # #Refresh second
        self.default_refresh_second = default_refresh_second



