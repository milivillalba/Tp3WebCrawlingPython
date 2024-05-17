import requests
from bs4 import BeautifulSoup
#url elegida
url= 'https://www.mercadolibre.com.ar/c/autos-motos-y-otros#menu=categories'

#reques
response = requests.get(url)
#obtener texto plano y darselo a beautifuloup
soup= BeautifulSoup(response.text,"html.parser")


#buscar un elemento por su clase en eun html 

classResul= soup.find_all('img',class_="dynamic-carousel__img")

for img in classResul:
    print(img['data-src'])