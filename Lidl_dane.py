from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Lidl:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get()
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    def pokaz_lidl(self):
        self.driver.get(url="https://www.lidl.pl")
        self.driver.implicitly_wait(30)

    def navigate_to_oferta_spozywcza(self):
        self.driver.find_element(By.XPATH, "//span[contains(.,'Oferta spożywcza')]").click()
        self.driver.implicitly_wait (90)

    def navigate_to_bulka_poznanska(self):
        self.driver.find_element(By.XPATH, "//a[contains(@href, '/pl/Nasza-odpowiedzialnosc.htm')]").click()
        self.driver.implicitly_wait (90)

    def teardown(self):
        self.driver.close()

