from selenium import webdriver 
# selenium 模块 http://selenium-python.readthedocs.org/
import os,time
# 缺少geckodriver执行程序 download 
# https://github.com/mozilla/geckodriver/releases 下载 然后配置环境变量即可
brower=webdriver.Firefox()
brower.get('http://inventwithpython.com/')
linkElem=brower.find_element_by_link_text('More Info')
# 自动点击某个按钮
linkElem.click()
# 提交表单
#brower.get('http://gmail.com')
#emailElem=brower.find_element_by_id('Email')
# emailElem.send_keys('example@gmail.com')
# pwElem=brower.find_element_by_id('Passwd')
#pwElem.send_keys('123456')
#pwElem.submit()

# 浏览器按钮
# 休眠五秒 刷新网页
time.sleep(5)
brower.refresh()
os.system('pause')
