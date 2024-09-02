import requests
from bs4 import BeautifulSoup

# 获取网页内容
url = "https://www.presidency.ucsb.edu/documents/statement-signing-the-promoting-resolution-the-tibet-china-dispute-act"
response = requests.get(url)
html_content = response.content

# 解析HTML内容
soup = BeautifulSoup(html_content, 'html.parser')

# 提取总统姓名
president_name = soup.select_one('.diet-title a').text
print('President Name:', president_name)

# 提取总统信息
president_info = soup.select_one('.diet-by-line.president').text
print('President Info:', president_info)

# 提取文档标题
doc_title = soup.select_one('.field-ds-doc-title h1').text
print('Document Title:', doc_title)

# 提取日期
date = soup.select_one('.field-docs-start-date-time .date-display-single').text
print('Date:', date)

# 提取每个p标签的内容
p_tags = soup.select('.field-docs-content p')
for p in p_tags:
    print('Paragraph:', p.text.strip())

# 提取签名图片链接
signature_img = soup.select_one('.field-docs-content img')
if signature_img:
    signature_img_url = signature_img['src']
    print('Signature Image URL:', signature_img_url)
else:
    print('Signature Image URL: Not found')

# 提取引用信息
citation = soup.select_one('.ucsbapp_citation').text
print('Citation:', citation)
