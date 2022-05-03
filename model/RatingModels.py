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
    """输出实体模型 - 抽象为一个学生的不同评分记录，并附加输出参数"""
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
        "__debate_score_model",
        # 输出参数
        # # 评阅成绩Word模板 路径 - 字符串
        "__comment_word_path",
        # # 答辩成绩Word模板 路径 - 字符串
        "__debate_word_path",
        # # 指导老师成绩Word模板 路径 - 字符串
        "__teacher_word_path",
        # # 输出目录 路径 - 字符串
        "__output_directory_path",
        # # Word模板 日期关键字 - 年
        "__template_key_year",
        # # Word模板 日期关键字 - 月
        "__template_key_month",
        # # Word模板 日期关键字 - 日
        "__template_key_day"
    )

    def __init__(self):
        self.__student_number = ''
        self.__student_name = ''
        self.__guidance_teacher_name = ''
        self.__comment_score_model = None
        self.__teacher_score_model = None
        self.__debate_score_model = None

        self.__comment_word_path = ''
        self.__debate_word_path = ''
        self.__teacher_word_path = ''
        self.__output_directory_path = ''
        self.__template_key_year = ''
        self.__template_key_month = ''
        self.__template_key_day = ''

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

    @property
    def comment_word_path(self):
        return self.__comment_word_path

    @comment_word_path.setter
    def comment_word_path(self, x):
        self.__comment_word_path = x

    @property
    def debate_word_path(self):
        return self.__debate_word_path

    @debate_word_path.setter
    def debate_word_path(self, x):
        self.__debate_word_path = x

    @property
    def teacher_word_path(self):
        return self.__teacher_word_path

    @teacher_word_path.setter
    def teacher_word_path(self, x):
        self.__teacher_word_path = x

    @property
    def output_directory_path(self):
        return self.__output_directory_path

    @output_directory_path.setter
    def output_directory_path(self, x):
        self.__output_directory_path = x

    @property
    def template_key_year(self):
        return self.__template_key_year

    @template_key_year.setter
    def template_key_year(self, x):
        self.__template_key_year = x

    @property
    def template_key_month(self):
        return self.__template_key_month

    @template_key_month.setter
    def template_key_month(self, x):
        self.__template_key_month = x

    @property
    def template_key_day(self):
        return self.__template_key_day

    @template_key_day.setter
    def template_key_day(self, x):
        self.__template_key_day = x

    def __str__(self) -> str:
        return f"student_number: {self.__student_number} " \
               f"student_name: {self.__student_name} " \
               f"guidance_teacher_name: {self.__guidance_teacher_name} \n" \
               f"teacher_score_model: {self.__teacher_score_model} \n" \
               f"comment_score_model: {self.__comment_score_model} \n" \
               f"debate_score_model: {self.__debate_score_model} \n" \
               f"comment_word_path: {self.__comment_word_path} \n" \
               f"debate_word_path: {self.__debate_word_path} \n" \
               f"teacher_word_path: {self.__teacher_word_path} \n" \
               f"output_directory_path: {self.__output_directory_path} \n" \
               f"template_key_year: {self.__template_key_year} \n" \
               f"template_key_month: {self.__template_key_month} \n" \
               f"template_key_day: {self.__template_key_day} \n"

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
