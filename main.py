from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import json

class ApplyCreditCard:
    def __init__(self, data):
        """Parameter initialization"""

        self.fname = data['first_name']
        self.lname = data['last_name']
        self.mname = data['middle_init']
        self.suffix = data['suffix']
        self.mail = data['mail']
        self.city = data['city']
        self.state = data['state']
        self.zip = data['zip']
        self.dob = data['dob']
        self.mmn = data['mmn']
        self.email = data['email']
        self.ssn = data['ssn']
        self.gross = data['gross']
        self.house = data['resident_type']
        self.work = data['Primary_inco_sour']
        self.phone = data['phone']
        self.driver = webdriver.Chrome(data['driver-path'])

    def chase(self):
        """Apply to Chase Cards"""
        self.driver.get('https://applynow.chase.com/FlexAppWeb/renderApp.do?SPID=GJ8J&CELL=61DS')

        self.driver.find_element_by_id('sFirstName').send_keys(self.fname)
        self.driver.find_element_by_id('sMiddleInitial').send_keys(self.mname)
        self.driver.find_element_by_id('sLastName').send_keys(self.lname)
        self.driver.find_element_by_id('sSuffix').send_keys(self.suffix)
        self.driver.find_element_by_id('sStreetAddr1').send_keys(self.mail)
        self.driver.find_element_by_id('sCity').send_keys(self.city)
        self.driver.find_element_by_id('sState1').send_keys(self.state)
        self.driver.find_element_by_id('sZip').send_keys(self.zip)
        self.driver.find_element_by_id('sDOB').send_keys(self.dob)
        self.driver.find_element_by_id('sMaidenName').send_keys(self.mmn)
        self.driver.find_element_by_id('sEMailAddr2').send_keys(self.email)
        self.driver.find_element_by_id('sSSN').send_keys(self.ssn)
        self.driver.find_element_by_id('currency').send_keys(self.gross)
        self.driver.find_element_by_id('sHousingType').send_keys(self.house)
        self.driver.find_element_by_id('sPosition').send_keys(self.work)
        self.driver.find_element_by_id('sHomePhone').send_keys(self.phone)
        self.driver.close()

    def americanExpress(self):
        """Apply to AmericanExpress Cards"""
        self.driver.get('https://www.americanexpress.com/us/credit-cards/card-application/apply/bluebusinesscash-credit-card/45094-9-0?intlink=US-Acq-GCP-BusinessCards-ViewAllCards-Apply-BlueBusinessCash#/')

        self.driver.close()

    def apply(self):
        """Apply to Cards"""

        self.chase()
        time.sleep(5)
        self.americanExpress()
        time.sleep(5)

if __name__ == '__main__':

    with open('config.json') as f:
        data = json.load(f)

    bot = ApplyCreditCard(data)
    bot.apply()

