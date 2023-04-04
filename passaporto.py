from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager



driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

# Navigate to the website
driver.get("https://prenotami.esteri.it/Services")

