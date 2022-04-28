#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   RatingModels.py
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/4/28 15:54
@Description  Python version-3.10

"""


class BaseRatingModel(object):
    """基础评分记录类"""
    __slots__ = (
        # 序号
        "__id",
        # 学号 - 字符串
        "__student_number",
        # 姓名
        "__student_name",
        # 专业
        "__major",
        # 题目
        "__thesis_topic",
        # 得分 - list集合
        "__scores",
        # 合计（总分）
        "__total_score"
    )

    def __init__(self):
        self.__id = 0
        self.__student_number = ''
        self.__student_name = ''
        self.__major = ''
        self.__thesis_topic = ''
        self.__scores = []
        self.__total_score = sum(self.__scores)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, x):
        self.__id = int(x)

    @property
    def student_number(self):
        return self.__student_number

    @student_number.setter
    def student_number(self, x):
        self.__student_number = str(x)

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, x):
        self.__student_name = str(x)

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, x):
        self.__major = str(x)

    @property
    def thesis_topic(self):
        return self.__thesis_topic

    @thesis_topic.setter
    def thesis_topic(self, x):
        self.__thesis_topic = str(x)

    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def scores(self, x):
        self.__scores = list(x)
        self.__total_score = sum(self.__scores)

    @property
    def total_score(self):
        return self.__total_score

    # @total_score.setter
    # def total_score(self, x):
    #     self.__thesis_topic = x

    def __str__(self) -> str:
        return f"id:{self.__id} student_number:{self.__student_number} student_name:{self.__student_name} major:{self.__major} thesis_topic:{self.__thesis_topic} scores:{self.__scores} total_score:{self.__total_score} "

    def __repr__(self) -> str:
        return self.__str__()


class CommentScoreModel(BaseRatingModel):
    """评阅评分记录类"""
    __slots__ = (
        # 评阅老师
        "__review_teacher_name",
        # 评阅老师工号 - 字符串
        "__review_teacher_work_number"
    )

    def __init__(self):
        super(CommentScoreModel, self).__init__()
        self.__review_teacher_name = ''
        self.__review_teacher_work_number = ''

    @property
    def review_teacher_name(self):
        return self.__review_teacher_name

    @review_teacher_name.setter
    def review_teacher_name(self, x):
        self.__review_teacher_name = str(x)

    @property
    def review_teacher_work_number(self):
        return self.__review_teacher_work_number

    @review_teacher_work_number.setter
    def review_teacher_work_number(self, x):
        self.__review_teacher_work_number = str(x)

    def __str__(self) -> str:
        return super().__str__() + f"review_teacher_name: {self.__review_teacher_name} review_teacher_work_number:{self.__review_teacher_work_number}";

    def __repr__(self) -> str:
        return self.__str__()


class DebateScoreModel(BaseRatingModel):
    """答辩评分记录类"""
    __slots__ = (
        # 答辩组长
        "__debate_group_leader_name",
        # 答辩组秘书 - 字符串
        "__debate_group_secretary_name",
        # 答辩组成员 - 字符串（不止一个人名组成的字符串）
        "__debate_group_member"
    )

    def __init__(self):
        super(DebateScoreModel, self).__init__()
        self.__debate_group_leader_name = ''
        self.__debate_group_secretary_name = ''
        self.__debate_group_member = ''

    @property
    def debate_group_leader_name(self):
        return self.__debate_group_leader_name

    @debate_group_leader_name.setter
    def debate_group_leader_name(self, x):
        self.__debate_group_leader_name = str(x)

    @property
    def debate_group_secretary_name(self):
        return self.__debate_group_secretary_name

    @debate_group_secretary_name.setter
    def debate_group_secretary_name(self, x):
        self.__debate_group_secretary_name = str(x)

    @property
    def debate_group_member(self):
        return self.__debate_group_member

    @debate_group_member.setter
    def debate_group_member(self, x):
        self.__debate_group_member = str(x)

    def __str__(self) -> str:
        return super().__str__() + f"debate_group_leader_name: {self.__debate_group_leader_name} debate_group_secretary_name:{self.__debate_group_secretary_name} debate_group_member:{self.__debate_group_member}";

    def __repr__(self) -> str:
        return self.__str__()


class TeacherScoreModel(BaseRatingModel):
    """指导老师评分记录类"""
    __slots__ = (
        # 指导老师
        "__guidance_teacher_name",
        # 指导老师工号
        "__guidance_teacher_work_number"
    )

    def __init__(self):
        super(DebateScoreModel, self).__init__()
        self.__guidance_teacher_name = ''
        self.__guidance_teacher_work_number = ''

    @property
    def guidance_teacher_name(self):
        return self.__guidance_teacher_name

    @guidance_teacher_name.setter
    def guidance_teacher_name(self, x):
        self.__guidance_teacher_name = str(x)

    @property
    def guidance_teacher_work_number(self):
        return self.__guidance_teacher_work_number

    @guidance_teacher_work_number.setter
    def guidance_teacher_work_number(self, x):
        self.__guidance_teacher_work_number = str(x)

    def __str__(self) -> str:
        return super().__str__() + f"guidance_teacher_name: {self.__guidance_teacher_name} guidance_teacher_work_number:{self.__guidance_teacher_work_number}";

    def __repr__(self) -> str:
        return self.__str__()


def test():
    """
    测试方法
    @return: None
    """
    params = [1, '201809090001', '张三', '计科', '微信小程序的打法水电费打法的设计', [20, 30, 20, 8, 7, 6], 'Jason', '001']
    params_2 = [1, '201809090001', '张三', '计科', '微信小程序的打法水电费打法的设计', [20, 30, 20, 8, 7, 6], 'Jason', '001']
    params_3 = [1, '201809090001', '张三', '计科', '微信小程序的打法水电费打法的设计', [20, 30, 20, 8, 7, 6], 'Jason', 'FeiFei', 'Auro,Jack,HuJian']
    a = CommentScoreModel()

    # a.id = params[0]
    # a.student_number = params[1]
    # a.student_name = params[2]
    # a.major = params[3]
    # a.thesis_topic = params[4]
    # a.scores = params[5]
    # a.review_teacher_name = params[6]
    # a.review_teacher_work_number = params[7]
    #
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
