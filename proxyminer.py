import requests
from bs4 import BeautifulSoup
import sys

global urltarget

def obtainProxies():
	r = requests.get("https://www.socks-proxy.net")
	soup = BeautifulSoup(r.text, 'html.parser')

	data = []
	table = soup.find('table', attrs={'id':'proxylisttable'})

	rows = table.find_all('tr')
	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		data.append([ele for ele in cols if ele]) # Get rid of empty values


	allProxys = []

	for elemento in data:
		if elemento:
			listOneProxy = []

			typeSocks = elemento[4].lower()
			if typeSocks != ("socks4" or "socks5"):
				continue
			ipProxy = elemento[0]
			portProxy = elemento[1]
			countryCode = elemento[2]

			listOneProxy.append(typeSocks)
			listOneProxy.append(ipProxy)
			listOneProxy.append(portProxy)
			listOneProxy.append(countryCode)

			#print("{0} {1} {2} # {3}".format(typeSocks,ipProxy,portProxy,countryCode))
			allProxys.append(listOneProxy)

	return allProxys


def checkProxy(lista):
	buildProxy = "{0}://{1}:{2}".format(lista[0],lista[1],lista[2])
	printProxy = "{0} {1} {2} # {3}".format(lista[0],lista[1],lista[2],lista[3])
	proxy = {'http': buildProxy,
		'https': buildProxy}
	try:
		requests.get(urltarget, proxies=proxy)
		#print(printProxy+" ---> ON")
		print(printProxy)
	except requests.exceptions.ConnectionError:
		#print("# "+printProxy+" ---> OFF")
		pass


def help():
	print("""usage: python3 """ + sys.argv[0] + """ <target>
""")



if len(sys.argv) != 2:
	help()
else:
	if sys.argv[1] == "help":
		help()
	elif sys.argv[1]:
		urltarget = sys.argv[1]
		from multiprocessing import Pool
		p = Pool(80)
		p.map(checkProxy, obtainProxies())
	else:
		help()
