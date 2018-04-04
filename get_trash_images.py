from bs4 import BeautifulSoup
import requests
import json


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'
}
links = []




for i in range(10):
    u = 'https://www.google.com/search?q=trash+landfill&source=lnms&tbm=isch&start={}'.format(i*100)
    content = requests.get(u, headers=headers)
    soup = BeautifulSoup(content.text, 'lxml')
    for a in soup.find_all('div', {'class': 'rg_meta'}):
        t = json.loads(a.text)
        if t['ity'] == 'jpg' or t['ity'] == 'jpeg':
            links.append(t['ou'])

for i,u in enumerate(links):
    d = requests.get(u, headers=headers)
    with open('data/{}.jpg'.format(i), 'wb') as f:
        f.write(d.content)


