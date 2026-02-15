import requests
from bing import  create_file
import json

from utility  import log_message
import os
import dotenv


dotenv.load_dotenv()





def perform_search(query,Maxquery=100):
    # Parametri necessari
    API_KEY = os.environ.get("GCP_API_KEY")
    CSE_ID = os.environ.get("CSE_ID")

    start_index = 1
    while True:
        url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={cse_id}&key={api_key}&start={start_index}"
        log_message(url)

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            
            # with open(create_file("Google"),"w" ) as f:
            #     json.dump(response.json(),f,indent=4)

            log_message(response.json())
            # log_message(response.content) in formato binary

            # Stampa i risultati della pagina corrente
            print(f"Results for query '{query}' (start at {start_index}):")
            for item in data.get('items', []):
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}\n")

            # Controlla se esiste una `nextPage`
            next_page = data.get('queries', {}).get('nextPage')
            if next_page:
                start_index = next_page[0]['startIndex']
                if start_index >= Maxquery:
                    break
            else:
                # Se non esiste una `nextPage`, esci dal ciclo
                break
        else:
            print(f"Error: {response.status_code}")
            break


if __name__ == "__main__":
    QUERY = "ukraine  kursk"

    perform_search( QUERY)





# # URL dell'API con i parametri di ricerca
# url = f"https://www.googleapis.com/customsearch/v1?q={QUERY}&cx={CSE_ID}&key={API_KEY}"

# # Esegui la richiesta
# response = requests.get(url)

# # Stampa i risultati
# if response.status_code == 200:
#     data = response.json()
#     with open(create_file("Google"),"w" ) as f:
#         json.dump(response.json(),f,indent=4)
    
#     for item in data.get('items', []):
#         print(f"Title: {item['title']}")
#         print(f"Link: {item['link']}\n")
# else:
#     print(f"Error: {response.status_code}")
