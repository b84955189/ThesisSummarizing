
## 论文汇总


--------------

### 翻译


[简体中文](/b84955189/thesis-summarizing/blob/master/docs/README.zh-CN.md)

[English](/b84955189/thesis-summarizing/blob/master/README.md)

---------
### 介绍
使用Python实现论文评分信息的自动化处理。

基本任务:为每个学生不同的得分记录(Excel数据)生成特定格式的Word文件。Word模板文件需要由用户提供。
#### GUI
GUI文件是由Parth Jadhav的Tkinter Designer生成的。

> 仓库: [https://github.com/ParthJadhav/Tkinter-Designer](https://github.com/ParthJadhav/Tkinter-Designer)
##### 示例
![示例图片](/b84955189/thesis-summarizing/raw/master/docs/img/example.png)
#### 第三方模块
##### openpyxl
一个关于读写Excel文件的Python库。

>  文档：[https://openpyxl.readthedocs.io/](https://openpyxl.readthedocs.io/)

##### python-docx
 Python -docx是一个用于创建和更新Microsoft Word (.docx)文件的Python库。

>  文档:[https://python-docx.readthedocs.io/](https://python-docx.readthedocs.io)

### 打包
本项目的发行版使用[PyInstaller](https://pyinstaller.org)第三方库进行打包。本项目路径中提供了 示例打包配置文件。您可以通过将其修改为自己的项目路径来使用和打包它。

**pack-config-template.spec**
```
···
···
···
a = Analysis(['main.py',
'【Your project path】\\ThesisSummarizing\\func\\CommonTools.py',
'【Your project path】\\ThesisSummarizing\\func\\ExcelFunc.py',
'【Your project path】\\ThesisSummarizing\\func\\WordFunc.py',
'【Your project path】\\ThesisSummarizing\\gui\\gui.py',
'【Your project path】\\ThesisSummarizing\\model\\Config.py',
'【Your project path】\\ThesisSummarizing\\model\\EnumModels.py',
'【Your project path】\\ThesisSummarizing\\model\\ExceptionModels.py',
'【Your project path】\\ThesisSummarizing\\model\\RatingModels.py',
'【Your project path】\\ThesisSummarizing\\model\\ExceptionModels.py',
'【Your project path】\\ThesisSummarizing\\venv\\Lib\\site-packages\\openpyxl\\__init__.py',
'【Your project path】\\ThesisSummarizing\\venv\\Lib\\site-packages\\docx\\__init__.py'
],
···
···
···
```
**执行打包**
```
pyinstaller -i xx.ico pack-config-template.spec
```
### 联系
 - **作者**： Jason   
 - **邮箱**： lking@lking.icu
 - **博客**： [blog.lking.icu](https://blog.lking.icu)
 - **CSDN**： [https://blog.csdn.net/weixin_43670802](https://blog.csdn.net/weixin_43670802)
