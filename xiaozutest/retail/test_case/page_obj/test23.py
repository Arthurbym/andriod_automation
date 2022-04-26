from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()

driver.set_window_position(100,0)