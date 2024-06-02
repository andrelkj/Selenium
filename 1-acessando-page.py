from selenium import webdriver

# 1 - Utilizando o WebDriver
browser = webdriver.Firefox()

browser.get('http://www.amazon.com.br')
browser.quit()