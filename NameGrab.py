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