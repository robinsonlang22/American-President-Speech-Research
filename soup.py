import requests
from bs4 import BeautifulSoup
import json

# 获取网页内容
url = "https://www.presidency.ucsb.edu/advanced-search?field-keywords=China&field-keywords2=&field-keywords3=&from%5Bdate%5D=06-19-1980&to%5Bdate%5D=06-19-2024&person2=&items_per_page=25&page=2"
response = requests.get(url)
html_content = response.content

# 解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')

# 提取每个结果的详细信息
results = soup.select('.views-row')
data = []

for result in results:
    item = {}
    
    # 提取总统姓名
    president_name = result.select_one('.diet-title a')
    if president_name:
        item['president_name'] = president_name.text.strip()
    
    # 提取文档标题
    doc_title = result.select_one('.field-title a')
    if doc_title:
        item['doc_title'] = doc_title.text.strip()
        item['link'] = "https://www.presidency.ucsb.edu" + doc_title['href']
    
    # 提取日期
    date = result.select_one('.field-docs-start-date-time .date-display-single')
    if date:
        item['date'] = date.text.strip()
    
    # 提取文档内容
    content = result.select('.field-docs-content p')
    item['content'] = ' '.join([p.text.strip() for p in content])
    
    # 提取引用信息
    citation = result.select_one('.ucsbapp_citation')
    if citation:
        item['citation'] = citation.text.strip()
    
    data.append(item)

# 将数据写入json文件
with open('presidency_data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



