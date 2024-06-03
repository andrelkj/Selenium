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

# 5 - Retornando a Qtd de Registros
time.sleep(2)
tools = browser.find_element(By.XPATH, "//div[@role='button' and text()='Ferramentas']")
tools.click()
results = browser.find_element(By.ID, "result-stats").text
print(f"Foram encontrados {results}")

# 6 - Retornando o Número de Páginas
qtd_results = int(
    results.split("Aproximadamente ")[1].split(" resultados")[0].replace(".", "")
)
tot_pages = qtd_results / 10
print(f"Número de páginas {int(tot_pages)}")

browser.quit()
