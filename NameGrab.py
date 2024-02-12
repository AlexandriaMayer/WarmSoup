import pandas as pd
import random
import datetime
from bs4 import BeautifulSoup
import requests

url = 'https://www.behindthename.com/top/lists/united-states/1992'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')



table = soup.find('table', attrs = {'class':'r1r2 pop-table pop-table-m'})
table_rows = table.find_all('tr')
# tr means table code
rows_data = []
headers = [header.text for header in table_rows[0].find_all('th')]

for m_table in table_rows[1:]:
    name_table = m_table.find_all('td')
    name_data = {headers[i]: name_table.text for i, name_table in enumerate(name_table)}
    rows_data.append(name_data)
    print(rows_data)

    # this is not working, will have to try again tomorrow.