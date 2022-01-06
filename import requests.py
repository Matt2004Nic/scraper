import requests
import json
import numpy as np
import pandas as pd
from selectorlib import Extractor 
from time import sleep
import random

# prende tutti gli indirizzi ip di saddy e li carica in y
response=requests.get("https://proxy.webshare.io/api/proxy/list/?page=1", headers={"Authorization":"4a12ecda825c37f598dc9d3ffad4da1193505e72"}).json()
jDump = json.dumps(response)
jLoad = json.loads(jDump)

# carica dal jLoad i risultati (quello che contiene tutte le cose che ci servono)
results=jLoad["results"]
DFrameResults=pd.DataFrame.from_dict(results, orient='columns', dtype=None, columns=None)

# prendere le porte http
ports = DFrameResults["ports"]
portsHTTP = []
for x in range(len(ports)):
    a = ports[x]
    portsHTTP.append(a.get("http"))

# prendere gli ip
variousIPs = DFrameResults["proxy_address"]

# unione di ip e porte
sockets = []
for x in range(len(portsHTTP)):
    sockets.append((str(variousIPs[x]) + ":" + str(portsHTTP[x])))

def scrape(url):  

    headers = {
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.amazon.it/',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'accept': 'test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    }
    s = requests.Session()
    s.auth = ('user', 'pass')
    dai=True
    s.headers.update(headers)
    proxies = {'https://': random.choice(sockets)}
    while dai == True:
        proxies = {'https://': random.choice(sockets)}
        print("Downloading %s"%url)
        r = s.get(url, headers=headers,proxies=proxies)
        if r.status_code > 500:
            if "To discuss automated access to Amazon data please contact" in r.text:
                print("Page %s was blocked by Amazon. Please try using better proxies\n"%url)
                return None
        else:
                dai = False
    print(proxies)
    #print(r.text)

    return e.extract(r.text)
    
x=1
template = {'products': None}
template2 = {'seller': None}

#while true:
indexCose = ["url", "search_url", "nomevenditore", "nomespedizione", "urlvenditore", "prezzo", "costospedizione", "recensionevenditore", "numerorecensionevenditore", "title", "img", "recensioneprodotto", "numerorecensioneprodotto"]

