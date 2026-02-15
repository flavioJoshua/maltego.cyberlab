def _readByReadabilityXml(url="https://www.lrb.co.uk/the-paper/v22/n23/daniel-soar/short-cuts"):
    """_summary_

    lascia  HTML un pò dentro al testo ma le  funzioni ausiliare sono molto efficaci

    Returns:
        _type_: _description_
  
///FIXME: questa  pagine  web risulta  vuota : https://www.msn.com/en-in/entertainment/hollywood/i-ve-never-been-married-telegram-ceo-is-father-to-over-100-biological-kids-in-12-countries/ar-BB1qSqbD

    Args:
        url (str, optional): _description_. Defaults to "https://www.lrb.co.uk/the-paper/v22/n23/daniel-soar/short-cuts".
    """



    import requests
    from readability import Document
    from lxml import html

    # URL della pagina web da analizzare
   

    # Scarica il contenuto della pagina web
    response = requests.get(url)
    doc = Document(response.text)

    # Parsing del contenuto HTML con lxml
    tree = html.fromstring(response.content)

    # Estrarre il titolo e il contenuto principale
    title = doc.title()
    summary = doc.summary()


    # Stampa il titolo
    print("Titolo:", title)

    # Stampa il testo dell'articolo (contenuto semplificato)
    print("\nTesto dell'articolo:")
    print(summary)

    # Estrazione delle immagini
    print("\nImmagini trovate:")
    images = tree.xpath('//img/@src')
    for image in images:
        print(image)

    print("\n senza  HTML :\n")
    print(doc.get_clean_html())


    # Estrazione dei link presenti nella pagina
    print("\nLink presenti nella pagina:")
    links = tree.xpath('//a/@href')
    for link in links:
        print(link)





def _readByNewsPaper(url="https://www.lrb.co.uk/the-paper/v22/n23/daniel-soar/short-cuts"):
    """_summary_
    perfetto,  il testo senza HTML  ma le funzione  aggintive per  images  movies e link sono poco efficaci

    Returns:
        _type_: _description_
  


    Args:
        url (str, optional): _description_. Defaults to "https://www.lrb.co.uk/the-paper/v22/n23/daniel-soar/short-cuts".
    """

    # https://www.lrb.co.uk/the-paper/v22/n23/daniel-soar/short-cuts

    from newspaper import Article

    # URL dell'articolo da analizzare
    # url = 'https://www.lrb.co.uk/the-paper/v22/n23/daniel-soar/short-cuts'

    # Crea un oggetto Article
    article = Article(url)

    # Scarica il contenuto della pagina
    article.download()

    # Parsing del contenuto
    article.parse()

    # Effettua il download e l'estrazione del testo, immagini e link
    article.nlp()

    # Stampa il titolo
    print("Titolo:", article.title)

    # Stampa il testo dell'articolo
    print("\nTesto dell'articolo:")
    print(article.text)

    # Stampa l'autore (se disponibile)
    print("\nAutore:", article.authors)

    # Stampa la data di pubblicazione (se disponibile)
    print("\nData di pubblicazione:", article.publish_date)

    # Stampa la lista delle immagini estratte
    print("\nImmagini trovate:")
    for image in article.images:
        print(image)

    # Stampa la lista dei video estratti
    print("\nVideo trovati:")
    for video in article.movies:
        print(video)


    # # Stampa i link ad altre URL presenti nel testo
    # print("\nLink presenti nell'articolo:")
    # for link in article.links:
    #     print(link)

    # Stampa i link trovati nel testo dell'articolo
    print("\nLink presenti nel testo:")
    for link in article.text.split():
        if link.startswith("http"):
            print(link)


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        url = sys.argv[1]
        _readByReadabilityXml(url)
    else:
        _readByNewsPaper()

