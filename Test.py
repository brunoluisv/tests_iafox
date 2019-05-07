# -*- coding: utf-8 -*-
from selenium import webdriver as wd
from selenium.webdriver.firefox.options import Options
import time
import allure

def test_setup():
    #time.sleep(120)
    options = Options()
    options.headless = True
    global driver
    driver = wd.Firefox(options=options)
    #driver = wd.Firefox()
    driver.get('https://demo1.test.iafox.com')
    time.sleep(2)

def test_login():
    if "Login no IAFOX" == driver.title:
        print("TITULO VALIDO = " + driver.title)
        driver.save_screenshot('pics/tela_login.png')
        allure.attach.file('pics/tela_login.png', attachment_type=allure.attachment_type.PNG)
    else:
        print("TITULO INVALIDO = " + driver.title)
        driver.close()

    user = driver.find_element_by_name("j_username")
    user.clear()
    user.send_keys("suporte@iafox.com")
    passwd = driver.find_element_by_name("j_password")
    passwd.clear()
    passwd.send_keys("4321")
    login = driver.find_element_by_id("ctlForm")
    login.click()
    print("TESTE DE LOGIN OK")
    time.sleep(1)
    driver.save_screenshot('pics/tela_inicial.png')
    allure.attach.file('pics/tela_inicial.png', attachment_type=allure.attachment_type.PNG)

def test_cadastros():
    cadastro = driver.find_element_by_xpath("//div[contains(text(), 'Cadastros')]")
    cadastro.click()
    time.sleep(1)
    driver.save_screenshot('pics/tela_cadastros.png')
    allure.attach.file('pics/tela_cadastros.png', attachment_type=allure.attachment_type.PNG)
    
def test_moldes():
    driver.get('https://demo1.test.iafox.com/')
    cadastro = driver.find_element_by_xpath("//div[contains(text(), 'Cadastros')]")
    cadastro.click()
    moldes = driver.find_element_by_xpath("//div[@class='mblListItemLabel'][contains(text(),'Molde')]")
    time.sleep(1)
    moldes.click()
    time.sleep(1)
    print("Moldes OK")
    driver.save_screenshot('pics/tela_moldes.png')
    allure.attach.file('pics/tela_moldes.png', attachment_type=allure.attachment_type.PNG)

def test_produtos():
    driver.get('https://demo1.test.iafox.com/')
    cadastro = driver.find_element_by_xpath("//div[contains(text(), 'Cadastros')]")
    cadastro.click()
    produtos = driver.find_element_by_xpath("//div[contains(text(),'Produto')]")
    time.sleep(1)
    produtos.click()
    print("Produtos OK")
    time.sleep(1)
    driver.save_screenshot('pics/tela_produtos.png')
    allure.attach.file('pics/tela_produtos.png', attachment_type=allure.attachment_type.PNG)

def test_familias():
    driver.get('https://demo1.test.iafox.com/')
    cadastro = driver.find_element_by_xpath("//div[contains(text(), 'Cadastros')]")
    cadastro.click()
    familias = driver.find_element_by_xpath("//div[contains(text(),'Família')]")
    time.sleep(1)
    familias.click()
    print("Familias OK")
    time.sleep(1)
    driver.save_screenshot('pics/tela_familias.png')
    allure.attach.file('pics/tela_familias.png', attachment_type=allure.attachment_type.PNG)

def test_etiquetas():
    driver.get('https://demo1.test.iafox.com/')
    cadastro = driver.find_element_by_xpath("//div[contains(text(), 'Cadastros')]")
    cadastro.click()
    etiquetas = driver.find_element_by_xpath("//div[contains(text(),'Etiquetas')]")
    time.sleep(1)
    etiquetas.click()
    print("Etiquetas OK")
    time.sleep(1)
    driver.save_screenshot('pics/tela_etiquetas.png')
    allure.attach.file('pics/tela_etiquetas.png', attachment_type=allure.attachment_type.PNG)

def test_logout():
    driver.get('https://demo1.test.iafox.com/')
    time.sleep(2)
    logout = driver.find_element_by_xpath("//div[contains(text(), 'suporte@iafox.com')]")
    logout.click()
    logout = driver.find_element_by_xpath("/html/body/div/button")
    logout.click()
    time.sleep(1)
    driver.get('https://demo1.test.iafox.com')
    print("TESTE DE LOGOUT OK")

def test_teardown():
    time.sleep(2)
    driver.close()
    driver.quit()
    print("TESTE COMPLETED")
