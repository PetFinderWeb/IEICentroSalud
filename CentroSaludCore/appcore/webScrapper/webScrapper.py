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
addressInput.send_keys("Godella")
addressInput.send_keys(Keys.RETURN)
getCoordinatesButton = driver.find_element(By.XPATH, '//button[text()="Obtener Coordenadas GPS"]')
getCoordinatesButton.click()

latitudeInput = driver.find_element(By.ID, "latitude")
longitudeInput = driver.find_element(By.ID, "longitude")
latitude = latitudeInput.get_attribute('value')
longitude = longitudeInput.get_attribute('value')
while (latitude == latitudeInput.get_attribute('value') or longitude == longitudeInput.get_attribute('value')):
    time.sleep(0.2)
latitude = latitudeInput.get_attribute('value')
longitude = longitudeInput.get_attribute('value')
print('la latitud de Godella es ' + latitude + ' y la longitud es ' + longitude)





# getCoordinatesButton = driver.find_element(By.XPATH, '//button[text()="Obtener Coordenadas GPS"]')
# getCoordinatesButton.click()
# assert "No results found." not in driver.page_source
# driver.close()