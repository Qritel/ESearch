#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import dateparser
import re

my_url = 'http://emploi-public.ma/fr/emploiSuperieursListe.asp'

filename = "Emplois_supérieurs/Emplois.csv"
f = open(filename, "w")
headers = " Id,\
            Emploi,\
            Autorité Gouvernementale,\
            Arrêté,\
            Date limite de dépot des candidatures,\
            Date de publication,\
            Pour plus d'informations,\
            Fichiers attachés\n"
f.write(headers)

last_page = BeautifulSoup(uReq(my_url).read(), 'html.parser').findAll(
    'td', {'class': 'next'})[1].a['href'][3:]
for i in range(1, int(last_page) + 1):
    url = my_url + '?p=' + str(i)
    print("Processing.." + url)
    uClient = uReq(url)
    page_html = uClient.read()
    soup = BeautifulSoup(page_html, 'html.parser')
    table = soup.find('tbody')

    for row in table.findAll('tr'):
        liens1 = []
        cells = row.findAll('td')
        s = cells[0].a["href"]
        f.write("emploi_" + re.findall("(?<=id=)(\d+)", s)[0] + ",")

        for j in range(2):
            f.write("\"" + cells[j].text + "\",")

        f.write("\"http://emploi-public-files.ma/fichiers/upload/"
                + cells[2].a["href"][14:] + "\",")
        liens1.append("http://emploi-public-files.ma/fichiers/upload/"
                      + cells[2].a["href"][14:])
        try:
            f.write("\"" + str(dateparser.parse(cells[3].text[:len(cells[3].text) - len(cells[3].td.text)]).date())
                    + "\",")
        except:
            f.write('1000-10-10' + ',')
        f.write("\"" + str(dateparser.parse(cells[4].text).date()) + "\",")
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
