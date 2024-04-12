import csv
import re

# 打开原始文本文件
with open('master_formatted_1023.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# 使用正则表达式找到所有的Instruction和Response
# 这里假设每个Response后面跟着至少一个换行符作为分隔
pattern = re.compile(r'Instruction: (.*?)\nResponse: (.*?)(?=\n\n|\Z)', re.S)
matches = pattern.findall(content)

# 创建新的CSV文件并写入数据
with open('convertedQA.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    # 写入表头
    writer.writerow(['Instruction', 'Response'])
    # 写入数据
    for match in matches:
        # 移除可能的多余换行符
        instruction, response = match[0].strip(), match[1].strip()
        writer.writerow([instruction, response])
