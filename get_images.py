from bs4 import BeautifulSoup
import requests
import json


def fetch_images(query, pages, destination):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36'}
    links = []
    for i in range(pages):
        u = 'https://www.google.com/search?q={}&source=lnms&tbm=isch&start={}'.format(query, i*100)
        content = requests.get(u, headers=headers)
        soup = BeautifulSoup(content.text, 'lxml')
        for a in soup.find_all('div', {'class': 'rg_meta'}):
            t = json.loads(a.text)
            if t['ity'] == 'jpg' or t['ity'] == 'jpeg':
                links.append(t['ou'])
    for i,u in enumerate(links):
        d = requests.get(u, headers=headers)
        with open('{}/{}.jpg'.format(destination, i), 'wb') as f:
            f.write(d.content)


fetch_images('trash+landfill', 5, 'data/trash')
fetch_images('normal+grass+landscape', 10, 'data/landscape'
