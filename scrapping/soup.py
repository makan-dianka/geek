import requests
from bs4 import BeautifulSoup as bs

url = "http://www.cnda.fr/Demarches-et-procedures/Roles-de-lecture-Decisions"
req = requests.get(url)

links = []
pdf_links = []

def getpage():
    soup = bs(req.text, "html.parser")
    
    div_Class = soup.find_all("div", class_="positionnement")[1]
    divPAGE = div_Class.find("div", id="cnt")
    
    div_ID = divPAGE.find("div", id="readspeaker")
    div_PAGETXT = div_ID.find("div", id="pagetxt")
    div_PAGECHAPO = div_ID.find("div", id="pagechapo")
    
    print()
    print(div_PAGECHAPO.text)
    print(div_ID.h1.text)
    
    for p in div_PAGETXT.find_all('p'):
        try:
            a = p.a
            links.append(a["href"])
        except:
            pass
        
    
    for h2 in div_PAGETXT.find_all("h2"):
        print(h2.text)
        
getpage()    

def getlink():
    print()
    print("\nredirect 2 :\nurl >> "+links[1])
    geturl = requests.get(links[1])
    soup = bs(geturl.text, "html.parser")
    title = soup.find('title')
    print("title >> "+title.text)
    
    div_Class = soup.find_all("div", class_="positionnement")[1]
    divPAGE = div_Class.find("div", id="cnt")
    
    div_ID = divPAGE.find("div", id="readspeaker")
    div_PAGETXT = div_ID.find("div", id="pagetxt")
    div_PAGECHAPO = div_ID.find("div", id="pagechapo")
    print(div_ID.h1.text)
    
    for ALL_p in div_PAGETXT.find_all("p"):
        try:
            pdf_link = ALL_p.a["href"]
            pdf_links.append(pdf_link)
        except:
            pass
getlink()

def savefile():
    print("redirect :\n>> "+pdf_links[15])
    r = requests.get(pdf_links[15])
    with open("cnda_s16.pdf", "wb") as file_pdf:
        file_pdf.write(r.content)
        print("File saved !")