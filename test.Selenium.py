from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.add_argument("-private")
options.add_argument("--headless")  # Modalità headless


# Specifica il percorso del geckodriver tramite la classe Service
service = Service(executable_path='/home/flavio/code/Osint/geckodriver')

# Inizializza il driver di Firefox con il servizio e le opzioni
driver = webdriver.Firefox(service=service, options=options)

# Naviga verso la pagina desiderata
driver.get("https://www.msn.com/en-za/news/world/russian-president-s-spokesperson-sends-a-message-to-telegram-ceo-after-moscow-attack-expected-more-attention-from-pavel-durov/ar-BB1kIZNT")  # Sostituire con l'URL della pagina reale che desideri scaricare

# Aspetta che la pagina si carichi completamente
driver.implicitly_wait(10)  # Attendere fino a 10 secondi per il caricamento completo della pagina

# Ottenere l'HTML completo della pagina
html = driver.page_source

# Aspetta che un elemento specifico sia visibile sulla pagina
try:
    WebDriverWait(driver, 10).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )
    # Una volta che il body è presente, estrai il testo
    page_text = driver.find_element(By.TAG_NAME, "body").text
    log_message(page_text)
finally:
    driver.quit()






# Chiudi il browser
driver.quit()

from newspaper import Article
from io import StringIO

# Crea un oggetto Article e passa l'HTML
article = Article('')
article.set_html(html)  # Imposta l'HTML direttamente

from  utility import log_message

log_message(html)
article.parse()  # Analizza l'articolo

# Stampa il testo estratto
print("Title:", article.title)
print("Text:", article.text)