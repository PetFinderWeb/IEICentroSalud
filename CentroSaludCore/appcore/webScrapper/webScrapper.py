from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_argument(
    ("prefs", {"profile.default_content_setting_values.notifications": 1})
)

driver = webdriver.Firefox(
    options=option
)
driver.get("https://www.coordenadas-gps.com/")
# waiting = WebDriverWait(driver, 10);
# driver.switch_to.alert()
elem = driver.find_element(By.ID, "address")
elem.clear()
elem.send_keys("Carrer Bisbe Orbe, Alcoy")
elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()