from selenium import webdriver

class selenium():
    def login(self,url):
        driver.get(url)
    def search(self,content):
        driver.find_element_by_id('kw').send_keys(content)


driver = webdriver.Chrome()
selenium().login("http://www.baidu.com")
selenium().search('selenium3')