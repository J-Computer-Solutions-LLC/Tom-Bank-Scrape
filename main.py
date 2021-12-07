from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, NoSuchElementException, ElementNotInteractableException
import time
import json

class ApplyCreditCard:
    def __init__(self, data):
        """Parameter initialization"""

        self.fname = data['first_name']
        self.lname = data['last_name']
        self.mname = data['middle_init']
        self.suffix = data['suffix']
        self.name_on_card = data['name_on_card']
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
        self.business = data['business_name']
        self.baddress = data['bus_address']
        self.bzip = data['bzip']
        self.bphone = data['bphone']
        self.industry = data['industry']
        self.byears = data['yearsN_business']
        self.numEmploy = data['num_of_employees']
        self.b_rev = data['anualB_rev']
        self.monthlyCost = data['monthlyCost']
        self.taxID = data['taxID']
        self.companyRole = data['companyRole']
        chromedriver_autoinstaller.install()
        options = webdriver.ChromeOptions()
        options.binary_location = "/usr/bin/google-chrome"
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument('--no-sandbox')
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome()

        self.driver.execute_script("window.open('https://www.americanexpress.com/us/credit-cards/card-application/apply/bluebusinesscash-credit-card/45094-9-0?intlink=US-Acq-GCP-BusinessCards-ViewAllCards-Apply-BlueBusinessCash#/', 'americanExpress')")
        self.driver.execute_script("window.open('https://applynow.chase.com/FlexAppWeb/renderApp.do?SPID=GJ8J&CELL=61DS', 'chase');")
        self.driver.execute_script("window.open('https://cards.barclaycardus.com/credit-card/d9b7c26c-b684-43df-96e8-8fea8d666de1?referrerid=BCSCD&xsessionid=21F89F30A127DB980A37613B54ADE190', 'barclay');")
        self.driver.execute_script("window.open('https://secure.bankofamerica.com/applynow/welcome.go', 'boatravel');")
        self.driver.execute_script("window.open('https://secure.bankofamerica.com/applynow/welcome.go', 'boacash');")
        self.driver.execute_script("window.open('https://www.alliantcreditunion.com/Clos/Clos/SignatureAgreement', 'alliant');")
        self.driver.execute_script("window.open('https://applynow.capitalone.com/?productId=14016', 'capitalonesavior');")
        self.driver.execute_script("window.open('https://secure03a.chase.com/web/oao/application/card?sourceCode=GMK8&action=guest#/origination/cardDetails/index/index;cellCode=61DS;combo=N', 'chasesapphire');")
        #self.driver.execute_script("window.open('https://secure05a.chase.com/web/oao/application/card?sourceCode=GJ3X&action=guest#/origination/cardDetails/index/indexBusinessCreditCard;cellCode=61DS;cfgCode=INDBIZCC_SNAICS;channel=C30;sourceCode=GJ3X;AOC=5686;RPC=0514;combo=N;params=,,,no,no,,,', 'chasecashink');")
        #self.driver.execute_script("window.open('https://www.schwab.com/credit-cards/platinum-card', 'americanexpressplatinumschwab');")
        self.driver.execute_script("window.open('https://www.americanexpress.com/us/credit-cards/card-application/apply/platinum-card/25330-10-0?pmccode=137&intlink=US-Acq-Shop-Consumer-PDP-Prospect-Apply-Platinum-Header#/', 'americanexpressplatinum');")
        self.driver.execute_script("window.open('https://www.americanexpress.com/us/credit-cards/card-application/apply/amex-everyday-preferred-credit-card/25330-10-0?pmccode=936&intlink=US-Acq-Shop-Consumer-PDP-Prospect-Apply-AEDP-Header#/', 'americanexpresseverday');")
        self.driver.execute_script("window.open('https://www.americanexpress.com/us/credit-cards/card-application/apply/businessgold-card/45094-9-0?intlink=US-Acq-GCP-Open-CardDetail-GoldCard-Apply-Gold#/', 'americanexpressgold');")


    def barclays(self):
        self.driver.switch_to.window('barclay')
    def chasecashink(self):
        self.driver.switch_to.window('chasecashink')
        self.driver.find_element_by_id('blx-nameBlock-firstName-text-validate-input-field').send_keys(self.fname)
    def chase(self):
        """Apply to Chase Cards"""

        self.driver.switch_to.window('chase')
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
        self.driver.find_element_by_id('sAnnualIncome').send_keys(self.gross)
        self.driver.find_element_by_id('sHousingType').send_keys(self.house)
        self.driver.find_element_by_id('sPosition').send_keys(self.work)
        self.driver.find_element_by_id('sHomePhone').send_keys(self.phone)
        time.sleep(10)
        acceptCheckBox = self.driver.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[2]/div[1]/div[5]/div[3]/div/div/div/div[5]/div[3]/div/div/label/div[1]')
        acceptCheckBox.click()
        submitButton = self.driver.find_element_by_id('flexappsubmit')
        #submitButton.click()

    def americanGold(self):
        """Apply to Chase Cards"""

        self.driver.switch_to.window('americanexpressgold')
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
        self.driver.find_element_by_id('sAnnualIncome').send_keys(self.gross)
        self.driver.find_element_by_id('sHousingType').send_keys(self.house)
        self.driver.find_element_by_id('sPosition').send_keys(self.work)
        self.driver.find_element_by_id('sHomePhone').send_keys(self.phone)
        time.sleep(10)
        acceptCheckBox = self.driver.find_element_by_xpath('/html/body/form/div[1]/div/div[1]/div[2]/div[1]/div[5]/div[3]/div/div/div/div[5]/div[3]/div/div/label/div[1]')
        acceptCheckBox.click()
        submitButton = self.driver.find_element_by_id('flexappsubmit')
        #submitButton.click()

    def americanExpress(self):
        """Apply to AmericanExpress Cards"""
        self.driver.switch_to.window("americanExpress")
        self.driver.find_element_by_id('email-32').send_keys(self.email)
        self.driver.find_element_by_id('business-name-34').send_keys(self.business)
        self.driver.find_element_by_id('business-name-on-card-36').send_keys(self.business)
        time.sleep(10)
        for i in range(10):
            try:
                checkBox = self.driver.find_element_by_xpath('//*[@id="doing-business-as-disabled-41"]')
                checkBox.send_keys(Keys.ENTER)
                checkBox.click()
                break
            except ElementClickInterceptedException as e:
                print('Retrying in 1 second')
                time.sleep(1)
        else:
            pass
        self.driver.find_element_by_id('street-address-43').send_keys(self.baddress)
        self.driver.find_element_by_id('zip-code-48').send_keys(self.bzip)
        self.driver.find_element_by_id('phone-number-57').send_keys(self.bphone)
        self.driver.find_element_by_id('industry-type-60').send_keys(self.industry)
        self.driver.find_element_by_id('years-in-business-75-list-dropdown').send_keys(self.byears)
        self.driver.find_element_by_id('number-of-employees-80').send_keys(self.numEmploy)
        self.driver.find_element_by_id('annual-business-revenue-82').send_keys(self.b_rev)
        self.driver.find_element_by_id('estimated-monthly-spend-84').send_keys(self.monthlyCost)
        self.driver.find_element_by_id('federal-tax-id-86').send_keys(self.taxID)
        self.driver.find_element_by_id('role-in-company-90-list-dropdown').send_keys(self.companyRole)
        self.driver.find_element_by_id('first-name-101').send_keys(self.fname)
        self.driver.find_element_by_id('middle-name-103').send_keys(self.mname)
        self.driver.find_element_by_id('last-name-105').send_keys(self.lname)
        self.driver.find_element_by_id('name-on-card-163').send_keys(self.name_on_card)
        self.driver.find_element_by_id('street-address-109').send_keys(self.mail)
        self.driver.find_element_by_id('zip-code-114').send_keys(self.zip)
        self.driver.find_element_by_id('phone-numer-126').send_keys(self.phone)
        self.driver.find_element_by_id('ssn-129').send_keys(self.ssn)
        self.driver.find_element_by_id('date-of-birth-132').send_keys(self.dob)
        self.driver.find_element_by_id('annual-income-135').send_keys(self.gross)
        self.driver.find_element_by_id('non-taxable-income-137').send_keys(self.gross)
        time.sleep(5)
        submitButton = self.driver.find_element_by_id('submit')
        #submitButton.click()

        self.driver.close()

    def apply(self):
        """Apply to Cards"""

        self.chase()
        self.americanExpress()
        self.chasecashink()

if __name__ == '__main__':

    with open('config.json') as f:
        data = json.load(f)

    bot = ApplyCreditCard(data)
    bot.apply()
