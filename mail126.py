from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
def login():
    #执行邮箱登录
    # iframe=driver.find_element_by_xpath("//*[@id='loginDiv']/iframe")
    # driver.switch_to.frame(iframe)
    iframe = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,"//*[@id='loginDiv']/iframe")))
    driver.switch_to.frame(iframe)
    element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.NAME,"email")))
    element.send_keys('chenjiayizzz@126.com')
    # driver.find_element_by_name('email').clear()
    # driver.find_element_by_name('email').send_keys('chenjiayizzz@126.com')
    driver.find_element_by_name('password').clear()
    driver.find_element_by_name('password').send_keys('cjy123..')
    driver.find_element_by_id('dologin').click()
    time.sleep(3)
def logout():
    driver.find_element_by_link_text("退出").click()
    driver.quit()

driver = webdriver.Chrome()
driver.get("http://www.126.com")
time.sleep(2)
print('Before login===============')
title = driver.title;print(title)#打印当前页面title
now_url = driver.current_url;print(now_url)#打印当前页面URL
login()#登录
print('After login===============')
title = driver.title;print(title)#再次打印当前页面title
now_url = driver.current_url;print(now_url)#打印当前页面URL
#获得登录用户名
user = driver.find_element_by_id('spnUid').text
print(user)

# logout()#退出
