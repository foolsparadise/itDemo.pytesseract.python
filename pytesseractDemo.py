# -*- coding: utf-8 -*-

# @Author  : github.com/foolsparadise
# @Time    : 2018-12-20 18:18:19 
# @desc    : 
# @usage   : python pytesseractDemo.py

from PIL import Image
import os
import pytesseract
# tesseract/4.0.0
# https://github.com/tesseract-ocr/tesseract/wiki
# https://github.com/tesseract-ocr/tessdata
# https://github.com/madmaze/pytesseract

# 图片
img = Image.open("./screenshot.png")
# 识别范围
question = img.crop((0, 0, 600, 400))
# tesseract 路径
pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract/4.0.0/bin/tesseract'
# 语言包目录
tessdata_dir_config = '--tessdata-dir "/usr/local/Cellar/tesseract/4.0.0/share/tessdata"'
# lang 指定中文简体
text = pytesseract.image_to_string(question, lang='chi_sim', config=tessdata_dir_config)
text = text.replace(" ", "")[2:]
# 打印
print(text)

