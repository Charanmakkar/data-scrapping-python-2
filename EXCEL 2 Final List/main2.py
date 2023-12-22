from excel import *
from bs4 import BeautifulSoup
import pandas as pd

import requests

def try1():
    for item in read_A_Col_data(fileToReadEnteriesFrom):
        try:
            temp_list = []
            temp_list = [item]
            print(item)
            resp = requests.get(str(item))
            html = resp.text
            soup = BeautifulSoup(html, 'html.parser')
            table_data = []
            table = soup.find('table', id="")
            for row in table.find_all('tr'):
                row_data = [cell.get_text(strip=True) for cell in row.find_all(['a', 'td', 'th'])]
                print(row_data)
                temp_list.append(row_data[2])
            insertListToROW(temp_list)
                
        except:
            print("*************************ok**************************")
            insertListToROW(["ERROORRR"])
try1()