with open("urls.txt",'r') as urllist, open('search_results_output.jsonl','w') as outfile:
    for url in urllist.read().splitlines():
        for y in range(1):
            '''alul = True
            urla = url + "&page=" + str(x)
            #print("url=",urla)
            e = Extractor.from_yaml_file('selectors.yml')
            while alul==True:
                data = scrape(urla) 
                if data != template:
                    alul = False
                
            if data:
                for product in data['products']:
                    product['search_url'] = url
                    url2 = product['url']
                    urla2 = "https://www.amazon.it" + url2
                    alul2 = True
                    contselector=0
                    e = Extractor.from_yaml_file('selectorsnuovoousato.yml')
                    while alul2==True:
                        conterror=0
                        data2 = scrape(urla2) 
                        if conterror < 5:
                            if data2['seller'] != None:
                                #print("data2 ",data2)
                                if data2['seller']['nomevenditore'] == None or data2['seller']['nomevenditore'] =="":
                                    data2['seller']['nomevenditore'] = "Amazon"
                                if data2['seller']['nomespedizione'] == None or data2['seller']['nomespedizione'] == "":
                                    data2['seller']['nomespedizione'] = "Amazon"
                                product.update(data2['seller'])
                                if data2['seller']['urlvenditore'] != None:
                                    urla3 = "https://www.amazon.it" + data2['seller']['urlvenditore']
                                    e = Extractor.from_yaml_file('selectorsvenditore.yml')
                                    alul3=False
                                    while alul3==True:
                                        venditore = scrape(urla3) 
                                        if venditore != None:
                                            print(venditore)
                                            alul3=False
                                    try:
                                        if venditore['recensioneseller'] != None:
                                            product.update(venditore['recensioneseller'])
                                    except:
                                        e = Extractor.from_yaml_file('selectorsnuovoeusato.yml')

                                    #print("venditore ", venditore)
                                alul2 = False
                            if data2['product'] != None:
                                product.update(data2['product'])
                                alul2 = False
                        else:
                            if contselector < 4:
                                e = Extractor.from_yaml_file('selectorsnuovoeusato.yml')
                            else:
                                alul2 = False
                        contselector+=1
                        conterror+=1
                    json.dump(product,outfile)
                    outfile.write("\n")'''
            alul = True
            urla = url + "&page=" + str(x)
            e = Extractor.from_yaml_file('selectors.yml')
            while alul==True:
                
                data = scrape(urla) 
                if data != template:
                    alul = False
                
            if data:
                for product in data['products']:
                    product['search_url'] = url
                    linkfinitoprodotto = product['url']
                    linkfinitoprodotto = "https://www.amazon.it" + linkfinitoprodotto
                    alul2 = True
                    contselector=0
                    e = Extractor.from_yaml_file('selectorsnuovoousato.yml')
                    try:
                        while alul2==True:
                            conterror=0
                            data2 = scrape(linkfinitoprodotto) 
                            data2['seller']
                            if data2['seller']['prezzo'] != None:
                                if data2['seller']['nomevenditore'] == None or data2['seller']['nomevenditore'] =="":
                                    data2['seller']['nomevenditore'] = "Amazon"
                                if data2['seller']['nomespedizione'] == None or data2['seller']['nomespedizione'] == "":
                                    data2['seller']['nomespedizione'] = "Amazon"
                                product.update(data2['seller'])
                                if data2['seller']['urlvenditore'] != None and (data2['seller']['nomevenditore'] != "Amazon Warehouse" or data2['seller']['nomevenditore'] != "Amazon"):
                                    urla3 = "https://www.amazon.it" + data2['seller']['urlvenditore']
                                    e = Extractor.from_yaml_file('selectorsvenditore.yml')
                                    alul3=True
                                    while alul3==True:
                                        venditore = scrape(urla3) 
                                        if venditore['recensioneseller'] != None:
                                            print(venditore)
                                            alul3=False
                                            product.update(venditore['recensioneseller'])  
                            json.dump(product,outfile)
                            outfile.write("\n")
                            alul2=False        
                    except Exception as ee:
                        print(ee)
                        e = Extractor.from_yaml_file('selectorsnuovoeusato.yml')

                        try:
                            while alul2==True:
                                conterror=0
                                data2 = scrape(linkfinitoprodotto) 
                                product2 = product
                                data2['seller']['venditorenuovo']
                                if data2['seller']['venditorenuovo']['prezzo'] != None:
                                    if data2['seller']['venditorenuovo']['nomevenditore'] == None or data2['seller']['venditorenuovo']['nomevenditore'] =="":
                                        data2['seller']['venditorenuovo']['nomevenditore'] = "Amazon"
                                    if data2['seller']['venditorenuovo']['nomespedizione'] == None or data2['seller']['venditorenuovo']['nomespedizione'] == "":
                                        data2['seller']['venditorenuovo']['nomespedizione'] = "Amazon"
                                    product.update(data2['seller']['venditorenuovo'])
                                    if data2['seller']['venditorenuovo']['urlvenditore'] != None and (data2['seller']['venditorenuovo']['nomevenditore'] != "Amazon Warehouse" or data2['seller']['venditorenuovo']['nomevenditore'] != "Amazon"):
                                        urla3 = "https://www.amazon.it" + data2['seller']['venditorenuovo']['urlvenditore']
                                        e = Extractor.from_yaml_file('selectorsvenditore.yml')
                                        alul3=True
                                        while alul3==True:
                                            venditore = scrape(urla3) 
                                            if venditore['recensioneseller'] != None:
                                                print(venditore)
                                                alul3=False
                                                product.update(venditore['recensioneseller'])  
                                json.dump(product,outfile)
                                outfile.write("\n")
                                alul2=False  
                                data2['seller']['venditoreusato']
                                if data2['seller']['venditoreusato']['prezzo'] != None:
                                    if data2['seller']['venditoreusato']['nomevenditore'] == None or data2['seller']['venditoreusato']['nomevenditore'] =="":
                                        data2['seller']['venditoreusato']['nomevenditore'] = "Amazon"
                                    if data2['seller']['venditoreusato']['nomespedizione'] == None or data2['seller']['venditoreusato']['nomespedizione'] == "":
                                        data2['seller']['venditoreusato']['nomespedizione'] = "Amazon"
                                    product2.update(data2['seller']['venditoreusato'])
                                    if data2['seller']['venditoreusato']['urlvenditore'] != None and (data2['seller']['venditoreusato']['nomevenditore'] != "Amazon Warehouse" or data2['seller']['venditoreusato']['nomevenditore'] != "Amazon"):
                                        urla3 = "https://www.amazon.it" + data2['seller']['venditoreusato']['urlvenditore']
                                        e = Extractor.from_yaml_file('selectorsvenditore.yml')
                                        alul3=True
                                        while alul3==True:
                                            venditore = scrape(urla3) 
                                            if venditore['recensioneseller'] != None:
                                                print(venditore)
                                                alul3=False
                                                product2.update(venditore['recensioneseller'])  
                                json.dump(product2,outfile)
                                outfile.write("\n")
                                alul2=False  
                        except Exception as eee: 
                            print(eee)
                            contselector+=1
                            if contselector >5:
                                alul2=False    


                            

            x+=1
            url[:-1]
        x=1
prova = pd.read_json('search_results_output.jsonl', lines=True)
prova.head(20)
