import requests
import json
import logging

def extract():
    try:
        logging.info("pipeline started")

        with open(r"c:\Users\HP TH\OneDrive\Desktop\ETL pipeline 2\data\file.json", "r") as f:
            config = json.load(f)

        api_url = config.get("input_file")
        output_file = config.get("output_file")
        log_file = config.get("log_file")

        if not api_url:
            raise ValueError("API URL missing in config")

        
        logging.info("API request started")
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()

        return data, output_file
        
    except Exception as e:
        logging.error(f"Error due to {e}")
        return None, None