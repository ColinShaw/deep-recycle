from bs4 import BeautifulSoup
import yaml
import uuid
import requests
import json


class Images(object):

    def __init__(self, config_file):
        self._c = yaml.load(open(config_file))

    def _fetch_links(self, query, pages):
        urls = []
        for i in range(pages):
            u = self._c['search-string'].format(query, i*100)
            cont = requests.get(u, headers={'User-Agent':self._c['user-agent']})
            soup = BeautifulSoup(cont.text, 'lxml')
            for a in soup.find_all('div', {'class': 'rg_meta'}):
                t = json.loads(a.text)
                if t['ity'] == 'jpg' or t['ity'] == 'jpeg':
                    urls.append(t['ou'])
        return urls

    def _fetch_images(self, urls, destination):
        for u in set(urls):
            try:
                d = requests.get(u, headers={'User-Agent':self._c['user-agent']})
                name = str(uuid.uuid4())
                with open('{}/{}.jpg'.format(destination, name), 'wb') as f:
                    f.write(d.content)
            except:
                pass

    def fetch(self, categories):
        for cat in categories:
            c = self._c[cat]
            links = self._fetch_links(c['query'], c['pages'])
            self._fetch_images(links, c['dest'])


Images('configs/images.yaml').fetch(['landfill-trash','grass-landscape','cityscape'])

