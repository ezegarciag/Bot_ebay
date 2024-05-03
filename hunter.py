# Importar las bibliotecas necesarias
import csv
import requests
from bs4 import BeautifulSoup
import telegram



def obtener_datos(producto):
    
    # URL de la página web que quieres scrapear
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={producto}&_sacat=0&LH_Auction=1&_sop=1'
    
    # Realizar la solicitud GET a la página web
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Parsear el contenido HTML usando Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Encontrar todos los divs con la clase "s-item__detail s-item__detail--primary"
        divs = soup.find_all('div', class_='s-item__info')
        
        # Listas para almacenar precios y enlaces
        lista_precios = []
        lista_links = []
        lista_tiempos = []
        
        # Iterar sobre los divs encontrados
        for div in divs:
            # Obtener el precio si está disponible
            precio_elemento = div.find('span', class_='s-item__price')
            termina_tiempo = div.find('span',class_="s-item__time-left")
            if precio_elemento:
                precio = precio_elemento.get_text()
                lista_precios.append(precio)
                if termina_tiempo:
                    tiempo = termina_tiempo.get_text()
                    lista_tiempos.append(tiempo)
            else:
                lista_precios.append('Precio no disponible')
            
            # Obtener el enlace si está disponible
            enlace_elemento = div.find('a', class_='s-item__link')
            if enlace_elemento:
                enlace = enlace_elemento['href']
                lista_links.append(enlace)
            else:
                lista_links.append('Enlace no disponible')
                
        
        return lista_precios,lista_links,lista_tiempos

def guardar(lista_precios,lista_links,lista_tiempos,producto,precio_max):
            # Crear una lista de tuplas con los datos a guardar
        datos = zip( lista_precios, lista_links,lista_tiempos)

        # Ruta donde guardar el archivo CSV
        archivo_csv = f'{producto}.csv'

        # Abrir el archivo CSV en modo de escritura
        with open(archivo_csv, 'w', newline='') as file:
            writer = csv.writer(file)

            # Escribir el encabezado
            writer.writerow(['Precio', 'Enlace',"tiempo"])

            # Escribir los datos
            for precio, enlace, tiempo in datos:
                precio_float = formateo_precio(precio)
                print(tiempo)
                if ('h' not in tiempo) and (precio_float<=precio_max):
                  if(enlace != "https://ebay.com/itm/123456?hash=item28caef0a3a:g:E3kAAOSwlGJiMikD&amdata=enc%3AAQAHAAAAsJoWXGf0hxNZspTmhb8%2FTJCCurAWCHuXJ2Xi3S9cwXL6BX04zSEiVaDMCvsUbApftgXEAHGJU1ZGugZO%2FnW1U7Gb6vgoL%2BmXlqCbLkwoZfF3AUAK8YvJ5B4%2BnhFA7ID4dxpYs4jjExEnN5SR2g1mQe7QtLkmGt%2FZ%2FbH2W62cXPuKbf550ExbnBPO2QJyZTXYCuw5KVkMdFMDuoB4p3FwJKcSPzez5kyQyVjyiIq6PB2q%7Ctkp%3ABlBMULq7kqyXYA"):
                    telegram.alerta(precio,enlace,tiempo)  
                    writer.writerow([precio,enlace,tiempo])
                  

        print("Los datos se han guardado correctamente en", archivo_csv)
            

def formateo_precio(precio):
    # Eliminar el "USD" y cualquier carácter que no sea un dígito o un punto
    precio_str_limpio = ''.join(caracter for caracter in precio if caracter.isdigit() or caracter == '.')

    # Convertir la cadena limpiada a un float
    precio_float = float(precio_str_limpio)
    
    return precio_float

   



precios=[]
links = []
tiempos = []

producto = input("ingrese producto: ")
precio_max = float(input("Ingrese el precio máximo: "))



precios,links,tiempos = obtener_datos(producto)
guardar(precios,links,tiempos,producto,precio_max)
