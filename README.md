# Python-selenium3（自动化测试）
##### 1、解决“selenium.common.exceptions.SessionNotCreatedException: Message: Unable to find a matching set of capabilities“

selenium 启动firefox浏览器时，报错：selenium.common.exceptions.SessionN otCreatedException:   Message: Unable to find a matching set of capabilities

原因：如果出现如上信息，说明firefox浏览器版本和浏览器驱动版本不匹配。

解决方法：
1.更换较低版本geckodriver驱动，下载链接 https://github.com/mozilla/geckodriver/releases
2.将驱动压缩包解压，将geckodriver.exe 放在python和火狐浏览器安装目录下 //这两个目录都已经添加至环境变量。
3.重启浏览器，运行python脚本启动浏览器。



成功运行的环境:
firefox：65.0.1
chrome：72.0.1
python：3.7
selenium：3.1.4.0              
geckodriver：v0.24.0         下载地址：https://github.com/mozilla/geckodriver/releases
chromedriver：v2.46	   下载地址：http://npm.taobao.org/mirrors/chromedriver/2.46/



#####	2、使用selenium登录126邮箱定位失败原因-报错：selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="auto-id-"]

原因：此id是动态id，每次刷新http://www.126.com页面该值都会变话。因此找不到对应元素。网易用了iframe框架，需要先定位到iframe框架，才能找到内部的元素.

但是iframe的ID也是随机生成，name为空，所以需要找到iframe这个元素才能定位

```
#找到iframe
iframe=driver.find_element_by_xpath("//*[@id='loginDiv']/iframe")
#切换到iframe
driver.switch_to.frame(iframe)
```

定位前建议加延时，防止页面未加载完成去寻找，导致错误。

