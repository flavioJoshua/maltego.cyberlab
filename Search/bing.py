#Copyright (c) Microsoft Corporation. All rights reserved.
#Licensed under the MIT License.

# -*- coding: utf-8 -*-

import json
import os 
from pprint import pprint
import requests


def create_file(NomeEngine = "Bing"):
    """ crea il nomeFile con la data e Time  """
    import datetime
    # Ottieni l'ora e la data correnti fino al secondo
    current_time = datetime.datetime.now().strftime("%Y-%m-%d-:-%H-%M-%S-%f")
    
    # Crea il nome del file
    filename = NomeEngine + current_time + ".json"
    return filename












def BingSearch():
    os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']="e039e1836b0c4cd6a4808dd37db4a5a3"

    """ sbagliato """
    os.environ['BING_SEARCH_V7_ENDPOINT']="https://api.bing.microsoft.com"

    # search_url = "https://api.bing.microsoft.com/v7.0/search"
    search_url = "https://api.bing.microsoft.com/v7.0/news/search"



    # Add your Bing Search V7 subscription key and endpoint to your environment variables.
    subscription_key = os.environ['BING_SEARCH_V7_SUBSCRIPTION_KEY']

    """ sbagliato """
    endpoint = os.environ['BING_SEARCH_V7_ENDPOINT'] + "/bing/v7.0/search"


    endpoint=search_url
    # Query term(s) to search for. 
    query = "Ukraine to Kursk"

    # Construct a request
    mkt = 'en-US'
    params = { 'q': query, 'mkt': mkt }
    headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

    # Call the API
    try:
        response = requests.get(endpoint, headers=headers, params=params)
        response.raise_for_status()

        print("\nHeaders:\n")
        print(response.headers)

        print("\nJSON Response:\n")
        pprint(response.json())
        with  open(create_file(),"w" ) as f:
            json.dump(response.json(),f,indent=4)
        
    except Exception as ex:
        raise ex