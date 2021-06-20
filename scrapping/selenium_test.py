from selenium import webdriver
import time
import requests

# path = 'C:\webdrivers\chromedriver.exe'

driver = webdriver.Chrome()   
driver.get('http://makandianka.pythonanywhere.com')

title = driver.title
current_url = driver.current_url

print(f'\n Titre: {title} --> Url: {current_url}')
print()
driver.find_element_by_link_text('G-F').click()

username= " " #username 
password = " " #password

User = driver.find_element_by_name('username')
User.send_keys(username)

Ps = driver.find_element_by_name('password')
Ps.send_keys(password)

btn = driver.find_element_by_class_name('login_btn')
btn.click()

title = driver.title
current_url = driver.current_url
driver.get(current_url)

print(f'\n Titre: {title} --> Url: {current_url}')
print()
driver.find_element_by_link_text('MALI').click()

title = driver.title
current_url = driver.current_url
print()
print(f'\n Titre: {title} --> Url: {current_url}')

# driver.close --> fermeture de l'onglet courant
# driver.quit() --> fermeture de toutes les onglets