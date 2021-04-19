import requests
from bs4 import BeautifulSoup

# set filters
price_lim = (75e3, 180e3)
area_lim = (750, 2500)
condominio = '&com=condominio-fechado'

# get page
_url = 'https://www.vivareal.com.br/venda/sp/sorocaba/lote-terreno_residencial/'
_filters = f'#area-desde={area_lim[0]}&area-ate={area_lim[1]}&preco-desde={price_lim[0]}&preco-ate={price_lim[1]}{condominio}'
_headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}

page = requests.get(''.join([_url, _filters]), headers=_headers)
soup = BeautifulSoup(page.content, "html.parser")

# pages loop
num_pages = len(soup.find_all('li', {'class':'pagination__item', 'data-type': 'number'}))
for page_num in range(0, num_pages):
    print(page_num+1)
    if page_num > 0:
        page = requests.get(''.join([_url, f'?pagina={page_num}', _filters]), headers=_headers)
        soup = BeautifulSoup(page.content, "html.parser")

    properties = soup.find_all('article', {'class': 'property-card__container'})
    for _property in properties:
        pass
        #print(_property)
        #print(_property.find_all('div')[0].get('id'))
    # dentro div unica com ID

# prints
print(total_results)
#print(soup.prettify())
