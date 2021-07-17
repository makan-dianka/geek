import requests
import time
import sys
from bs4 import BeautifulSoup

line = 0


def google_research(url):
    session = requests.Session()
    try:
        res = session.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        return soup
    except requests.exceptions.MissingSchema:
        pass

keyword = input("\n\t\t\t\t\t google research :\nquit: q, z, c \n>> ".upper())
if keyword.lower() in ["q", "z", "c"]:
    sys.exit()
url = "http://google.com/search?q="+keyword
google = google_research(url)

class_principal = google.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')[:4]
class_principal1 = google.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')[4:5]
class_principal2 = google.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')[5:6]
class_principal3 = google.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')[6:7]
class_principal4 = google.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')[7:8]
class_principal5 = google.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')[8:9]
class_principal6 = google.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')[9:10]
class_principal7 = google.find_all('div', class_='ZINbbc xpd O9g5cc uUPGi')[10:11]

print(f"\n\t\tgoogle results for : {keyword}".upper())

def google_resultats():
    global line
    for i in class_principal:
        for p in i.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
            line += 1
            print("GOOGLE Line "+str([line]))
            try:
                links = i.a["href"]
                link_sa = links.split("=")
                link = link_sa[1].split("&")
                print(i.h3.text.upper())
                print(p.text)
                print(link[0])
                print("--"*50)
                print()
                time.sleep(2)
                break
            except:
                pass

google_resultats()


def google_resultats1(s):
    if s.lower() == "":
        global line
        for i in class_principal1:
            for p in i.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
                line += 1
                print("GOOGLE Line "+str([line]))
                try:
                    links = i.a["href"]
                    link_sa = links.split("=")
                    link = link_sa[1].split("&")
                    print(i.h3.text.upper())
                    print(p.text)
                    print(link[0])
                    print("--"*50)
                    print()
                    break
                except:
                    pass
    else:
        try:
            url = input("link >> ")
            site = google_research(url)
            title = site.find("title")
            print(title.text.upper())
            time.sleep(1)
            for body in site.find_all("p"): 
                print(body.text.strip())
                print("--"*60)
                time.sleep(0.5)
        except AttributeError:
            print("invalid url".upper())
        
print("Page suivante\nCliquez sur le boutton [entrer] pour la line suivante - OU - \nCliquez sur n'import quel autre boutton pour suivre un lien\nCliquez q, z, c pour quiter")
suivant = input()
if suivant.lower() in ["q", "z", "c"]:
    sys.exit()
google_resultats1(suivant)


def google_resultats2(s):
    if s.lower() == "":
        global line
        for i in class_principal2:
            for p in i.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
                line += 1
                print("GOOGLE Line "+str([line]))
                try:
                    links = i.a["href"]
                    link_sa = links.split("=")
                    link = link_sa[1].split("&")
                    print(i.h3.text.upper())
                    print(p.text)
                    print(link[0])
                    print("--"*50)
                    print()
                    break
                except:
                    pass
    else:
        try:
            url = input("link >> ")
            site = google_research(url)
            title = site.find("title")
            print(title.text.upper())
            time.sleep(1)
            for body in site.find_all("p"): 
                print(body.text.strip())
                print("--"*60)
                time.sleep(0.5)
        except AttributeError:
            print("invalid url".upper())
suivant = input()
if suivant.lower() in ["q", "z", "c"]:
    sys.exit()
google_resultats2(suivant)


def google_resultats3(s):
    if s.lower() == "":
        global line
        for i in class_principal3:
            for p in i.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
                line += 1
                print("GOOGLE Line "+str([line]))
                try:
                    links = i.a["href"]
                    link_sa = links.split("=")
                    link = link_sa[1].split("&")
                    print(i.h3.text.upper())
                    print(p.text)
                    print(link[0])
                    print("--"*50)
                    print()
                    break
                except:
                    pass
    else:
        try:
            url = input("link >> ")
            site = google_research(url)
            title = site.find("title")
            print(title.text.upper())
            time.sleep(1)
            for body in site.find_all("p"): 
                print(body.text.strip())
                print("--"*60)
                time.sleep(0.5)
        except AttributeError:
            print("invalid url".upper())
