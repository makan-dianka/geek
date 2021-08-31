import requests
from bs4 import BeautifulSoup

url = 'https://www.ofpra.gouv.fr/fr/asile/la-procedure-de-demande-d-asile/demander-l-asile-en-france'
resp = requests.get(url)

soup = BeautifulSoup(resp.text, 'lxml')
finder_h_one = soup.find('div', class_='desc-res')
finder = soup.find_all('div', class_='finder_h_one')
compte = len(finder)
h_one = finder_h_one

print(h_one.text)
print(compte)