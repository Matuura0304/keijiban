#!/usr/bin/python3
# 0L01021
import cgi
import datetime
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
html = """Content-type: text/html

<html lang="ja-jp">
<head>
<title>掲示板</title>
<meta charset="utf-8">
<link rel="stylesheet" href="./style.css">
</head>
<body>
<div class='header'>
    <h2>掲示板</h2>
    <form action="index.py" method="POST">
        <input type="text" name="text" placeholder="入力" />
        <input type="submit" name="submit" />
    </form>
</div>
<br>
<br>
</body>
</html>"""

file_name = 'data.txt'

form = cgi.FieldStorage()
text = form.getvalue('text','')
now = datetime.datetime.now()
now = now.strftime('%Y年 %m月%d日 %H:%M ')
now = str(now)

if len(text) != 0:
    with open(file_name, mode='a') as f:
        f.write('a' + '\n' + now + text)
else:
    pass

with open(file_name) as f:
    text1 = f.read().replace("\n","<hr>")

text1 = text1.split("a")
text1 = text1[::-1]
text1 = " ".join(text1)
print(html, text1)