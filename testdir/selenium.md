
Selenium requires a driver to interface with the chosen browser (chromedriver, edgedriver, geckodriver, etc).

#  titolo sds
`google-chrome-stable --version`
Google Chrome **136.0.7103.113**

ti serve la  versione  precisa  per  caricare  i chromedriver  relativi 

In **older** versions of ***Selenium***, it was necessary to install and manage these drivers yourself. You had to make sure the driver executable was available on your system PATH, or specified explicitly in code. Modern versions of Selenium handle browser and driver installation for you with Selenium Manager. You generally don’t have to worry about driver installation or configuration now that it’s done for you when you instantiate a WebDriver. Selenium Manager works with most supported platforms and browsers. If it doesn’t meet your needs, you can still install and specify browsers and drivers yourself.

Links to some of the more popular browser drivers:





https://googlechromelabs.github.io/chrome-for-testing/#stable 




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
