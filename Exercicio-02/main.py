# Crie um programa com selenium que
# 1 - Jogue o jogo
# 2 - Quando você ganhar o script deve parar de ser executado
# url: https://curso-python-selenium.netlify.app/exercicio_02.html

from selenium.webdriver import Firefox
import time

browser = Firefox()
browser.get("https://curso-python-selenium.netlify.app/exercicio_02.html")
time.sleep(1)
ancora = browser.find_element_by_id('ancora')
result = ""
while 1:
    ancora.click()
    tags_p = browser.find_elements_by_tag_name('p')
    if "Você ganhou:" in tags_p[-1].text:
        result = tags_p[-1].text
        break

print(result)
browser.close()
