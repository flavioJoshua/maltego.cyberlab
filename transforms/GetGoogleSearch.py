import socket

from extensions import registry
from maltego_trx.entities import IPAddress
from maltego_trx.maltego import UIM_TYPES, MaltegoMsg, MaltegoTransform
from maltego_trx.entities import *
from maltego_trx.transform import DiscoverableTransform
from utility import   GetProperties
from maltego_trx.maltego  import BOOKMARK_COLOR_BLUE , BOOKMARK_COLOR_GREEN, BOOKMARK_COLOR_PURPLE, BOOKMARK_COLOR_RED, BOOKMARK_COLOR_YELLOW       

# from Search import GoogleCSE
import os
import dotenv


dotenv.load_dotenv()




def cerca_immagini(query, api_key, cse_id, num_risultati=5):
    import  requests

    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": query,
        "cx": cse_id,
        "key": api_key,
        "searchType": "image",
        "num": num_risultati
    }

    response = requests.get(url, params=params)
    data = response.json()

    risultati = []
    for item in data.get("items", []):
        risultati.append(item["link"])
    return risultati



@registry.register_transform(display_name="ICT Search Image by Google CSE", input_entity="maltego.Phrase",
                             description='ICT get image links output maltego.Image',
                             output_entities=["maltego.Image"])
class GetGoogleSearchImage(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
         
        from utility import   log_message
        import  requests
        # log_message(f"{type(request.Properties)}")

        _strProperties='\n'.join( f" {Key} : {Value} "  for Key, Value in request.Properties.items()  )
        _strSettings='\n'.join( f" {Key} : {Value} "  for Key, Value in request.TransformSettings.items()  )

        log_message(f" Value: {request.Value}\n Properties:  { _strProperties} \n TransformSettings: { _strSettings} ")

         # Parametri necessari
        API_KEY = os.environ.get("GCP_API_KEY")
        CSE_ID = os.environ.get("CSE_ID")
        max_results = 100
        query=request.Value

        start_index = 1
        while True:
            params = {
                "q": query,
                "cx": CSE_ID,
                "key": API_KEY,
                "searchType": "image",
                "start": start_index,
            }
            log_message(f"https://www.googleapis.com/customsearch/v1?{params}")

            http_response = requests.get("https://www.googleapis.com/customsearch/v1", params=params)

            if http_response.status_code == 200:
                data = http_response.json()

                
                # with open(create_file("Google"),"w" ) as f:
                #     json.dump(response.json(),f,indent=4)

                log_message(http_response.json())
                # log_message(response.content) in formato binary

                # Stampa i risultati della pagina corrente
                log_message(f"Results for query '{query}' (start at {start_index}):")
                for item in data.get('items', []):
                    search_Title=""
                    Search_link=""
                    search_Title = item['title']
                    Search_link = item['link']
                    _entity=response.addEntity(Image,Search_link)
                    _entity.addProperty("url",value=Search_link)
                    _entity.addProperty("title",value=search_Title)
                    _entity.addProperty("source", value=item.get("image", {}).get("contextLink", ""))
                    

                # Controlla se esiste una `nextPage`
                next_page = data.get('queries', {}).get('nextPage')
                if next_page:
                    start_index = next_page[0]['startIndex']
                    if start_index > max_results:
                        break
                else:
                    # Se non esiste una `nextPage`, esci dal ciclo
                    break
            else:
                log_message(f"Error: {http_response.status_code} | params: {params}")
                break


        # _ict_person=response.addEntity(URL,)

        # _ict_person.setBookmark(BOOKMARK_COLOR_BLUE)
        # _ict_person.addProperty("content_Article","content_Article",value=_strArticle)
        # _ict_person.setNote(_strArticle)
        # _ict_person.addProperty("data","data",value=_data_writer)




@registry.register_transform(display_name="ICT Search  by Google CSE", input_entity="maltego.Phrase",
                             description='ICT get Link  and Title output  Maltego.URL',
                             output_entities=["maltego.URL"])
class GetGoogleSearch(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
         
        from utility import   log_message
        import  requests
        # log_message(f"{type(request.Properties)}")

        _strProperties='\n'.join( f" {Key} : {Value} "  for Key, Value in request.Properties.items()  )
        _strSettings='\n'.join( f" {Key} : {Value} "  for Key, Value in request.TransformSettings.items()  )

        log_message(f" Value: {request.Value}\n Properties:  { _strProperties} \n TransformSettings: { _strSettings} ")

         # Parametri necessari
        API_KEY = os.environ.get("GCP_API_KEY")
        CSE_ID = os.environ.get("CSE_ID")
        Maxquery=256
        query=request.Value

        start_index = 1
        while True:
            url = f"https://www.googleapis.com/customsearch/v1?q={query}&cx={CSE_ID}&key={API_KEY}&start={start_index}"
            log_message(url)

            http_response = requests.get(url)

            if http_response.status_code == 200:
                data = http_response.json()

                
                # with open(create_file("Google"),"w" ) as f:
                #     json.dump(response.json(),f,indent=4)

                log_message(http_response.json())
                # log_message(response.content) in formato binary

                # Stampa i risultati della pagina corrente
                log_message(f"Results for query '{query}' (start at {start_index}):")
                for item in data.get('items', []):
                    search_Title=""
                    Search_link=""
                    search_Title = item['title']
                    Search_link = item['link']
                    _entity=response.addEntity(URL,Search_link)
                    _entity.addProperty("url",value=Search_link)
                    _entity.addProperty("title",value=search_Title)
                    

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
                log_message(f"URL: {url} \n Error: {http_response.status_code}")
                break


        # _ict_person=response.addEntity(URL,)

        # _ict_person.setBookmark(BOOKMARK_COLOR_BLUE)
        # _ict_person.addProperty("content_Article","content_Article",value=_strArticle)
        # _ict_person.setNote(_strArticle)
        # _ict_person.addProperty("data","data",value=_data_writer)

