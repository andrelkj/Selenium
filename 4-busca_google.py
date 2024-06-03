from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Especifique o caminho para o ChromeDriver
chrome_driver_path = '/usr/local/bin/chromedriver'


# 1 - Termo de pesquisa
term = input("Digite o que deseja pesquisar:\n")

# 2 - Iniciando o Driver
browser = webdriver.Chrome()
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
time.sleep(2)
results = browser.find_element(By.ID, "result-stats").text
print(f"Foram encontrados {results}")

# 6 - Retornando o Número de Páginas
qtd_results = int(
    results.split("Aproximadamente ")[1].split(" resultados")[0].replace(".", "")
)
tot_pages = qtd_results / 10
print(f"Número de páginas {int(tot_pages)}")

# # Page navigation does not apply to firefox once it loads the results in one page when scrolling down
# # 7 - Navegando entre páginas
# time.sleep(5)
# url_page = browser.find_element(By.XPATH, '//a[@aria-label="Page 2"]').get_attribute(
#     "href"
# )

# current_page = 0
# start = 10
# list_results = []

# while current_page <= 5:
#     if not current_page == 0:
#         url_page = url_page.replace(
#             "start=%s" % start,
#             "start=%s" % (start + 10),
#         )
#         start += 10
#     current_page += 1
#     browser.get(url_page)

# # 8 - Recuperando informações
#     divs = browser.find_elements(
#         By.XPATH,
#         '//div[@class="yuRUbf"]'
#     )
#     for div in divs:
#         name = div.find_element(By.TAG_NAME, 'h3')
#         link = div.find_element(By.TAG_NAME, 'a')
#         result = "%s,%s" %(name.text, link.get_attribute('href'))
#         print(result)
#         list_results.append(result)

# 9 - Salvando em arquivo txt
# with open('results_term.txt', 'w', encoding='utf-8') as file:
#     for result in list_results:
#         file.write("%s\n" %result)

# print(f'Foram encontrados {len(list_results)} resultados na pesquisa')
browser.quit()