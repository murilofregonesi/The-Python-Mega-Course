import requests
from bs4 import BeautifulSoup
import pandas


# set filters
price_lim = (75e3, 180e3)
area_lim = (750, 2500)
com = '&com=condominio-fechado'

# get first page
_url = 'https://www.vivareal.com.br/venda/sp/sorocaba/lote-terreno_residencial/'
_filters = f'#area-desde={area_lim[0]}&area-ate={area_lim[1]}&preco-desde={price_lim[0]}&preco-ate={price_lim[1]}{com}'
_headers = {'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}

page = requests.get(''.join([_url, _filters]), headers=_headers)
soup = BeautifulSoup(page.content, "html.parser")

# pages loop
data = []
num_pages = len(soup.find_all('li', {'class':'pagination__item', 'data-type': 'number'}))
for page_num in range(0, num_pages):
    print(page_num+1)
    if page_num > 0:
        page = requests.get(''.join([_url, f'?pagina={page_num}', _filters]), headers=_headers)
        soup = BeautifulSoup(page.content, "html.parser")


    # info collection
    properties = soup.find_all('article', {'class': 'property-card__container'})
    for _property in properties:
        #print(_property.prettify())
        price = _property.find('div', {'class': 'property-card__price'})
        try:
            price = price.find('p').text.replace('R$','').replace(' ','').replace('.','')
        except:
            price = 'Sob consulta'

        area = _property.find('li', {'class': 'property-card__detail-area'}).\
            find('span', {'class': 'property-card__detail-value'}).text
        area = area.replace(' ','').replace('.','')

        condominio = None
        try:
            condominio = _property.find('div', {'class': 'property-card__price-details--condo'}).\
                find('strong', {'class': 'js-condo-price'}).text
            condominio = condominio.replace('R$','').replace(' ','').replace('.','')
        except:
            pass

        url = _property.find('a', {'class': 'property-card__content-link'})['href']
        url = url.replace(' ','')

        amenities = _property.find('ul', {'class': 'property-card__amenities'})
        try:
            amenities = amenities.find_all('li', {'class': 'amenities__item'})
        except:
            amenities = []


        # append property details
        data.append({
            'preço': price,
            'área': area,
            'condomínio': condominio,
            'url': url
        })
        for amenitie in amenities:
            data[-1][amenitie.text] = 'Sim'

    # TODO properties are repeating for every page
    # TODO total properties is wrong
    # TODO total pages different from browser or even Selenium


# store scraping details
df = pandas.DataFrame(data)
df.to_excel('Resultado.xlsx')

print(df)
