from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 1 - Termo de pesquisa
term = input("Digite o que deseja pesquisar:\n")

# 2 - Iniciando o Driver
browser = webdriver.Firefox()
browser.get("https://www.google.com.br/")

# 3 - Encontrando o elemento
elem = browser.find_element(By.XPATH, "//textarea[@aria-label='Pesquisar']")

# 4 - Enviando termo para pesquisa

elem.send_keys(term)
elem.send_keys(Keys.ENTER)
