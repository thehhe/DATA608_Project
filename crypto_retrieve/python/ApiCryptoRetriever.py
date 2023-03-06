import requests
from typing import Any

class ApiCryptoRetriever:
    def __init__(self, url_template: str, currencies: str, interval: str) -> None:
        self.currencies = currencies
        self.interval = interval

        self.url = url_template.format(self.currencies, self.interval)

    def retrieve_data(self) -> dict[str, Any]:
        response = requests.get(self.url)
        return response.json()
    

import configparser
import os
if __name__ == "__main__":
    config_filename = "config.ini"
    full_path = os.path.realpath(__file__)
    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(full_path), "../config", config_filename))

    url_template = config["API"]["api_url_template"]
    currencies = config["API"]["crypto_subset"]
    interval = config["API"]["interval"]

    api_crypto_retriever = ApiCryptoRetriever(url_template, currencies, interval)
    print(api_crypto_retriever.retrieve_data())
