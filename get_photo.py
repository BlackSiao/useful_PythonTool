import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://tieba.baidu.com/p/9472435013'

# 获取网页内容
def GetHtml(url):
    try:
        html = requests.get(url)
        html.raise_for_status()  # 检查是否成功获取
        return html.text
    except requests.RequestException as e:
        print(f"Error getting HTML: {e}")
        return None

# 获取并下载图片
def GetImg(html):
    if not html:   # 请求网页失败就返回
        return
    # 请求网页成功就继续执行
    soup = BeautifulSoup(html, 'html.parser')
    imglist = []

    # 获取所有图片链接（注意：有时图片使用的是 data-src 属性）
    for photourl in soup.find_all('img', class_='BDE_Image'):
        imgurl = photourl.get('data-src') or photourl.get('src')
        if imgurl:
            imglist.append(urljoin(url, imgurl))  # 处理相对路径

    # 如果图片下载目录不存在，则创建
    download_dir = 'D:\photos'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # 下载图片
    x = 0
    for imgurl in imglist:
        try:
            img_data = requests.get(imgurl).content
            with open(f'{download_dir}{x}.jpg', 'wb') as file:
                file.write(img_data)
            print(f"Downloaded {x}.jpg")
            x += 1
        except requests.RequestException as e:
            print(f"Error downloading image {imgurl}: {e}")


# 主程序入口
if __name__ == '__main__':
    html = GetHtml(url)
    GetImg(html)
