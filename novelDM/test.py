import requests
import parsel

url = 'http://www.xbiquzw.com/1_1245/603352.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
selector = parsel.Selector(response.text)  # 获取小说章节名字
chapter_title = selector.xpath('//div[@class="bookname"]/h1/text()').extract_first()
# 获取小说章节内容
content = '\n'.join(selector.css('#content::text').getall())
# content = selector.xpath('//div[@id="content"]').extract()
# content = '\n'.join(content)
# print(chapter_title)
# print(type(content))
print(content)
# print(content.replace('<br><br>',''))
