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




def fileTOexcel_Table1():
    file_path = 'file.html'

    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract table data and organize it into a list of lists
    table_data = []

    institute_type = soup.find('span', id="ctl00_ContentPlaceHolder1_lblinsttype").string[17:]
    
    table = soup.find('table', id="ctl00_ContentPlaceHolder1_grd1")
    for row in table.find_all('tr'):
        row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
        table_data.append(row_data)

    institute_details = row_data[0]
##    print(institute_details)
    institute_details = institute_details.split(":")
    instituteCode = institute_details[1].split("INSTITUTE NAME")[0]
    instituteName = institute_details[1].split("INSTITUTE NAME")[1]

    institute_details = row_data[1]
##    print(institute_details)
    institute_details = institute_details.split(":")
    phoneNumber = institute_details[-2].split("ALTERNATIVEMOBILENUMBER")[0]
    alternateNumber = institute_details[-1]
    webSite = institute_details[1].split("EMAILID")[0]
    emailId = institute_details[2].split("MOBILE")[0]

    institute_details = row_data[2]
##    print(institute_details)
    address = institute_details.split(":")[1][:-8]
    district = institute_details.split(":")[-2][:-7]
    pincode = institute_details.split(":")[-1]

    return [instituteCode, instituteName, phoneNumber, alternateNumber, emailId, webSite, address, district, pincode, institute_type]   #instituteCode, instituteName, phoneNumber, alternateNumber, emailId, webSite, address, district, pincode


def fileTOexcel_Table2():
    file_path = 'file.html'

    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract table data and organize it into a list of lists
    table_data = []

    table = soup.find('table', id="ctl00_ContentPlaceHolder1_grdbranch")
    for row in table.find_all('tr'):
        row_data = [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]
        table_data.append(row_data)
    del table_data[0]
    
    print(table_data)

##    
##    S_No = table_data[3][0]
##    BRANCH_CODE = table_data[3][1]
##    BRANCH_NAME = table_data[3][2]
##    TOTAL_SEATS = table_data[3][3]
    
    return table_data
##    return [S_No, BRANCH_CODE, BRANCH_NAME, TOTAL_SEATS] 
##    return [instituteCode, instituteName, phoneNumber, alternateNumber, emailId, webSite, address, district, pincode]   #instituteCode, instituteName, phoneNumber, alternateNumber, emailId, webSite, address, district, pincode

# r1 = fileTOexcel_Table1()
# r2 = fileTOexcel_Table2()
