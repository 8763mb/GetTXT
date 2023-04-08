import re
import pandas as pd

#定義檔案變數
originalfile = 'D:\\DNACL.txt'
outputfile = 'D:\\DNACL.html'

#使用open含式打開檔案，r是代表僅讀取
with open(originalfile, 'r', encoding='utf-8') as txt:
    content = txt.read()

# 將前面的content分割檔案
rules = re.findall(r"set name \"(\S+)\"[\s\S]+?set srcaddr \"(\S+)\"[\s\S]+?set dstaddr \"(\S+)\"[\s\S]+?set action (\S+)[\s\S]+?set service \"(\S+)\"", content)


# 將資料轉換為表格格式
df = pd.DataFrame(rules, columns=['name', 'srcaddr', 'dstaddr', 'action', 'service'])


# 建立標頭
html = df.to_html(index=False)

#使用open寫入資料，w代表寫入
with open(outputfile , 'w', encoding='utf-8') as f:
    f.write(html)
