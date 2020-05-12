# Gere um dicionário, onde a chave é a tag h1
# ○ O valor deve ser um novo dicionário
# ○ cada chave do valor deverá ser o valor de 'atributo'
# ○ cada valor deve ser o texto contido no elemento
# url = https://curso-python-selenium.netlify.app/exercicio_01.html
from selenium.webdriver import Firefox
import time

browser = Firefox()
browser.get("https://curso-python-selenium.netlify.app/exercicio_01.html")

time.sleep(1)

h1 = browser.find_element_by_tag_name('h1').text
tagsP = browser.find_elements_by_tag_name('p')
data = {h1: {}}

for p in tagsP:
    data[h1].update({p.get_attribute('atributo'): p.text})

print(data)
browser.close()
