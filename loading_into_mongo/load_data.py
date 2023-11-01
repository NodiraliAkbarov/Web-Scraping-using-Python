from pymongo import MongoClient
import logging
from dotenv import load_dotenv
import os


load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def loading_data(data:list):
    """Function receives a list of tuples on gas_info and loads into MongoDB"""

    client = MongoClient(os.getenv('uri'))
    
    #checking connection to MongoDB
    try : 
        client.admin.command('ping')
        logging.info("Successfully connected to MongoDB")
    except Exception as e:
        logging.error(f"{e}")

    try :
        #connecting gas_prices_coll collection from gas_prices_db database
        collection = client['gas_prices_db']['gas_prices_coll']

        for gas_info in data:
            document = {
                "city": gas_info[0],
                "station": gas_info[1],
                "price": float(gas_info[2]),
                "time_and_user": gas_info[3],
                "load_date": gas_info[4]
            }

            collection.insert_one(document)
        logging.info(f"Inserted {len(data)} documents")

    except Exception as e:
        logging.error(f"{e}")
    
    client.close()
    logging.info("MongoDB connection closed")


