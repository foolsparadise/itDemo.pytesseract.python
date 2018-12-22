## 文字识别Demo之Python版Tesseract(Google)  

## 安装(Mac系统环境)
```
brew install tesseract
brew list tesseract
```
安装tesseract，并打印
```
/usr/local/Cellar/tesseract/4.0.0/bin/tesseract
/usr/local/Cellar/tesseract/4.0.0/include/tesseract/ (20 files)
/usr/local/Cellar/tesseract/4.0.0/lib/libtesseract.4.dylib
/usr/local/Cellar/tesseract/4.0.0/lib/pkgconfig/tesseract.pc
/usr/local/Cellar/tesseract/4.0.0/lib/ (2 other files)
/usr/local/Cellar/tesseract/4.0.0/share/tessdata/ (32 files)
```
在 https://github.com/tesseract-ocr/tessdata 下载语言包，比如简体中文，就是文件 chi_sim_vert.traineddata 和 chi_sim.traineddata， 复制到 /usr/local/Cellar/tesseract/4.0.0/share/tessdata/ 目录下  
然后安装pytesseract  
```

Installing via pip:
Check the pytesseract package page for more information.
$ (env)> pip install pytesseract
Or if you have git installed:
$ (env)> pip install -U git+https://github.com/madmaze/pytesseract.git
Installing from source:
$> git clone https://github.com/madmaze/pytesseract.git
$ (env)> cd pytesseract && pip install -U .
```
## 运行
```
python pytesseractDemo.py
```

