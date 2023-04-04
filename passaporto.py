from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options


def set_options():
    firefox_options = Options()

    #firefox_options.add_argument('--headless')

    driver = webdriver.Firefox(options=firefox_options, executable_path=GeckoDriverManager().install())
    return driver

# Navigate to the website

driver = set_options()
driver.get("https://prenotami.esteri.it/Services")
print("hello")

