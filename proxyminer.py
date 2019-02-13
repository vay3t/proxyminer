import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.socks-proxy.net")
soup = BeautifulSoup(r.text, 'html.parser')

data = []
table = soup.find('table', attrs={'id':'proxylisttable'})

rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values

for elemento in data:
	if elemento:
		#print(elemento)
		print(elemento[4].lower()+ " " +elemento[0]+ " " +elemento[1]+ " # " +elemento[2])

