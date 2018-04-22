import re
import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.socks-proxy.net")
soup = BeautifulSoup(r.text, 'html.parser')

lista = []
for info in soup.find_all('td'):
	ip_candidates = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|\d{2,5}\b", str(info))
	scanSocks = re.findall(r"Socks[4-5]",str(info))
	if ip_candidates:
		lista.append(ip_candidates[0])
	elif scanSocks:
		lista.append(scanSocks[0])

a = 0
while a < len(lista):
	print(lista[a+2] + " " + lista[a] + " " + lista[a+1])
	a += 3