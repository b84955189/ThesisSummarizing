#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
@File    :   gui.py    
@Contact :   lking@lking.icu
@Author :    Jason
@Date :      4/2/2022 4:33 PM
@Description  Python version-3.10
GUI界面
TODO: 重构冗余代码
TODO: 中英文语言统一化处理
"""
import time
import datetime
import webbrowser
from pathlib import Path

import tkinter.filedialog
import tkinter as tk
import threading

from func import ExcelFunc, CommonTools
from func.WordFunc import handle_output_model
from model.Config import Configs
from model.EnumModel import SheetType

ROOT_PATH = Path(__file__).parent.parent
ASSETS_PATH = ROOT_PATH / Path("./assets")
DEFAULT_OUTPUT_PATH = ROOT_PATH / Path("./out")
OFFSET_Y = -70
DEFAULT_TIME = datetime.datetime.now()

# 全局变量

# # 公共组件
window = ""
my_task_thread = ""
config = Configs()
generate_btn = ''
generate_btn_img = ''
processing_btn_img = ''

# # 路径
output_directory_path = ""
rating_excel_file_path = ""
comment_word_file_path = ""
debate_word_file_path = ""
teacher_word_file_path = ""

# # 评分数据Excel文件路径
rating_excel_file_path_entry = ""
# # 评阅成绩Word模板文件路径
comment_word_file_path_entry = ""
# 答辩成绩Word模板文件路径
debate_word_file_path_entry = ""
# 指导老师成绩Word模板文件路径
teacher_word_file_path_entry = ""
# 输出目录路径
output_path_entry = ""

# # 日期
year_time_entry = ""
month_time_entry = ""
day_time_entry = ""


def change_generate_button_state(sign, tips=None, box_type=1):
    """
    改变生成按钮状态
    True - 可用
    False - 不可用
    @param sign: 是否可用标志 - Boolean
    @param tips: 提示语
    @param box_type: 1 - 信息 2 - 错误  - int
    @return: None
    """
    if sign:
        generate_btn.config(image=generate_btn_img)
        generate_btn.config(state="normal")
    else:
        generate_btn.config(image=processing_btn_img)
        generate_btn.config(state="disable")
    if not CommonTools.is_empty_or_none(tips):
        match box_type:
            case 1:
                tk.messagebox.showinfo("Info", f"{tips}")
            case 2:
                tk.messagebox.showerror("Error", f"{tips}")


def my_task(rating_excel_path,
            comment_word_path,
            debate_word_path,
            teacher_word_path,
            template_key_year,
            template_key_month,
            template_key_day,
            output_path):
    """
    线程任务
    @param rating_excel_path: 评分数据Excel路径
    @param comment_word_path: 评阅老师成绩Word模板 路径
    @param debate_word_path: 答辩成绩Word模板 路径
    @param teacher_word_path: 指导老师成绩Word模板 路径
    @param template_key_day: 模板日期 - 年
    @param template_key_month: 模板日期 - 月
    @param template_key_year: 模板日期 - 日
    @param output_path: 输出目录
    @return: None
    """
    wb = None
    try:
        window.after(0, change_generate_button_state, False)
        # ---------------
        # 按 日期时间 生成子目录
        date_catalog = output_path / Path(
            f'./{datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d-%H%M%S")}')
        # 获取工作簿
        wb = ExcelFunc.get_workbook(rating_excel_path)
        comment_scores_sheet = wb[ExcelFunc.COMMENT_SCORE_SHEET_NAME]
        debate_scores_sheet = wb[ExcelFunc.DEBATE_SCORE_SHEET_NAME]
        teacher_scores_sheet = wb[ExcelFunc.TEACHER_SCORE_SHEET_NAME]
        # 生成Word
        for output_model in ExcelFunc.reorganization_data(
                ExcelFunc.get_data_from_sheet(debate_scores_sheet, SheetType.DEBATE_SCORES_SHEET),
                ExcelFunc.get_data_from_sheet(comment_scores_sheet, SheetType.COMMENT_SCORES_SHEET),
                ExcelFunc.get_data_from_sheet(teacher_scores_sheet, SheetType.TEACHER_SCORES_SHEET),
        ):
            output_model.comment_word_path = comment_word_path
            output_model.debate_word_path = debate_word_path
            output_model.teacher_word_path = teacher_word_path
            output_model.template_key_year = template_key_year
            output_model.template_key_month = template_key_month
            output_model.template_key_day = template_key_day
            # TODO: 删去多余字段
            output_model.output_directory_path = output_path

            handle_output_model(output_model, date_catalog)

        # ---------------
        window.after(0, change_generate_button_state, True, "Generate word file successfully!")
    except Exception as e:
        # 错误提示
        window.after(0, change_generate_button_state, True, "An error occurred, please try again!", 2)
        # dev
        print("错误：", e)
        pass
    finally:
        # 关闭数据信息工作簿
        if wb is not None:
            ExcelFunc.close_workbook(wb)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def btn_clicked():
    rating_excel_path = rating_excel_file_path_entry.get().strip()
    comment_word_path = comment_word_file_path_entry.get().strip()
    debate_word_path = debate_word_file_path_entry.get().strip()
    teacher_word_path = teacher_word_file_path_entry.get().strip()
    output_path = output_path_entry.get().strip()

    # 日期
    year_time = year_time_entry.get().strip()
    month_time = month_time_entry.get().strip()
    day_time = day_time_entry.get().strip()

    if CommonTools.is_empty_or_none(rating_excel_path):
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Rating Excel FileName.")
        return
    if CommonTools.is_empty_or_none(comment_word_path):
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Comment Word FileName.")
        return
    if CommonTools.is_empty_or_none(debate_word_path):
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Debate Word FileName.")
        return
    if CommonTools.is_empty_or_none(teacher_word_path):
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Teacher Word FileName.")
        return
    if CommonTools.is_empty_or_none(output_path):
        tk.messagebox.showerror(
            title="Invalid Path!", message="Enter a valid output path.")
        return

    if CommonTools.is_empty_or_none(year_time):
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Year.")
        return
    if CommonTools.is_empty_or_none(month_time):
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Month.")
        return
    if CommonTools.is_empty_or_none(day_time):
        tk.messagebox.showerror(
            title="Empty Fields!", message="Please enter Day.")
        return

    output = Path(output_path + "").expanduser().resolve()
    if output.exists() and not output.is_dir():
        tk.messagebox.showerror(
            "Exists!",
            f"{output} already exists and is not a directory.\n"
            "Enter a valid output directory.")
    elif output.exists() and output.is_dir() and tuple(output.glob('*')):
        response = tk.messagebox.askyesno(
            "Continue?",
            f"Directory {output} is not empty.\n"
            "Do you want to continue and overwrite?")
        if not response:
            return
    try:
        global my_task_thread
        # Check thread whether alive
        if isinstance(my_task_thread, threading.Thread) and my_task_thread.is_alive():
            tk.messagebox.showerror(
                "操作异常!", "请稍等任务处理完毕!")
        else:
            # creat a thread to operate long-time task.
            my_task_thread = threading.Thread(target=my_task,
                                              args=(rating_excel_path,
                                                    comment_word_path,
                                                    debate_word_path,
                                                    teacher_word_path,
                                                    year_time,
                                                    month_time,
                                                    day_time,
                                                    output),
                                              name="my_task_thread")
            # start thread
            my_task_thread.start()
            # wait this thread util it completes its task.
            # excel_task_thread.join()

    except Exception as e:
        print(e)
        tk.messagebox.showerror(
            "文件格式错误!", "请再次选择文件！")
        change_tips(config.default_welcome_tips)
    finally:
        pass


def select_out_path():
    global output_directory_path

    output_directory_path = tk.filedialog.askdirectory()
    output_path_entry.delete(0, tk.END)
    output_path_entry.insert(0, output_directory_path)


def select_rating_excel_file_path():
    global rating_excel_file_path

    rating_excel_file_path = tk.filedialog.askopenfilename()
    rating_excel_file_path_entry.delete(0, tk.END)
    rating_excel_file_path_entry.insert(0, rating_excel_file_path)


def select_comment_word_file_path():
    global comment_word_file_path

    comment_word_file_path = tk.filedialog.askopenfilename()
    comment_word_file_path_entry.delete(0, tk.END)
    comment_word_file_path_entry.insert(0, comment_word_file_path)


def select_debate_word_file_path():
    global debate_word_file_path

    debate_word_file_path = tk.filedialog.askopenfilename()
    debate_word_file_path_entry.delete(0, tk.END)
    debate_word_file_path_entry.insert(0, debate_word_file_path)


def select_teacher_word_file_path():
    global teacher_word_file_path

    teacher_word_file_path = tk.filedialog.askopenfilename()
    teacher_word_file_path_entry.delete(0, tk.END)
    teacher_word_file_path_entry.insert(0, teacher_word_file_path)


# UI thread is single thread !!! If there have a long-time task , everything of
# operation in UI thread will be blocked for a while.
def start():
    global window
    window = tk.Tk()
    logo = tk.PhotoImage(file=ASSETS_PATH / "icon.gif")
    window.call('wm', 'iconphoto', window._w, logo)
    window.title("Linyi University")

    window.geometry("862x519")
    window.configure(bg="#3A7FF6")
    canvas = tk.Canvas(
        window, bg="#3A7FF6", height=519, width=862,
        bd=0, highlightthickness=0, relief="ridge")
    canvas.place(x=0, y=0)
    canvas.create_rectangle(431, 0, 431 + 431, 0 + 519, fill="#FCFCFC", outline="")
    canvas.create_rectangle(40, 160, 40 + 60, 160 + 5, fill="#FCFCFC", outline="")

    text_box_bg = tk.PhotoImage(file=ASSETS_PATH / "TextBox_Bg.png")
    # 时间输入控件
    # # 年
    global year_time_entry
    year_time_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    year_time_entry.place(x=100 - 10, y=137 + 25 + 150 + 15, width=40.0, height=35)
    year_time_entry.focus()
    canvas.create_text(
        50 - 10, 137 + 40 + 150 + 15, text="YEAR:", fill="#FFF",
        font=("Arial-BoldMT", int(13.0)), anchor="w")
    year_time_entry.delete(0, tk.END)
    year_time_entry.insert(0, str(DEFAULT_TIME.year))
    # # 月
    global month_time_entry
    month_time_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    month_time_entry.place(x=207 - 10, y=137 + 25 + 150 + 15, width=40.0, height=35)
    canvas.create_text(
        150 - 10, 137 + 40 + 150 + 15, text="MONTH:", fill="#FFF",
        font=("Arial-BoldMT", int(13.0)), anchor="w")
    month_time_entry.delete(0, tk.END)
    month_time_entry.insert(0, str(DEFAULT_TIME.month))
    # # 日
    global day_time_entry
    day_time_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    day_time_entry.place(x=300 - 10, y=137 + 25 + 150 + 15, width=40.0, height=35)
    canvas.create_text(
        260 - 10, 137 + 40 + 150 + 15, text="DAY:", fill="#FFF",
        font=("Arial-BoldMT", int(13.0)), anchor="w")
    day_time_entry.delete(0, tk.END)
    day_time_entry.insert(0, str(DEFAULT_TIME.day))
    # rating Excel file path entry
    rating_excel_file_path_entry_img = canvas.create_image(650.5, 167.5 + OFFSET_Y - 5, image=text_box_bg)
    global rating_excel_file_path_entry
    rating_excel_file_path_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    rating_excel_file_path_entry.place(x=490.0, y=137 + 25 + OFFSET_Y - 5, width=321.0, height=35)
    rating_excel_file_path_picker_img = tk.PhotoImage(file=ASSETS_PATH / "path_picker.png")
    rating_excel_file_path_picker_button = tk.Button(
        image=rating_excel_file_path_picker_img,
        text='',
        compound='center',
        fg='white',
        borderwidth=0,
        highlightthickness=0,
        command=select_rating_excel_file_path,
        relief='flat')

    rating_excel_file_path_picker_button.place(
        x=783, y=160 + OFFSET_Y - 5,
        width=24,
        height=22)
    canvas.create_text(
        490.0, 150.0 + OFFSET_Y - 5, text="Select Rating Excel File", fill="#515486",
        font=("Arial-BoldMT", int(13.0)), anchor="w")

    # comment word file path entry
    comment_word_file_path_entry_img = canvas.create_image(650.5, 167.5 + OFFSET_Y + 70, image=text_box_bg)
    global comment_word_file_path_entry
    comment_word_file_path_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    comment_word_file_path_entry.place(x=490.0, y=137 + 25 + OFFSET_Y + 70, width=321.0, height=35)
    comment_word_file_path_picker_img = tk.PhotoImage(file=ASSETS_PATH / "path_picker.png")
    comment_word_file_path_picker_button = tk.Button(
        image=comment_word_file_path_picker_img,
        text='',
        compound='center',
        fg='white',
        borderwidth=0,
        highlightthickness=0,
        command=select_comment_word_file_path,
        relief='flat')

    comment_word_file_path_picker_button.place(
        x=783, y=160 + OFFSET_Y + 70,
        width=24,
        height=22)
    canvas.create_text(
        490.0, 150.0 + OFFSET_Y + 70, text="Select Comment Word Template", fill="#515486",
        font=("Arial-BoldMT", int(13.0)), anchor="w")

    # debate word file path entry
    global debate_word_file_path_entry
    teacher_info_file_path_entry_img = canvas.create_image(650.5, 167.5 + OFFSET_Y + 50 + 100, image=text_box_bg)
    debate_word_file_path_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    debate_word_file_path_entry.place(x=490.0, y=137 + 25 + OFFSET_Y + 50 + 100, width=321.0, height=35)
    debate_word_file_path_picker_img = tk.PhotoImage(file=ASSETS_PATH / "path_picker.png")
    debate_word_file_path_picker_button = tk.Button(
        image=debate_word_file_path_picker_img,
        text='',
        compound='center',
        fg='white',
        borderwidth=0,
        highlightthickness=0,
        command=select_debate_word_file_path,
        relief='flat')

    debate_word_file_path_picker_button.place(
        x=783, y=160 + OFFSET_Y + 50 + 100,
        width=24,
        height=22)
    canvas.create_text(
        490.0, 150.0 + OFFSET_Y + 50 + 100, text="Select Debate Word Template", fill="#515486",
        font=("Arial-BoldMT", int(13.0)), anchor="w")
    # teacher word file path entry
    global teacher_word_file_path_entry
    data_file_path_entry_img = canvas.create_image(650.5, 167.5 + OFFSET_Y + 140 + 90, image=text_box_bg)
    teacher_word_file_path_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    teacher_word_file_path_entry.place(x=490.0, y=137 + 25 + OFFSET_Y + 140 + 90, width=321.0, height=35)
    teacher_word_file_path_picker_img = tk.PhotoImage(file=ASSETS_PATH / "path_picker.png")
    teacher_word_file_path_picker_button = tk.Button(
        image=teacher_word_file_path_picker_img,
        text='',
        compound='center',
        fg='white',
        borderwidth=0,
        highlightthickness=0,
        command=select_teacher_word_file_path,
        relief='flat')

    teacher_word_file_path_picker_button.place(
        x=783, y=160 + OFFSET_Y + 140 + 90,
        width=24,
        height=22)
    canvas.create_text(
        490.0, 150.0 + OFFSET_Y + 140 + 90, text="Select Teacher Word Template", fill="#515486",
        font=("Arial-BoldMT", int(13.0)), anchor="w")
    # output directory entry
    global output_path_entry
    output_path_entry_img = canvas.create_image(650.5, 329.5 + 70 + 70 + OFFSET_Y, image=text_box_bg)
    output_path_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
    output_path_entry.place(x=490.0, y=299 + 25 + 70 + 70 + OFFSET_Y, width=321.0, height=35)
    out_path_picker_img = tk.PhotoImage(file=ASSETS_PATH / "path_picker.png")
    out_path_picker_button = tk.Button(
        image=out_path_picker_img,
        text='',
        compound='center',
        fg='white',
        borderwidth=0,
        highlightthickness=0,
        command=select_out_path,
        relief='flat')
    out_path_picker_button.place(
        x=783, y=319 + 70 + 70 + OFFSET_Y,
        width=24,
        height=22)
    canvas.create_text(
        490.0, 315.5 + 70 + 70 + OFFSET_Y, text="Select Output Directory",
        fill="#515486", font=("Arial-BoldMT", int(13.0)), anchor="w")

    canvas.create_text(
        646.5, 428.5, text="Generate",
        fill="#FFFFFF", font=("Arial-BoldMT", int(13.0)))
    canvas.create_text(
        573.5, 30, text="Enter the details.",
        fill="#515486", font=("Arial-BoldMT", int(22.0)))

    title = tk.Label(
        text="Welcome to Linyi University", bg="#3A7FF6",
        fg="white", font=("Arial-BoldMT", int(20.0)))
    title.place(x=27.0, y=120.0)

    info_text = tk.Label(
        text="Linyi University also known as LYU\n"
             "is located in Linyi City,\n"
             "Shandong Province.",
        bg="#3A7FF6", fg="white", justify="left",
        font=("Georgia", int(16.0)))

    info_text.place(x=27.0, y=200.0)

    know_more_university = tk.Label(
        text="Click here for further information.",
        bg="#3A7FF6", fg="white", cursor="hand2")
    know_more_university.place(x=27, y=400)
    know_more_university.bind('<Button-1>', lambda event: webbrowser.open_new_tab('"https://www.lyu.edu.cn/"'))

    # Author
    author_info = tk.Label(
        text="© LKING.ICU",
        bg="#3A7FF6", fg="white", cursor="hand2")
    author_info.place(x=27, y=425)
    author_info.bind('<Button-1>', lambda event: webbrowser.open_new_tab('https://blog.lking.icu'))
    global generate_btn
    global generate_btn_img
    global processing_btn_img
    generate_btn_img = tk.PhotoImage(file=ASSETS_PATH / "generate.png")
    processing_btn_img = tk.PhotoImage(file=ASSETS_PATH / "processing.png")
    generate_btn = tk.Button(
        image=generate_btn_img, borderwidth=0, highlightthickness=0,
        command=btn_clicked, relief="flat")
    generate_btn.place(x=557, y=401 + 50, width=180, height=55)
    window.resizable(False, False)
    window.mainloop()


if __name__ == "__main__":
    # q = Queue()
    # print(ASSETS_PATH)
    start()
