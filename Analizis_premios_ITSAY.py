import pandas as pd
import requests
import io
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
# Configuracion y Extraccion
URL =  'https://en.wikipedia.org/wiki/I_Told_Sunset_About_You'
headers = {'User-Agent':'Mozilla/5.0'}
response = requests.get(URL, headers=headers)
 #  Buscamos la tabla que tenga la palabra 'Category'
tablas_premios = pd.read_html(io.StringIO(response.text), match='Category')
df_premios = tablas_premios[0]
# Limpieza de datos
if isinstance(df_premios.columns, pd.MultiIndex):
    df_premios.columns = df_premios.columns.get_level_values(-1)
# Localizacion de la columna de resultados
columna_ganadora = None
for columna in df_premios.columns:
    # Queremos que busque la palabra "result" 
    # Queremos que no le importen las mayúsculas (usando un método de texto)
    if "result" in columna.lower(): 
        columna_ganadora = columna
# Procesamineto y Visualizacion        
if columna_ganadora:
    df_premios = df_premios.dropna(subset=[columna_ganadora])
    conteo = df_premios[columna_ganadora].value_counts()    
    plt.style.use('ggplot')
    plt.figure(figsize=(8, 5))
    conteo.plot(kind='bar', color=['#e67e22', '#A2231D', '#95a5a6'])
    plt.title('Exito de "I Told Sunset About You"', fontsize=14)
    plt.xlabel('resultado', fontsize=12)
    plt.ylabel('Cantidad de premiso', fontsize=12)
    plt.xticks(rotation=0)
    plt.show()
else:
    print('Error')

