from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup 

def scrape_and_export_to_excel(producto, excel_file_path, num_productos):
    url = f"https://listado.mercadolibre.com.co/{producto}"
    
    
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        productos = soup.find_all('div', class_='andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16')[:num_productos]
        
        # Crear un nuevo libro de Excel
        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Productos"
        sheet.append(["Nombre", "Precio","calificacion"])
        
        for producto in productos:
            nombre = producto.find('h2', class_='ui-search-item__title').text
            precio = producto.find('span', class_='andes-money-amount__fraction').text
            #calificacion = producto.fin('div', class_='ui-search-item__group ui-search-item__group--reviews').text
   
            sheet.append([nombre, precio,])
        
        workbook.save(excel_file_path)
        print(f"Los {num_productos} mejores resultados de consolas se han exportado a Excel correctamente.")
    else:
        print("No se pudo conectar a Mercado Libre")

scrape_and_export_to_excel("consolas", "consolas.xlsx", 10)