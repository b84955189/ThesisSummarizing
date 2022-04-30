#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   WordFunc.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/4/28 20:49
@Description  Python version-3.10

"""
import datetime
from pathlib import Path
from docx import Document

from model.RatingModels import CommentScoreModel, DebateScoreModel, TeacherScoreModel

# 模板路径
TEMPLATE_PATH = Path(__file__).parent.parent / Path("./template")
COMMENT_SCORE_FILE_PATH = TEMPLATE_PATH / Path("./comment-score.docx")
DEBATE_SCORE_FILE_PATH = TEMPLATE_PATH / Path("./debate-score.docx")
TEACHER_SCORE_FILE_PATH = TEMPLATE_PATH / Path("./teacher-score.docx")

# 替换关键字
MAJOR_KEY = "{{专业}}"
STU_NUMBER_KEY = "{{学号}}"
NAME_KEY = "{{姓名}}"
TOPIC_KEY = "{{题目}}"

SCORE_1_KEY = "{{分数1}}"
SCORE_2_KEY = "{{分数2}}"
SCORE_3_KEY = "{{分数3}}"
SCORE_4_KEY = "{{分数4}}"
SCORE_5_KEY = "{{分数5}}"
SCORE_6_KEY = "{{分数6}}"

TOTAL_SCORE_KEY = "{{总分}}"
YEAR_KEY = "{{年}}"
MONTH_KEY = "{{月}}"
DAY_KEY = "{{日}}"

# 年月日 - 默认当前时间
DEFAULT_YEAR = f"{datetime.datetime.now().year}"
DEFAULT_MONTH = f"{datetime.datetime.now().month}"
DEFAULT_DAY = f"{datetime.datetime.now().day}"

# 生成文件名格式 - [指导老师]-[学号]-[姓名]
COMMENT_SCORE_FILE_NAME_FORMAT = "{}-{}-{}-计科-2022届-毕业设计（论文）论文评阅评分表.docx"
DEBATE_SCORE_FILE_NAME_FORMAT = "{}-{}-{}-计科-2022届-毕业设计（论文）答辩评分表.docx"
TEACHER_SCORE_FILE_NAME_FORMAT = "{}-{}-{}-计科-2022届-毕业设计（论文）指导老师评分表.docx"

# 输出路径
OUTPUT_PATH = Path(__file__).parent.parent / Path("./out")


def generate_word_to_file(rating_model, date_catalog):
    """
    生成word文件（docx）
    # TODO: 生成的每个Word文件名需带有指导老师
    @param rating_model: 评分记录实体类
    @param date_catalog: 日期时间 子目录
    @return: None
    """
    output_file_path = ''
    document = ''
    if isinstance(rating_model, CommentScoreModel):
        document = Document(COMMENT_SCORE_FILE_PATH)
        # 目录
        # 创建目录
        comment_score_file_catalog_path = date_catalog / Path("./论文评阅评分")
        # parents：如果父目录不存在，是否创建父目录。
        # exist_ok：只有在目录不存在时创建目录，目录已存在时不会抛出异常。
        comment_score_file_catalog_path.mkdir(parents=True, exist_ok=True)
        output_file_path = comment_score_file_catalog_path / Path(
            COMMENT_SCORE_FILE_NAME_FORMAT.format("测试老师", rating_model.student_number,
                                                  rating_model.student_name))
    elif isinstance(rating_model, DebateScoreModel):
        document = Document(DEBATE_SCORE_FILE_PATH)
        debate_score_file_catalog_path = date_catalog / Path("./答辩评分")
        debate_score_file_catalog_path.mkdir(parents=True, exist_ok=True)
        output_file_path = debate_score_file_catalog_path / Path(
            DEBATE_SCORE_FILE_NAME_FORMAT.format("测试老师", rating_model.student_number,
                                                 rating_model.student_name))
    elif isinstance(rating_model, TeacherScoreModel):
        document = Document(TEACHER_SCORE_FILE_PATH)
        teacher_score_file_catalog_path = date_catalog / Path("./指导老师评分")
        teacher_score_file_catalog_path.mkdir(parents=True, exist_ok=True)
        output_file_path = teacher_score_file_catalog_path / Path(
            TEACHER_SCORE_FILE_NAME_FORMAT.format("测试老师", rating_model.student_number,
                                                  rating_model.student_name))

    # 因为模板中只有一个表格对象
    table = document.tables[0]
    # TODO: 一致字体格式
    # 遍历段落
    for paragraph in document.paragraphs:
        # 测试
        # print(paragraph.style.name, paragraph.text)
        temp = paragraph.text
        # 关键字替换
        if MAJOR_KEY in temp:
            temp = temp.replace(MAJOR_KEY, rating_model.major)
        if STU_NUMBER_KEY in temp:
            temp = temp.replace(STU_NUMBER_KEY, rating_model.student_number)
        if NAME_KEY in temp:
            temp = temp.replace(NAME_KEY, rating_model.student_name)
        if TOPIC_KEY in temp:
            temp = temp.replace(TOPIC_KEY, rating_model.thesis_topic)
        if YEAR_KEY in temp:
            temp = temp.replace(YEAR_KEY, DEFAULT_YEAR)
        if MONTH_KEY in temp:
            temp = temp.replace(MONTH_KEY, DEFAULT_MONTH)
        if DAY_KEY in temp:
            temp = temp.replace(DAY_KEY, DEFAULT_DAY)
        paragraph.text = temp
    # 遍历表格
    # 遍历 表格-行
    for row in range(len(table.rows)):
        # 遍历 表格-行的每列值
        for cell_value in table.rows[row].cells:
            temp = cell_value.text
            # 关键字替换 - 这里由于评分记录实体对象不同 关键字也不同，所以无需担心该表没有该关键字却被赋值问题
            if SCORE_1_KEY in temp:
                temp = temp.replace(SCORE_1_KEY, str(rating_model.scores[0]))
            if SCORE_2_KEY in temp:
                temp = temp.replace(SCORE_2_KEY, str(rating_model.scores[1]))
            if SCORE_3_KEY in temp:
                temp = temp.replace(SCORE_3_KEY, str(rating_model.scores[2]))
            if SCORE_4_KEY in temp:
                temp = temp.replace(SCORE_4_KEY, str(rating_model.scores[3]))
            if SCORE_5_KEY in temp:
                temp = temp.replace(SCORE_5_KEY, str(rating_model.scores[4]))
            if SCORE_6_KEY in temp:
                temp = temp.replace(SCORE_6_KEY, str(rating_model.scores[5]))
            if TOTAL_SCORE_KEY in temp:
                temp = temp.replace(TOTAL_SCORE_KEY, str(rating_model.total_score))
            cell_value.text = temp
    # 储存新文件
    document.save(output_file_path)


def test():
    """
    测试方法
    @return: None
    """
    # template_path = Path(__file__).parent.parent / Path("./template")
    # file_path = template_path / Path("./comment-score.docx")
    # print(template_path)
    # document = Document(file_path)
    # 因为模板中只有一个表格对象
    # table = document.tables[0]
    # 遍历段落
    # for paragraph in document.paragraphs:
    #     print(paragraph.style.name, paragraph.text)
    #     temp = paragraph.text
    #     # 关键字替换
    #     if "{{专业}}" in temp:
    #         temp = temp.replace("{{专业}}", "计算机")
    #     if "{{学号}}" in temp:
    #         temp = temp.replace("{{学号}}", "202109070129")
    #     if "{{姓名}}" in temp:
    #         temp = temp.replace("{{姓名}}", "刘龙龙")
    #     if "{{题目}}" in temp:
    #         temp = temp.replace("{{题目}}", "Python自动化")
    #     if "{{年}}" in temp:
    #         temp = temp.replace("{{年}}", "2021")
    #     if "{{月}}" in temp:
    #         temp = temp.replace("{{月}}", "04")
    #     if "{{日}}" in temp:
    #         temp = temp.replace("{{日}}", "28")
    #     paragraph.text = temp
    # 遍历表格
    # 遍历 表格-行
    # for row in range(len(table.rows)):
    #     # 遍历 表格-行的每列值
    #     for cell_value in table.rows[row].cells:
    #         # print(cell_value.text)
    #         temp = cell_value.text
    #         # 关键字替换
    #         if "{{分数1}}" in temp:
    #             temp = temp.replace("{{分数1}}", "10")
    #         if "{{分数2}}" in temp:
    #             temp = temp.replace("{{分数2}}", "20")
    #         if "{{分数3}}" in temp:
    #             temp = temp.replace("{{分数3}}", "30")
    #         if "{{分数4}}" in temp:
    #             temp = temp.replace("{{分数4}}", "40")
    #         if "{{分数5}}" in temp:
    #             temp = temp.replace("{{分数5}}", "50")
    #         if "{{分数6}}" in temp:
    #             temp = temp.replace("{{分数6}}", "60")
    #         if "{{总分}}" in temp:
    #             temp = temp.replace("{{总分}}", "210")
    #         cell_value.text = temp
    # 储存新文件
    # document.save(template_path / Path("./new.docx"))
    # 测试创建目录
    # parents：如果父目录不存在，是否创建父目录。
    # exist_ok：只有在目录不存在时创建目录，目录已存在时不会抛出异常。
    # (template_path / Path(f'./{datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d-%H-%M-%S")}')).mkdir(
    #     parents=True, exist_ok=True)
    # generate_word_to_file()

    params = [1, '201809090001', '张三', '计科', '微信小程序的打法水电费打法的设计', [20, 30, 20, 8, 7, 6], 'Jason', '001']
    params_2 = [1, '201809090001', '张三', '计科', '微信小程序的打法水电费打法的设计', [20, 30, 20, 8, 7, 6], 'Jason', '001']
    params_3 = [1, '201809090001', '张三', '计科', '微信小程序的打法水电费打法的设计', [20, 30, 20, 8, 7, 6], 'Jason', 'FeiFei',
                'Auro,Jack,HuJian']
    a = CommentScoreModel()
    print(isinstance(a, CommentScoreModel))
    a.id = params[0]
    a.student_number = params[1]
    a.student_name = params[2]
    a.major = params[3]
    a.thesis_topic = params[4]
    a.scores = params[5]
    a.review_teacher_name = params[6]
    a.review_teacher_work_number = params[7]

    generate_word_to_file(a)

    # b = DebateScoreModel()
    # b.id = params_3[0]
    # b.student_number = params_3[1]
    # b.student_name = params_3[2]
    # b.major = params_3[3]
    # b.thesis_topic = params_3[4]
    # b.scores = params_3[5]
    # b.debate_group_leader_name = params_3[6]
    # b.debate_group_secretary_name = params_3[7]
    # b.debate_group_member = params_3[8]
    #
    # print(b)


if __name__ == "__main__":
    test()
