import os
import time

import selenium
from selenium import webdriver
from datetime import datetime
from selenium.webdriver import ChromeOptions

image_path = 'images'  # 图片保存路径
if not os.path.exists(image_path):
	os.makedirs(image_path)



# 定义一个函数，用于将网页渲染后的内容保存为图片
def save_webpage_as_image(url, image_path):
    # 开启无头模式
    option = ChromeOptions()
    option.add_argument('--headless')

    driver = webdriver.Chrome(options=option)  # 使用Chrome浏览器
    driver.implicitly_wait(5) # 隐式等待5秒
    driver.get(url)
    driver.maximize_window()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')  # 当前时间戳
    image_name = f'webpage_{timestamp}.png'
    driver.get_screenshot_as_file(f'{image_path}/{image_name}')


    # 使用定时任务调用函数，每隔5分钟保存一次网页渲染后的内容
while True:
    try:
        save_webpage_as_image('https://list.jd.com/list.html?cat=1318,12099,9756', image_path)
        save_webpage_as_image('https://www.google.com/finance;?hl=zh', image_path)
        time.sleep(300)  # 等待5分钟
    except selenium.common.exceptions.WebDriverException:
        print('超时！')