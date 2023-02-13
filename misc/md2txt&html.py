# 本程序用于帮助规则书由md打包为txt和html文件，不是什么通用的格式转换工具，仅为自用。
# 当然如果您觉得此程序对您有用的话也可以拿去用用。
# 如果你只是《永恒之岛》的玩家，看不懂这个程序是什么，不用管它。
import markdown

def md2html(text: str):
    html = """<!--此文件由md2txt&html.py直接生成，格式不成体统-->
<!DOCTYPE html>
<html>
    <head>
        <title>永恒之岛规则书V1.0</title>
        <style>
            body {
                margin: 16px;
                background-color: rgb(245, 234, 218);
                font-family: Times, Arial, "微软雅黑", sans-serif;
                line-height: 24px;
            }
            
            h1,h2 { text-align: center; }
            
            p { text-indent: 32px; }
            
            pre {
                margin: 40px;
                border: 1px solid black;
                padding: 12px;
                background-color: rgb(245, 226, 199);
                font-family: unset
                font-size: 14px;
            }
        </style>
    </head>
    <body>
    {body}
    </body>
</html>"""
    body = ""
    preList = text.splite("```")
    f = lambda x : markdown.markdown(x)
    for i in range((len(preList) - 1) / 2):
        body += f(preList[i*2-1]) + "<pre>" + f(preList[i*2]) + "</pre>"
    body += preList[-1]

