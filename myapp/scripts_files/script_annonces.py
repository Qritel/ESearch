#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import dateparser
import re

my_url = 'http://emploi-public.ma/fr/'

filename = "annonces.csv"
f = open(filename, "w")
headers = "Id, Type, Date, Detail, URL\n"
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
        cells = row.findAll('td')
        s = cells[2].a["href"]

        Type_postes = cells[0].img["title"]
        Date = str(dateparser.parse(cells[1].text).date())
        Detail = cells[2].text
        URL = "http://emploi-public.ma/fr/" + cells[2].a["href"]

        if Type_postes == "Postes de responsabilité":
            Id = "poste_e" + re.findall("(?<=e=)(\d+)", s)[0] \
                + "id" + re.findall("(?<=id=)(\d+)", s)[0]
        elif Type_postes == "Emplois supérieurs":
            Id = "emploi_" + re.findall("(?<=id=)(\d+)", s)[0]
        else:
            Id = "concour_e" + re.findall("(?<=e=)(\d+)", s)[0] \
                + "c" + re.findall("(?<=c=)(\d+)", s)[0] \
                + "id" + re.findall("(?<=id=)(\d+)", s)[0]

        f.write(Id + "," + Type_postes + "," + Date + "," + "\"" +
                Detail + "\"," + "\"" + URL + "\"\n")

uClient.close()
f.close()
