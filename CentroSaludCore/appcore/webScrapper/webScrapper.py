from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import re


class WebScrapper():
    def __init__(self):
        seleniumOptions = Options()
        # Evita que el navegador pregunte por la localización
        seleniumOptions.set_preference("geo.enabled", False)
        self.driver = webdriver.Firefox(
            options=seleniumOptions
        )
        self.driver.get("https://www.coordenadas-gps.com/")
        adContent = self.driver.find_element(By.ID, "ad-content")
        # Es necesario hacer scroll para poder interactuar con los botones
        self.driver.execute_script("arguments[0].scrollIntoView();", adContent)
        # Esperar porque la página web cambia el valor de address tras hacer scroll
        time.sleep(3)
        self.addressInput = self.driver.find_element(By.ID, "address")
        self.getCoordinatesButton = self.driver.find_element(
            By.XPATH, '//button[text()="Obtener Coordenadas GPS"]')
        self.getDirectionButton = self.driver.find_element(
            By.XPATH, '//button[text()="Obtener Dirección"]')
        self.latitudeInput = self.driver.find_element(By.ID, "latitude")
        self.longitudeInput = self.driver.find_element(By.ID, "longitude")

    ''' Método utilizado para obtener latitud, longitud y código postal a partir de una dirección'''

    def searchByAddress(self, medicalCenterAddress: str):
        self.addressInput.clear()
        self.addressInput.send_keys(medicalCenterAddress)
        self.addressInput.send_keys(Keys.RETURN)
        latitude = self.latitudeInput.get_attribute('value')
        longitude = self.longitudeInput.get_attribute('value')
        self.getCoordinatesButton.click()
        # Esperar hasta que se actualice latitud y longitud
        while (latitude == self.latitudeInput.get_attribute('value') or longitude == self.longitudeInput.get_attribute('value')):
            time.sleep(0.2)
        latitude = self.latitudeInput.get_attribute('value')
        longitude = self.longitudeInput.get_attribute('value')
        address = self.addressInput.get_attribute('value')
        postalCode = re.findall(r'\d+', address)
        if (len(postalCode) == 0):
            self.getDirectionButton.click()
            while (address == self.addressInput.get_attribute('value')):
                time.sleep(0.2)
            address = self.addressInput.get_attribute('value')
            postalCode = re.findall(r'\d+', address)   
        if (len(postalCode) == 0):
            postalCode = None
        else:
            postalCode = postalCode[0]            
        
        print(medicalCenterAddress + '. Latitud: ' + latitude +
              '. Longitud: ' + longitude + '. Código postal: ' + postalCode)
        return (latitude, longitude, postalCode[0])


webScrapper = WebScrapper()
webScrapper.searchByAddress('godella')