suivant = input()
if suivant.lower() in ["q", "z", "c"]:
    sys.exit()
google_resultats3(suivant)


def google_resultats4(s):
    if s.lower() == "":
        global line
        for i in class_principal4:
            for p in i.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
                line += 1
                print("GOOGLE Line "+str([line]))
                try:
                    links = i.a["href"]
                    link_sa = links.split("=")
                    link = link_sa[1].split("&")
                    print(i.h3.text.upper())
                    print(p.text)
                    print(link[0])
                    print("--"*50)
                    print()
                    break
                except:
                    pass
    else:
        try:
            url = input("link >> ")
            site = google_research(url)
            title = site.find("title")
            print(title.text.upper())
            time.sleep(1)
            for body in site.find_all("p"): 
                print(body.text.strip())
                print("--"*60)
                time.sleep(0.5)
        except AttributeError:
            print("invalid url".upper())
suivant = input()
if suivant.lower() in ["q", "z", "c"]:
    sys.exit()
google_resultats4(suivant)


def google_resultats5(s):
    if s.lower() == "":
        global line
        for i in class_principal5:
            for p in i.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
                line += 1
                print("GOOGLE Line "+str([line]))
                try:
                    links = i.a["href"]
                    link_sa = links.split("=")
                    link = link_sa[1].split("&")
                    print(i.h3.text.upper())
                    print(p.text)
                    print(link[0])
                    print("--"*50)
                    print()
                    break
                except:
                    pass
    else:
        try:
            url = input("link >> ")
            site = google_research(url)
            title = site.find("title")
            print(title.text.upper())
            time.sleep(1)
            for body in site.find_all("p"): 
                print(body.text.strip())
                print("--"*60)
                time.sleep(0.5)
        except AttributeError:
            print("invalid url".upper())
suivant = input()
if suivant.lower() in ["q", "z", "c"]:
    sys.exit()
google_resultats5(suivant)

def google_resultats6(s):
    if s.lower() == "":
        global line
        for i in class_principal6:
            for p in i.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
                line += 1
                print("GOOGLE Line "+str([line]))
                try:
                    links = i.a["href"]
                    link_sa = links.split("=")
                    link = link_sa[1].split("&")
                    print(i.h3.text.upper())
                    print(p.text)
                    print(link[0])
                    print("--"*50)
                    print()
                    break
                except:
                    pass
    else:
        try:
            url = input("link >> ")
            site = google_research(url)
            title = site.find("title")
            print(title.text.upper())
            time.sleep(1)
            for body in site.find_all("p"): 
                print(body.text.strip())
                print("--"*60)
                time.sleep(0.5)
        except AttributeError:
            print("invalid url".upper())
suivant = input()
if suivant.lower() in ["q", "z", "c"]:
    sys.exit()
google_resultats6(suivant)

def google_resultats7(s):
    if s.lower() == "":
        global line
        for i in class_principal7:
            for p in i.find_all("div", class_="BNeawe s3v9rd AP7Wnd"):
                line += 1
                print("GOOGLE Line "+str([line]))
                try:
                    links = i.a["href"]
                    link_sa = links.split("=")
                    link = link_sa[1].split("&")
                    print(i.h3.text.upper())
                    print(p.text)
                    print(link[0])
                    print("--"*50)
                    print()
                    break
                except:
                    pass
    else:
        try:
            url = input("link >> ")
            site = google_research(url)
            title = site.find("title")
            print(title.text.upper())
            time.sleep(1)
            for body in site.find_all("p"): 
                print(body.text.strip())
                print("--"*60)
                time.sleep(0.5)
        except AttributeError:
            print("invalid url".upper())
suivant = input()
if suivant.lower() in ["q", "z", "c"]:
    sys.exit()
google_resultats7(suivant)