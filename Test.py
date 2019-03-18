from Testowanie.Lidl_dane import Lidl
import unittest
from selenium import webdriver


class Lidlowanie(unittest.TestCase):

    def setUp(self):
        self.Lidl = Lidl
        self.driver = webdriver.Chrome(executable_path=r"C:\Testy\chromedriver")
        self.driver.get(url="https://www.lidl.pl")
        self.driver.implicitly_wait(90)
        self.driver.maximize_window()

    def test_lidlowu(self):
        self.Lidl.pokaz_lidl(self)
        self.Lidl.navigate_to_oferta_spozywcza(self)
        self.Lidl.navigate_to_bulka_poznanska(self)

    def teardown(self):
        self.driver.close ()

    def sprawdzenie(self):
        title = self.driver.title
        expected_url = "https://www.lidl.pl/pl/Nasza-odpowiedzialnosc.htm"
        self.assertIn(expected_url, self.driver.current_url)
        print (title)


#!/usr/bin/python

HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

print(HEADER, "Well done!", OKBLUE, "You have seen the Lidl site,", OKGREEN,"how cool is that?!")

