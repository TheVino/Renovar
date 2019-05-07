from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pynput.keyboard import Key, Controller
import getpass
import os
import time
import requests

h = getpass.getuser()
dir = os.path.join(r'C:\Users\{}\Desktop\Script\drivers\chromedriver_win32\chromedriver.exe'.format(h))
driver = webdriver.Chrome(dir) # Lembrando que este driver deve estar adicionado ao PATH para poder ser executado
driver.set_page_load_timeout(50)
driver.maximize_window()
driver.get("http://sofia.fei.edu.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php")
time.sleep(12)
driver.find_element_by_id("id_login").send_keys("121152888")
driver.find_element_by_id("id_senhaLogin").send_keys("2469")
driver.find_element_by_id("button").click()
time.sleep(15)

# qtdeLivros = driver.find_elements_by_xpath('//*[@id="Accordion1"]')
# print (qtdeLivros)

#print ("**********")
#for x in qtdeLivros:
#	print (x)

renove = driver.find_elements_by_css_selector("#txt_cinza_10")
for x in renove:
	print (renove)


#Analisar como identificar cada botão de renovação individualmente

# Caso encontre algum livro prestes a vencer
## driver.find_element_by_class_name("btn_renovar").click() #Analisar como identificar cada botão de renovar individualmente, pois o site é um lixo e nomeia exatamente todos iguais
## driver.find_element_by_id("btn_gravar4").click() #Irá votlar p/ pg inicial após renovar o empréstimo
# <input type="button" name="btn_gravar4" value="Back" class="btn_voltar" id="btn_gravar4" onclick="javascript:jumpBack();">

#Caso o empréstimo ainda esteja dentro da data de validade, página irá forcener um valor abaixo informando. Utilizar informações desta classe para informar ao usuário o feedbak.
#<td width="320" class="box_vermelho_left">Renovação Cancelada. Exemplar já está renovado. (PT)</td>


#driver.close()
#driver.quit()
#https://www.youtube.com/watch?v=BURK7wMcCwU

#                           DATA                               ||            BOTÃO RENOVAR
# //*[@id="Accordion1"]/div[1]/div[2]/table/tbody/tr[2]/td[3]  || //*[@id="botao_renovar1"]/center/input

# //*[@id="Accordion1"]/div[1]/div[2]/table/tbody/tr[3]/td[3]  || //*[@id="botao_renovar2"]/center/input