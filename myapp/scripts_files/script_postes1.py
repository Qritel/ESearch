#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import dateparser
import re

my_url = 'http://emploi-public.ma/fr/candidaturesListe.asp'

filename = "Postes_de_responsabilité/Services_de_l'Etat.csv"
f = open(filename, "w")
headers = " Id,\
            Administration organisatrice,\
            Nombre postes de chef de division,\
            Nombre postes de chef de service,\
            Dèlai dépôt,\
            Date publication,\
            Candidats convoqués,\
            Résultats,\
            Pour plus d'informations,\
            Fichiers attachés\n"
f.write(headers)

last_page = BeautifulSoup(uReq(my_url).read(), 'html.parser').findAll(
    'td', {'class': 'next'})[1].a['href'][11:]
for i in range(1, int(last_page) + 1):
    url = my_url + '?c=0&e=0&p=' + str(i)
    print("Processing.." + url)
    uClient = uReq(url)
    page_html = uClient.read()
    soup = BeautifulSoup(page_html, 'html.parser')
    table = soup.find('tbody')

    for row in table.findAll('tr'):
        liens1 = []
        cells = row.findAll('td')
        s = cells[0].a["href"]
        f.write("poste_e0id" + re.findall("(?<=id=)(\d+)", s)[0] + ",")
        for j in range(3):
            if j == 1 or j == 2:
                if len(cells[j].text.split()) == 2:
                    f.write(cells[j].text.split()[0] + ",")
                else:
                    f.write("0,")
            else:
                f.write("\"" + cells[j].text + "\",")
        for j in range(3, 5):
            try:
                f.write(str(dateparser.parse(cells[j].text).date()) + ",")
            except:
                f.write('1000-10-10' + ',')
        for j in range(5, 7):
            files = cells[j].findAll('a')
            if len(files) != 0:
                f.write("\"")
                for pdf in files:
                    f.write("http://emploi-public-files.ma/fichiers/upload/"
                            + pdf["href"][14:] + "|")
                    liens1.append("http://emploi-public-files.ma/fichiers/upload/"
                                  + pdf["href"][14:])
                f.write("\",")
            else:
                f.write('-' + ',')
        url_detail = "http://emploi-public.ma/fr/" + cells[0].a["href"]
        uClient = uReq(url_detail)
        page_html = uClient.read()
        soup = BeautifulSoup(page_html, 'html.parser')
        liens2 = []
        for tr in soup.find('tbody').findAll('tr'):
            if tr.th.text == 'Pour plus d\'informations :':
                f.write("\"" + tr.td.text.strip() + "\",")
            elif tr.th.text == 'Fichiers attachés :':
                for l in tr.td.ul.findAll('li'):
                    liens2.append("http://emploi-public-files.ma/fichiers/upload/" +
                                  l.a['href'][14:])
        liens3 = []
        for a in soup.find('div', {'class': 'list'}).findNext('div').findAll('a'):
            liens3.append("http://emploi-public-files.ma/fichiers/upload/" +
                          a['href'][14:])
        l = (set(liens2) | set(liens3)) - set(liens1)
        if len(l) != 0:
            f.write('|'.join(l))
            f.write("\n")
        else:
            f.write('-\n')

    uClient.close()

f.close()
