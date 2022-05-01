#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   RatingModels.py
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      2022/4/28 15:54
@Description  Python version-3.10
TODO: 在CommonTools下创建不同类型的判空方法并使用
"""


class BaseRatingModel(object):
    """基础评分记录类"""
    # @property 与 @xx.setter 装饰器 的使用注意使用顺序与名称是否对应。
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
        self.__id = 0 if x is None else int(x)

    @property
    def student_number(self):
        return self.__student_number

    @student_number.setter
    def student_number(self, x):
        self.__student_number = '' if x is None else str(x)

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, x):
        self.__student_name = '' if x is None else str(x)

    @property
    def major(self):
        return self.__major

    @major.setter
    def major(self, x):
        self.__major = '' if x is None else str(x)

    @property
    def thesis_topic(self):
        return self.__thesis_topic

    @thesis_topic.setter
    def thesis_topic(self, x):
        self.__thesis_topic = '' if x is None else str(x)

    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def scores(self, x):
        self.__scores = [] if x is None else list(x)
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

    def __eq__(self, o: object) -> bool:
        """
        重写，以便 == 比较时用
        """
        return str(self.__student_number) == str(o.student_number)

    def __hash__(self) -> int:
        """
        重写，以便 set 集合用
        判断 是否同一人
        """
        return hash(str(self.__student_number))


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
        self.__review_teacher_name = '' if x is None else str(x)

    @property
    def review_teacher_work_number(self):
        return self.__review_teacher_work_number

    @review_teacher_work_number.setter
    def review_teacher_work_number(self, x):
        self.__review_teacher_work_number = '' if x is None else str(x)

    def __str__(self) -> str:
        return super().__str__() + f"review_teacher_name: {self.__review_teacher_name} review_teacher_work_number:{self.__review_teacher_work_number}";

    def __repr__(self) -> str:
        return self.__str__()


class DebateScoreModel(BaseRatingModel):
    """答辩评分记录类"""
    __slots__ = (
        # 答辩内容/答辩评语 - 字符串
        "__debate_content",
        # 答辩组长
        "__debate_group_leader_name",
        # 答辩组秘书 - 字符串
        "__debate_group_secretary_name",
        # 答辩组成员 - 字符串（不止一个人名组成的字符串）
        "__debate_group_member"
    )

    def __init__(self):
        super(DebateScoreModel, self).__init__()
        self.__debate_content = ''
        self.__debate_group_leader_name = ''
        self.__debate_group_secretary_name = ''
        self.__debate_group_member = ''

    @property
    def debate_content(self):
        return self.__debate_content

    @debate_content.setter
    def debate_content(self, x):
        self.__debate_content = '' if x is None else str(x)

    @property
    def debate_group_leader_name(self):
        return self.__debate_group_leader_name

    @debate_group_leader_name.setter
    def debate_group_leader_name(self, x):
        self.__debate_group_leader_name = '' if x is None else str(x)

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
        self.__debate_group_member = '' if x is None else str(x)

    def __str__(self) -> str:
        return super().__str__() + f"debate_group_content: {self.__debate_content} debate_group_leader_name: {self.__debate_group_leader_name} debate_group_secretary_name:{self.__debate_group_secretary_name} debate_group_member:{self.__debate_group_member}";

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
        super(TeacherScoreModel, self).__init__()
        self.__guidance_teacher_name = ''
        self.__guidance_teacher_work_number = ''

    @property
    def guidance_teacher_name(self):
        return self.__guidance_teacher_name

    @guidance_teacher_name.setter
    def guidance_teacher_name(self, x):
        self.__guidance_teacher_name = '' if x is None else str(x)

    @property
    def guidance_teacher_work_number(self):
        return self.__guidance_teacher_work_number

    @guidance_teacher_work_number.setter
    def guidance_teacher_work_number(self, x):
        self.__guidance_teacher_work_number = '' if x is None else str(x)

    def __str__(self) -> str:
        return super().__str__() + f"guidance_teacher_name: {self.__guidance_teacher_name} guidance_teacher_work_number:{self.__guidance_teacher_work_number}";

    def __repr__(self) -> str:
        return self.__str__()


class OutputModel(object):
    """输出实体模型 - 抽象为一个学生的不同评分记录"""
    __slots__ = (
        # 学号 - 字符串
        "__student_number",
        # 姓名
        "__student_name",
        # 指导老师姓名
        "__guidance_teacher_name",
        # 评阅评分记录
        "__comment_score_model",
        # 指导老师评分记录
        "__teacher_score_model",
        # 答辩评分记录
        "__debate_score_model"
    )

    def __init__(self):
        self.__student_number = ''
        self.__student_name = ''
        self.__guidance_teacher_name = ''
        self.__comment_score_model = None
        self.__teacher_score_model = None
        self.__debate_score_model = None

    @property
    def student_number(self):
        return self.__student_number

    @student_number.setter
    def student_number(self, x):
        self.__student_number = '' if x is None else str(x)

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, x):
        self.__student_name = '' if x is None else str(x)

    @property
    def guidance_teacher_name(self):
        return self.__guidance_teacher_name

    @guidance_teacher_name.setter
    def guidance_teacher_name(self, x):
        self.__guidance_teacher_name = '' if x is None else str(x)

    @property
    def comment_score_model(self):
        return self.__comment_score_model

    @comment_score_model.setter
    def comment_score_model(self, x):
        self.__comment_score_model = x

    @property
    def teacher_score_model(self):
        return self.__teacher_score_model

    @teacher_score_model.setter
    def teacher_score_model(self, x):
        self.__teacher_score_model = x

    @property
    def debate_score_model(self):
        return self.__debate_score_model

    @debate_score_model.setter
    def debate_score_model(self, x):
        self.__debate_score_model = x

    def __str__(self) -> str:
        return f"student_number: {self.__student_number} " \
               f"student_name: {self.__student_name} " \
               f"guidance_teacher_name: {self.__guidance_teacher_name} \n"\
               f"teacher_score_model: {self.__teacher_score_model} \n"\
               f"comment_score_model: {self.__comment_score_model} \n"\
               f"debate_score_model: {self.__debate_score_model}"

    def __repr__(self) -> str:
        return self.__str__()


def test():
    """
    测试方法
    @return: None
    """
    pass


if __name__ == "__main__":
    test()
