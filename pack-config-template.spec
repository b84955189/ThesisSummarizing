# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['main.py',
'【你的项目绝对路径】\\ThesisSummarizing\\func\\CommonTools.py',
'【你的项目绝对路径】\\ThesisSummarizing\\func\\ExcelFunc.py',
'【你的项目绝对路径】\\ThesisSummarizing\\func\\WordFunc.py',
'【你的项目绝对路径】\\ThesisSummarizing\\gui\\gui.py',
'【你的项目绝对路径】\\ThesisSummarizing\\model\\Config.py',
'【你的项目绝对路径】\\ThesisSummarizing\\model\\EnumModels.py',
'【你的项目绝对路径】\\ThesisSummarizing\\model\\ExceptionModels.py',
'【你的项目绝对路径】\\ThesisSummarizing\\model\\RatingModels.py',
'【你的项目绝对路径】\\ThesisSummarizing\\model\\ExceptionModels.py',
'【你的项目绝对路径】\\ThesisSummarizing\\venv\\Lib\\site-packages\\openpyxl\\__init__.py',
'【你的项目绝对路径】\\ThesisSummarizing\\venv\\Lib\\site-packages\\docx\\__init__.py'
],
             pathex=[],
             binaries=[],
             datas=[('assets', 'assets')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='ThesisSummarizing',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
