import logging
from web_scraping.extract_data import extracting_from_url
from loading_into_mongo.load_data import loading_data

if __name__ == "__main__":

    scraped_data = extracting_from_url()
    loading_data(scraped_data)
