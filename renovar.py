from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from pynput.keyboard import Key, Controller
import getpass
import os

class main:		 #Inicia o programa
	print("Bem vindo ao Automatic Book Renwer...")

#Verificação da senha nos arquivos locais
from senha import checaSenha #Verifica se existe senha criada

class criaSenha:
if fh == 1:
	f = open(r'C:\Users\R430\Desktop\Script\identificacao.txt')
	login = f.readline(1)
	print (login + "\n")
	senha = f.readline(2)
	print (senha)
	f.close()

#Login e Senha
login =  input('Insira seu Login: ')
senha =  input('Insira sua senha: ')

#Adapter do Chrome
h = getpass.getuser()
dir = os.path.join(r'C:\Users\{}\Desktop\Script\drivers\chromedriver.exe'.format(h))
driver = webdriver.Chrome(r'C:\Users\{}\Desktop\Script\drivers\chromedriver.exe'.format(h))

#Abrir página
driver.set_page_load_timeout(25)
driver.maximize_window()
driver.get("http://sofia.fei.edu.br/pergamum/biblioteca_s/php/login_usu.php?flag=index.php")
time.sleep(12)
driver.find_element_by_id("id_login").click()

#Logar
keyboard = Controller()
keyboard.type(login)
keyboard.press(Key.tab)
keyboard.release(Key.tab)
keyboard.type(senha)
driver.find_element_by_id("button").click()
driver.set_page_load_timeout(30)

#Variável necessária para comparar data
driver.find_element_by_class_name(".txt_cinza_10").click(3)

#url = requests.get('http://sofia.fei.edu.br/pergamum/biblioteca/index.php')

#soup = BeautifulSoup(url.text, 'html.parser')

#with open('sb.txt' , 'w') as f:
#	for subreddit in soup.find_all('a'):
#		try:
#			if 'r' in subreddit.string:
#				f.write(subreddit.string[0:] + '\n')
#		except:
#				TypeError	

if __name__ = "__main__":
	main()