from excel import *
from bs4 import BeautifulSoup
import pandas as pd

import requests

def try1():
    for item in read_A_Col_data(fileToReadEnteriesFrom):
        #print(item)
        resp = requests.get(str(item))
        html = resp.text
        soup = BeautifulSoup(html, 'html.parser')
        table_data = []
        table = soup.find('table', id="voter-table")
        for row in table.find_all('tr'):
            raw_hyperlink = row.find('a')
            if(raw_hyperlink):
                hyperlink = str(raw_hyperlink).split("\"")[1]
            else:
                hyperlink = "hyperlink = NONE"
            print(hyperlink)
            row_data = [cell.get_text(strip=True) for cell in row.find_all(['a', 'td', 'th'])]
            #table_data.append(row_data)
            print(row_data)
            row_data[1] = hyperlink
            insertListToROW(row_data)


try1()
