from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webdriver import WebElement
import time
import re


class WebScrapper():
    driver: webdriver.Firefox
    addressInput: WebElement
    getCoordinatesButton: WebElement
    getDirectionButton: WebElement
    latitudeInput: WebElement
    longitudeInput: WebElement

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
            By.XPATH, "//button[normalize-space()='Obtener Coordenadas GPS']")
        self.getDirectionButton = self.driver.find_element(
            By.XPATH, '//form[2]//div[3]//div[1]//button[1]')
        self.latitudeInput = self.driver.find_element(By.ID, "latitude")
        self.longitudeInput = self.driver.find_element(By.ID, "longitude")
    ''' Método utilizado para obtener latitud, longitud y código postal a partir de una dirección'''

    def searchByAddress(self, medicalCenterAddress: str):
        try:
            self.addressInput.clear()
            self.addressInput.send_keys(medicalCenterAddress)
            latitude = self.latitudeInput.get_attribute('value')
            longitude = self.longitudeInput.get_attribute('value')
            address = self.addressInput.get_attribute('value')
            self.driver.execute_script(
                "arguments[0].click();", self.getCoordinatesButton)
            timeToLiveWhile = 0
            # Esperar hasta que se actualice latitud y longitud. Ponemos un límite de 10 iteraciones en el bucle. Hay ocasiones en las que la latitud y longitud no cambia porque se ha preguntado por el mismo municipio
            while (latitude == self.latitudeInput.get_attribute('value') and longitude == self.longitudeInput.get_attribute('value') and timeToLiveWhile < 10):
                time.sleep(0.2)
                timeToLiveWhile = timeToLiveWhile + 1
            latitude = self.latitudeInput.get_attribute('value')
            longitude = self.longitudeInput.get_attribute('value')
            # print("Las coordenadas de " + medicalCenterAddress + " son " + str(latitude) + " y " +  str(longitude))
            # Comprobamos si ha obtenido el código postal
            if (address != self.addressInput.get_attribute('value')):
                address = self.addressInput.get_attribute('value')
                # Buscar 5 dígitos en la nueva address
                postalCode = re.findall(r'\d{5}', address)
                # Si la expresión regular devuelve resultados, return también el código postal
                if (len(postalCode) > 0 and len(postalCode[0]) > 0):
                    return (latitude, longitude, postalCode[0])
            # En caso contrario return solo latitud y longitud
            return (latitude, longitude)
        except Exception as e:
            print(e)
            return (None, None)

    def searchByCoordinates(self, lat, lang):
        try:
            self.latitudeInput.clear()
            self.longitudeInput.clear()
            self.latitudeInput.send_keys(lat)
            self.longitudeInput.send_keys(lang)
            address = self.addressInput.get_attribute('value')
            self.driver.execute_script(
                "arguments[0].click();", self.getDirectionButton)
            timeToLiveWhile = 0
            # Esperamos hasta que cambie la dirección (para obtener postal code). Ponemos un límite de 10 iteraciones en el bucle. Hay ocasiones en las que address no cambia porque se ha preguntado por el mismo municipio
            while (address == self.addressInput.get_attribute('value') and timeToLiveWhile < 10):
                timeToLiveWhile = timeToLiveWhile + 1
                time.sleep(0.2)
            address = self.addressInput.get_attribute('value')
            postalCode = re.findall(r'\d{5}', address)
            if (len(postalCode[0]) == 0):
                return None
            else:
                return postalCode[0]
        except:
            return (None)
