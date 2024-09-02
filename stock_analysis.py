import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

# Pregunta 1: Extraer datos de acciones de Tesla usando yfinance
def get_tesla_stock_data():
    tesla_data = yf.download('TSLA', start='2010-01-01', end='2023-12-31')
    tesla_data.reset_index(inplace=True)  
    print("Tesla Stock Data (First 5 Rows):")
    print(tesla_data.head())  
    return tesla_data

tesla_stock_data = get_tesla_stock_data()


# Pregunta 2: Extraer datos de ingresos de Tesla usando web scraping
def get_tesla_revenue_data():
    url_tesla = 'https://finance.yahoo.com/quote/TSLA/financials?p=TSLA'
    response_tesla = requests.get(url_tesla)
    soup_tesla = BeautifulSoup(response_tesla.text, 'html.parser')

    tables_tesla = soup_tesla.find_all('table')

    for table in tables_tesla:
        if 'Total Revenue' in str(table):  
            tesla_revenue = pd.read_html(str(table))[0]
            print("Tesla Revenue Data (Last 5 Rows):")
            print(tesla_revenue.tail()) 
            return tesla_revenue

    print("No se encontró la tabla de ingresos de Tesla en la página web.")
    return None

tesla_revenue_data = get_tesla_revenue_data()


# Pregunta 3: Extraer datos de acciones de GameStop usando yfinance
def get_gme_stock_data():
    gme_data = yf.download('GME', start='2010-01-01', end='2023-12-31')
    gme_data.reset_index(inplace=True)  
    print("GameStop Stock Data (First 5 Rows):")
    print(gme_data.head())  
    return gme_data

gme_stock_data = get_gme_stock_data()


# Pregunta 4: Extraer datos de ingresos de GameStop usando web scraping
def get_gme_revenue_data():
    url_gme = 'https://finance.yahoo.com/quote/GME/financials?p=GME'
    response_gme = requests.get(url_gme)
    soup_gme = BeautifulSoup(response_gme.text, 'html.parser')

    tables_gme = soup_gme.find_all('table')

    for table in tables_gme:
        if 'Total Revenue' in str(table): 
            gme_revenue = pd.read_html(str(table))[0]
            print("GameStop Revenue Data (Last 5 Rows):")
            print(gme_revenue.tail())  
            return gme_revenue

    print("No se encontró la tabla de ingresos de GameStop en la página web.")
    return None

gme_revenue_data = get_gme_revenue_data()


# Pregunta 5: Graficar los datos de acciones de Tesla
def make_graph(data, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price USD ($)')
    plt.grid()
    plt.show()

make_graph(tesla_stock_data, 'Tesla Stock Price History')


# Pregunta 6: Graficar los datos de acciones de GameStop
make_graph(gme_stock_data, 'GameStop Stock Price History')
