import requests
from bs4 import BeautifulSoup
import logging
from datetime import datetime
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def extracting_from_url()->list:

    url = "https://www.essencemontreal.com/prices.php?l=e&prov=QC&city=Montreal"

    #Sending request to url and checking status_code
    try : 
        response = requests.get(url=url)
        if response.status_code == 200:
            logging.info("Response is OK")
        else:
            logging.error(f"Returned {response.status_code} code")
    except Exception as e :
        logging.error(f"{e}")

    #creating soup object
    soup = BeautifulSoup(response.text, 'html.parser')

    prices = soup.find_all('td', {'class':['greencell', 'redcell']})
    stations = soup.find_all('td', {'class': 'stationcell'})
    cities = soup.find_all('td', {'class': 'citycell'})
    times_users = soup.find_all('td', {'class': 'usercell'})

    gas_prices = []
    
    for price, station, city, time_user in zip(prices, stations, cities, times_users):

        gas_station = " ".join(station.stripped_strings)
        gas_city = " ".join(city.stripped_strings)
        gas_price = " ".join(price.stripped_strings)
        gas_time_user = " ".join(time_user.stripped_strings)
        
        #adding todays date as load_time
        today = datetime.today()
        
        gas_prices.append((gas_city,gas_station,gas_price,gas_time_user, today))

    return gas_prices


    

