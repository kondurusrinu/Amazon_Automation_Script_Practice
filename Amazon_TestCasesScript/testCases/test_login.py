from selenium import webdriver
from pageObjects.signUpPage import SignUpPage
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller

#It will install ChromeDriver Automatically
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

base_URL = "https://www.amazon.com/"
link_linktext = "Hello, Sign in"
button_creatAccount_id = "createAccountSubmit"
textbox_name_id = "ap_customer_name"
textbox_mobilePhoneOrEmail_id = "ap_email"
link_countryCode_linktext = "US +1"
link_countryCode_in_xpath = '//*[@id="a-popover-1"]/div/div/ul/li[93]'
textbox_password_id = "ap_password"
textbox_ReenterPassword_id = "ap_password_check"
button_signUp_id = "continue"
    
class TS_001_signUp:  
     
    @staticmethod        
    def TC_Amazon_SignUp_001():
        print("Please Check all the Text, Text boxes and  buttons etc., are placed correctly as per the requirment  ")
        
    def __init__(self):   
        pass
    def driverInit(self, driver):
        self.driver= driver    
    
    def clickURL(self, base_URL):
        self.driver.get(self.base_URL)
        
    def clickSignInLinkText(self):
        self.driver.find_element(by=By.LINK_TEXT, value = self.link_linktext).click()
        
    def clickCreateAccount(self):
        self.driver.find_element(by=By.ID, value = self.button_creatAccount_id).click()
        
    def setName(self, name):
        self.driver.find_element(by=By.ID, value = self.textbox_name_id).clear()
        self.driver.find_element(by=By.ID, value = self.textbox_name_id).send_keys(name)
        
    def setPhoneNumber(self, phoneNumber):
        self.driver.find_element(by=By.ID, value = self.textbox_mobilePhoneOrEmail_id).clear()
        self.driver.find_element(by=By.ID, value = self.textbox_mobilePhoneOrEmail_id).send_keys(phoneNumber)
        
    def setEmail(self, email):
        self.driver.find_element(by=By.ID, value = self.textbox_mobilePhoneOrEmail_id).clear()
        self.driver.find_element(by=By.ID, value = self.textbox_mobilePhoneOrEmail_id).send_keys(email)
        
    def clickCountryCode(self):
        self.driver.find_element(by=By.ID, value = self.link_countryCode_in_linktext).click()
        
    def clickCountryCodeIndia(self):
        #Select country = new Select(self.driver.find_element(by = By.LINK_TEXT, value = self.link_countryCode_linktext))
        self.driver.find_element(by=By.ID, value = self.link_countryCode_linktext).click()
        
    def setPassword(self, password):
        self.driver.find_element(by=By.ID, value = self.textbox_password_id).clear()
        self.driver.find_element(by=By.ID, value = self.textbox_password_id).send_keys(password)
        
    def setReenterPassword(self, password):
        self.driver.find_element(by=By.ID, value = self.textbox_ReenterPassword_id).clear()
        self.driver.find_element(by=By.ID, value = self.textbox_ReenterPassword_id).send_keys(password)
        
    def clickContinue(self):
        self.driver.find_element(by=By.LINK_TEXT, value = self.button_signUp_id).click()
    
        
    @staticmethod
    def TC_Amazon_SignUp_002(self):
        self.driverInit(driver)
        self.clickURL(base_URL)
        self.clickSignInLinkText()
        self.clickCreateAccount()
        self.clickContinue()
        name_er = driver.find_element(by = By.ID, value = "auth-customerName-missing-alert").text
        phone_er = driver.find_element(by = By.ID, value = "auth-email-missing-alert").text
        password_er = driver.find_element(by = By.ID, value = "auth-password-missing-alert").text
        print(name_er)
        if(name_er == "Enter your name"):
            print("Pass")
            assert True
        else:
            print("Fail")
            assert False
                
        
signUp = TS_001_signUp()
signUp.TC_Amazon_SignUp_001()
signUp.TC_Amazon_SignUp_002()
            
        
        