from extensions import registry
from maltego_trx.maltego import BOOKMARK_COLOR_GREEN, BOOKMARK_COLOR_PURPLE, BOOKMARK_COLOR_RED, UIM_TYPES, MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform
from utility import log_message

from lxml import html
from newspaper import Article
from readability import Document
import requests


def extract_url_from_request(value, properties=None):
    props = properties or {}
    for key in ("theurl", "url", "link"):
        candidate = str(props.get(key, "") or "").strip()
        if candidate:
            return candidate
    fallback = str(value or "").strip()
    if fallback.startswith("http://") or fallback.startswith("https://"):
        return fallback
    raise ValueError("URL non trovata in request.Properties (theurl/url/link) o request.Value.")


def download_article_text(url):
    errors = []
    try:
        article = Article(url)
        article.download()
        article.parse()
        text = str(article.text or "").strip()
        title = str(article.title or "").strip()
        publish_date = ""
        if article.publish_date is not None:
            try:
                publish_date = article.publish_date.isoformat()
            except Exception:
                publish_date = str(article.publish_date)
        if text:
            return {
                "url": url,
                "title": title,
                "text": text,
                "publish_date": publish_date,
                "download_method": "newspaper3k",
            }
        errors.append("newspaper3k empty text")
    except Exception as exc:
        errors.append(f"newspaper3k: {exc}")

    try:
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/127.0 Safari/537.36"
            )
        }
        response = requests.get(url, headers=headers, timeout=25)
        response.raise_for_status()
        doc = Document(response.text)
        title = str(getattr(doc, "short_title", lambda: "")() or doc.title() or "").strip()
        summary_html = str(doc.summary() or "")
        text = ""
        if summary_html:
            try:
                text = " ".join(html.fromstring(summary_html).text_content().split())
            except Exception:
                text = ""
        if not text:
            try:
                text = " ".join(html.fromstring(response.content).text_content().split())
            except Exception:
                text = ""
        if text:
            return {
                "url": url,
                "title": title,
                "text": text,
                "publish_date": "",
                "download_method": "readability-lxml",
            }
        errors.append("readability-lxml empty text")
    except Exception as exc:
        errors.append(f"readability-lxml: {exc}")

    raise RuntimeError(f"Download articolo fallito: {' | '.join(errors)}")



@registry.register_transform(display_name="ICT Article Details", input_entity="maltego.URL",
                             description=' get Article, Get  relative URLs, Get Image.',
                             output_entities=["ict.ArticleDetails"])
class getArticle(DiscoverableTransform):

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
        props = dict(request.Properties or {})
        _strProperties = "\n".join(f" {key} : {value} " for key, value in props.items())
        _strSettings = "\n".join(
            f" {key} : {value} " for key, value in (request.TransformSettings or {}).items()
        )
        log_message(
            f"ICT Article Details start value={request.Value}\n"
            f"Properties:\n{_strProperties}\nTransformSettings:\n{_strSettings}"
        )

        try:
            url = extract_url_from_request(request.Value, props)
            article = download_article_text(url)
            title = str(article.get("title", "") or "").strip() or url
            text = str(article.get("text", "") or "").strip()
            publish_date = str(article.get("publish_date", "") or "").strip()
            download_method = str(article.get("download_method", "") or "").strip()

            entity = response.addEntity("ict.ArticleDetails", title)
            entity.addProperty("theurl", "url", value=url)
            entity.addProperty("content_Article", "content_Article", value=text)
            entity.addProperty("data", "data", value=publish_date)
            entity.addProperty("ICT.Article.DownloadMethod", value=download_method)

            if text:
                entity.setBookmark(BOOKMARK_COLOR_GREEN)
                entity.setNote(text[:8000])
            else:
                warn_msg = f"WARNING articolo vuoto: {url}"
                entity.setBookmark(BOOKMARK_COLOR_PURPLE)
                entity.setNote(warn_msg)
                response.addUIMessage(warn_msg, UIM_TYPES["partial"])
                log_message(warn_msg)

            log_message(
                f"ICT Article Details success: url={url} title_len={len(title)} "
                f"text_len={len(text)} method={download_method}"
            )
        except Exception as exc:
            err = f"ICT Article Details error: {exc}"
            log_message(err)
            response.addUIMessage(err, UIM_TYPES["partial"])
            fallback_value = str(request.Value or "").strip() or "article"
            entity = response.addEntity("ict.ArticleDetails", f"ERROR: {fallback_value[:120]}")
            entity.setBookmark(BOOKMARK_COLOR_RED)
            entity.setNote(err)

    def  GetHTML_LXML(url,*_listParams,**_dictParams):


        import requests
        from readability import Document
        from lxml import html

        _strResponse=""
        """  variabile che contiene il testo della  pagina HTML  """
        
        """ 
        ///infoTag: non serve a nulla perchè  se una pagina che carica il codice dinamicamente in JS devono essere eseguiti da  Selenium, Playwright, o Puppeteer:
        import requests
        from bs4 import BeautifulSoup

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        log_message(soup.prettify())

        """

        # Scarica il contenuto della pagina web
        response = requests.get(url)
        doc = Document(response.text)

        if not doc or  response.text=="":
            raise Exception(f"anche con LXML  non vi è risultato per : {url}")

        # Parsing del contenuto HTML con lxml
        tree = html.fromstring(response.content)

        # Estrarre il titolo e il contenuto principale
        title = doc.title()
        summary = doc.summary()


        # Stampa il titolo
        log_message("Titolo:", title)

        # Stampa il testo dell'articolo (contenuto semplificato)
        log_message("\nTesto dell'articolo:")
        log_message(summary)

        # Estrazione delle immagini
        log_message("\nImmagini trovate:")
        images = tree.xpath('//img/@src')
        for image in images:
            log_message(image)

        log_message("\n senza  HTML :\n")
        log_message(doc.get_clean_html())


        # Estrazione dei link presenti nella pagina
        log_message("\nLink presenti nella pagina:")
        links = tree.xpath('//a/@href')
        for link in links:
            log_message(link)


        return summary


