#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   ExcelFunc.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/4/28 19:36
@Description  Python version-3.10
# TODO: 重构冗余代码
"""
from openpyxl import load_workbook

# Excel 表名称
from model.RatingModels import CommentScoreModel, DebateScoreModel, TeacherScoreModel

# TODO: 判断无效评分记录，无效则不读取

COMMENT_SCORE_SHEET_NAME = "评阅老师成绩"
DEBATE_SCORE_SHEET_NAME = "答辩成绩"
TEACHER_SCORE_SHEET_NAME = "指导老师成绩"


def get_workbook(file_path):
    return load_workbook(file_path)


def close_workbook(workbook):
    """
    关闭Excel工作簿对象
    @param workbook: Excel工作簿对象
    @return:
    """
    if workbook is not None:
        workbook.close()


def get_comment_scores_data(workbook):
    """
    读 评阅老师成绩 记录
    @param workbook: Excel工作簿对象
    @return: 评阅老师成绩 记录
    """
    comment_scores = []
    comment_scores_sheet = workbook[COMMENT_SCORE_SHEET_NAME]
    # 跳过评阅老师成绩表 表头
    for row in range(3, comment_scores_sheet.max_row + 1):
        comment_score = CommentScoreModel()

        comment_score.id = comment_scores_sheet.cell(row, 1).value
        comment_score.student_number = comment_scores_sheet.cell(row, 2).value
        comment_score.student_name = comment_scores_sheet.cell(row, 3).value
        comment_score.major = comment_scores_sheet.cell(row, 4).value
        comment_score.thesis_topic = comment_scores_sheet.cell(row, 5).value
        # 分数
        # TODO: 优化分数读取存储方式
        score_1 = comment_scores_sheet.cell(row, 6).value
        score_2 = comment_scores_sheet.cell(row, 7).value
        score_3 = comment_scores_sheet.cell(row, 8).value
        score_4 = comment_scores_sheet.cell(row, 9).value
        score_5 = comment_scores_sheet.cell(row, 10).value
        score_6 = comment_scores_sheet.cell(row, 11).value
        scores = [
            0 if score_1 is None else int(score_1),
            0 if score_2 is None else int(score_2),
            0 if score_3 is None else int(score_3),
            0 if score_4 is None else int(score_4),
            0 if score_5 is None else int(score_5),
            0 if score_6 is None else int(score_6),
        ]
        comment_score.scores = scores
        comment_score.review_teacher_name = comment_scores_sheet.cell(row, 13).value
        comment_score.review_teacher_work_number = comment_scores_sheet.cell(row, 14).value
        comment_scores.append(comment_score)

    return comment_scores


def get_debate_scores_data(workbook):
    """
    读 答辩成绩 记录
    @param workbook: Excel工作簿对象
    @return: 答辩成绩 记录
    """
    debate_scores = []
    debate_scores_sheet = workbook[DEBATE_SCORE_SHEET_NAME]

    # 跳过评阅老师成绩表 表头
    for row in range(3, debate_scores_sheet.max_row + 1):
        debate_score = DebateScoreModel()

        debate_score.id = debate_scores_sheet.cell(row, 1).value
        debate_score.student_number = debate_scores_sheet.cell(row, 2).value
        debate_score.student_name = debate_scores_sheet.cell(row, 3).value
        debate_score.major = debate_scores_sheet.cell(row, 4).value
        debate_score.thesis_topic = debate_scores_sheet.cell(row, 5).value
        # 分数
        # TODO: 优化分数读取存储方式
        score_1 = debate_scores_sheet.cell(row, 6).value
        score_2 = debate_scores_sheet.cell(row, 7).value
        score_3 = debate_scores_sheet.cell(row, 8).value
        score_4 = debate_scores_sheet.cell(row, 9).value
        score_5 = debate_scores_sheet.cell(row, 10).value
        scores = [
            0 if score_1 is None else int(score_1),
            0 if score_2 is None else int(score_2),
            0 if score_3 is None else int(score_3),
            0 if score_4 is None else int(score_4),
            0 if score_5 is None else int(score_5)
        ]
        debate_score.scores = scores
        debate_score.debate_group_leader_name = debate_scores_sheet.cell(row, 12).value
        debate_score.debate_group_secretary_name = debate_scores_sheet.cell(row, 13).value
        debate_score.debate_group_member = debate_scores_sheet.cell(row, 14).value
        # 测试
        # print(debate_score)
        debate_scores.append(debate_score)

    return debate_scores


def get_teacher_scores_data(workbook):
    """
    读 指导老师成绩 记录
    @param workbook: Excel工作簿对象
    @return: 指导老师成绩 记录
    """
    teacher_scores = []
    teacher_scores_sheet = workbook[TEACHER_SCORE_SHEET_NAME]

    # 跳过评阅老师成绩表 表头
    for row in range(3, teacher_scores_sheet.max_row + 1):
        teacher_score = TeacherScoreModel()

        teacher_score.id = teacher_scores_sheet.cell(row, 1).value
        teacher_score.student_number = teacher_scores_sheet.cell(row, 2).value
        teacher_score.student_name = teacher_scores_sheet.cell(row, 3).value
        teacher_score.major = teacher_scores_sheet.cell(row, 4).value
        teacher_score.thesis_topic = teacher_scores_sheet.cell(row, 5).value
        # 分数
        # TODO: 优化分数读取存储方式
        score_1 = teacher_scores_sheet.cell(row, 6).value
        score_2 = teacher_scores_sheet.cell(row, 7).value
        score_3 = teacher_scores_sheet.cell(row, 8).value
        score_4 = teacher_scores_sheet.cell(row, 9).value
        score_5 = teacher_scores_sheet.cell(row, 10).value
        score_6 = teacher_scores_sheet.cell(row, 11).value
        scores = [
            0 if score_1 is None else int(score_1),
            0 if score_2 is None else int(score_2),
            0 if score_3 is None else int(score_3),
            0 if score_4 is None else int(score_4),
            0 if score_5 is None else int(score_5),
            0 if score_6 is None else int(score_6),
        ]
        teacher_score.scores = scores
        teacher_score.guidance_teacher_name = teacher_scores_sheet.cell(row, 13).value
        teacher_score.guidance_teacher_work_number = teacher_scores_sheet.cell(row, 14).value
        # 测试
        # print(teacher_score)
        teacher_scores.append(teacher_score)

    return teacher_scores


def test():
    """
    测试方法
    @return: None
    """
    wb = get_workbook("D:\\Projects\\Python\\ThesisSummarizing\\template\\rating-information.xlsx")
    get_debate_scores_data(wb)
    get_teacher_scores_data(wb)
    get_debate_scores_data(wb)
    close_workbook(wb)


if __name__ == "__main__":
    test()
