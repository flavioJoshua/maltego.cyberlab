from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


# Percorso assoluto al chromedriver
chrome_driver_path = "/home/flavio/Downloads/chromedriver-linux64/chromedriver"

# Opzioni del browser (facoltativo)
options = Options()
# options.add_argument("--headless")  # se vuoi senza interfaccia grafica
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("profile-directory=Profile 2")  # Sostituisci con il nome del profilo


""" 

Selenium requires a driver to interface with the chosen browser (chromedriver, edgedriver, geckodriver, etc).

In older versions of Selenium, it was necessary to install and manage these drivers yourself. You had to make sure the driver executable was available on your system PATH, or specified explicitly in code. Modern versions of Selenium handle browser and driver installation for you with Selenium Manager. You generally don’t have to worry about driver installation or configuration now that it’s done for you when you instantiate a WebDriver. Selenium Manager works with most supported platforms and browsers. If it doesn’t meet your needs, you can still install and specify browsers and drivers yourself.

Links to some of the more popular browser drivers:

Chrome:

https://developer.chrome.com/docs/chromedriver

Edge:

https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

Firefox:

https://github.com/mozilla/geckodriver

Safari:

https://webkit.org/blog/6900/webdriver-support-in-safari-10



https://storage.googleapis.com/chrome-for-testing-public/137.0.7151.68/linux64/chromedriver-linux64.zip

 cp -r ~/.config/google-chrome/* ~/Documents/code/selenium-profiles


 """
options.add_argument("user-data-dir=/home/flavio/Documents/code/selenium-profiles")
options.add_argument("profile-directory=Profile 2")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)




# Setup del servizio
service = Service(executable_path=chrome_driver_path)

# Avvio del driver
driver = webdriver.Chrome(service=service, options=options)

# Prova ad aprire una pagina
driver.get("https://italiancyberteam.it/webmail/mail")
print(driver.title)


body_text = driver.find_element("tag name", "body").text
print(body_text)

print ("\n\n\n\n\n\n")
print (driver.page_source )
driver.quit()