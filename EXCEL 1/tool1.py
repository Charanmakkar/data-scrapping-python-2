from bs4 import BeautifulSoup

import requests

# request web page
resp = requests.get("https://aptiindia.org/member_list_new/search/0/0/0")

# get the response text. in this case it is HTML
html = resp.text

# parse the HTML
soup = BeautifulSoup(html, "html.parser")

# print the HTML as text
##print(soup.body.get_text().strip())
