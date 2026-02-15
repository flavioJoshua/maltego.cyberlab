import datetime
import inspect
import logging
import os



def GetProperties(Values):
    """_summary_
        prende  i valori di request.Properties o request.Value o per main.py primo = sys.argv[0]
        secondo=sys.argv[1] 
        terzo= sys.argv[2]  e le  fa  diventare una dictionary
   

    Args:
        Values (_type_): _description_  probbile  formato 
        
        maltego.v2.value.property=UAW files federal labor charges against Donald Trump and Elon Musk#theurl=https://www.msn.com/en-us/money/companies/uaw-files-federal-labor-charges-against-donald-trump-and-elon-musk/ar-AA1oJNGd#fulltitle=UAW files federal labor charges against Donald Trump and Elon Musk#description=The United Auto Workers Union has filed federal labor charges against former President Donald Trump and Elon Musk, the union said Tuesday.#provider=ABC News on MSN.com#date_published=2024-08-13 23:10:27.100 +0200#reserved-entity-icon-overlay-url=https://www.bing.com/th?id\=OVFT.hLL6NWBPC7fSZU30T6nxxS&pid\=News 
    Return: 
    ritorna  la Dictionary
    """
    # _dict = dict(item.split('=') for  item  in  Values.split('#'))
    # if  _dict is None:
    #     raise  ValueError(" la dictionary era nulla")
    _dict = {}
    for item in Values.split('#'):
        try:
            key, value = item.split('=')
            _dict[key] = value
        except ValueError:
            log_message("Attenzione:  c'è in errore nella  gestione  dei parametri")
            pass  # Ignora gli elementi che non possono essere suddivisi in due parti

    return _dict




def log_message(message, log_file="audit.log"):
    """_summary_
    serce a  sostituire  logging
    Args:
        message (_type_): _description_
        log_file (str, optional): _description_. Defaults to "audit.log".
    """
    # Ottieni il tempo corrente con precisione ai millesimi di secondo
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    caller_function_name =    inspect.stack()[1].filename +  " : "  +   inspect.stack()[1].function
    # caller_function_name =  ""  


   # Crea il messaggio di log
    log_entry = f"{current_time} | {caller_function_name} | {message}\n"
    
    # Scrivi il messaggio nel file di log
    # Se log_file è relativo, scrive sempre nella root del progetto
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_path = log_file if os.path.isabs(log_file) else os.path.join(base_dir, log_file)
    with open(log_path, "a") as f:
        f.write(log_entry)

    # Scrive anche nei log standard (utile per debug in Maltego)
    logging.getLogger("maltego.server").info(log_entry.strip())

# Esempio di utilizzo
log_message("Questo è un log con millisecondi.")
# log_message("Un altro messaggio di log.")
