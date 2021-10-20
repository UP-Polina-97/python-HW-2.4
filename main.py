import requests
from bs4 import BeautifulSoup
import json





class Generator_of_country():
    def __init__(self):
        self.Countries_to_find = set()
        self.data = ()
#        self.links_parts = ()
    page = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area')
    soup = BeautifulSoup(page.content, 'html.parser')
    table = soup.find('table', {'class': 'wikitable sortable'})
    links_parts = table.findAll('a')


    def reading_json_and_getting_links(self, name_of_file):
        f = open(name_of_file,)
        data = json.load(f)
        for k in data:
            self.Countries_to_find.add(k.get('name').get('common'))
        f.close()



    def print_names_and_links(self):
        page = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area')
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find('table', {'class': 'wikitable sortable'})
        links_parts = table.findAll('a')
        for link in links_parts:
            href = link.get('href')
            hr = link.get('title')
            for country in self.Countries_to_find:
                if country == hr:
                    link_maker = 'https://en.wikipedia.org' + href
                    yield hr, '--->', link_maker
    def inis(self):
        for item in self.print_names_and_links():
            print(item)


if __name__ == '__main__':
    generate = Generator_of_country()
    generate.reading_json_and_getting_links('countries.json')
    generate.inis()
