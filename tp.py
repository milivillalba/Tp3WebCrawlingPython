import requests
from bs4 import BeautifulSoup
import json

def crawl_website(url):
    # Lista para almacenar los datos recolectados
    datos = {}

    # Realizar la solicitud GET a la URL
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        # Parsear el contenido HTML usando BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Encontrar todas las etiquetas <a> con sus enlaces
        links = soup.find_all('a')

        # Recorrer cada enlace encontrado
        for link in links:
            # Obtener la URL del enlace
            link_url = link.get('href')

            # Verificar si la URL es válida
            if link_url.startswith('http'):
                # Realizar una nueva solicitud GET a la URL del enlace
                link_response = requests.get(link_url)

                # Verificar si la solicitud fue exitosa
                if link_response.status_code == 200:
                    # Parsear el contenido HTML del enlace
                    link_soup = BeautifulSoup(link_response.text, 'html.parser')

                    # Encontrar todas las etiquetas <h1> y <p> en el contenido del enlace
                    h1_tags = link_soup.find_all('h1')
                    p_tags = link_soup.find_all('p')

                    # Almacenar los elementos encontrados en un diccionario
                    link_data = {
                        'h1': [h1.text.strip() for h1 in h1_tags],
                        'p': [p.text.strip() for p in p_tags]
                    }

                    # Agregar los datos al diccionario principal usando la URL del enlace como clave
                    data[link_url] = link_data

    return data

# URL del sitio web
url = 'https://doramasflix.co/'

# Llamar a la función para rastrear el sitio web y obtener los datos
result = crawl_website(url)

# Guardar los datos en un archivo JSON
with open('web_crawler_data.json', 'w') as json_file:
    json.dump(result, json_file, indent=4)

print("Los datos se han almacenado correctamente en 'web_crawler_data.json'")
