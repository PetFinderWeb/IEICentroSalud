from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
seleniumOptions = Options()
# Evita que el navegador pregunte por la localización
seleniumOptions.set_preference("geo.enabled", False)
driver = webdriver.Firefox(
    options=seleniumOptions
)
driver.get("https://www.coordenadas-gps.com/")
adContent = driver.find_element(By.ID, "ad-content")
driver.execute_script("arguments[0].scrollIntoView();", adContent)
time.sleep(3)
addressInput = driver.find_element(By.ID, "address")
addressInput.clear()
addressInput.send_keys("Carrer Bisbe Orbe, Alcoy")
addressInput.send_keys(Keys.RETURN)
getCoordinatesButton = driver.find_element(By.XPATH, '//button[text()="Obtener Coordenadas GPS"]')
getCoordinatesButton.click()





# getCoordinatesButton = driver.find_element(By.XPATH, '//button[text()="Obtener Coordenadas GPS"]')
# getCoordinatesButton.click()
# assert "No results found." not in driver.page_source
# driver.close()