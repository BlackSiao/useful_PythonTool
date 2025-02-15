# 这个是用来学习如何使用Selenium的

import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 创建 WebDriver 对象
wd = webdriver.Chrome()

# 每隔半秒就查看是否有该元素出现，最久等10s
wd.implicitly_wait(10)

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
url = 'https://tieba.baidu.com/p/9496592832'
wd.get(url)

# 根据id选择元素，返回的就是该元素对应的WebElement对象
elements = wd.find_elements(By.CSS_SELECTOR, '.BDE_Image')

# 确保目标保存路径存在
save_dir = r'D:\BlackSiao\python\photos'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 通过该 WebElement对象，获取图片的 URL，并保存到指定路径
for index, example in enumerate(elements):
    img_url = example.get_attribute('src')  # 获取图片的 src 属性

    if img_url:  # 如果 img_url 存在
        try:
            # 请求图片并获取内容
            img_data = requests.get(img_url).content

            # 保存图片到本地路径
            img_name = os.path.join(save_dir, f'image_{index + 1}.jpg')
            with open(img_name, 'wb') as file:
                file.write(img_data)
            print(f"已保存图片: {img_name}")
        except Exception as e:
            print(f"下载图片时出错: {e}")

# 等待一下，确保页面加载完成
sleep(10)

# 退出浏览器
wd.quit()
