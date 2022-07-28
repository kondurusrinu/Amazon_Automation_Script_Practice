from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
    
signUp_URL = "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
link_email_xpath="//*[@id='ap_email']"
link_email_Continue="//*[@id='continue']"
textbox_password_xpath='//*[@id="ap_password"]'
button_signin_xpath='//*[@id="signInSubmit"]'

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
           
def get_URL():
    driver.get(signUp_URL)
    driver.maximize_window()
    
def enterEmailOrPhnum(email):
    driver.find_element(by=By.XPATH, value =link_email_xpath).send_keys(email)
    
def continueButton ():
    driver.find_element(by=By.XPATH, value=link_email_Continue)
    driver.find_element(by=By.XPATH, value=link_email_Continue).click()
    
def enterPassword (password):
    driver.find_element(by=By.XPATH, value = textbox_password_xpath)
    driver.find_element(by=By.XPATH, value = textbox_password_xpath).send_keys(password)

def signIn ():
    driver.find_element(by = By.XPATH, value =button_signin_xpath)
    driver.find_element(by = By.XPATH, value =button_signin_xpath).click()
    
def TC_Amazon_ProductSupport_002():
    get_URL()
    enterEmailOrPhnum("7674084250")
    continueButton()
    enterPassword("Srinu9491")
    signIn()
    driver.find_element(by = By.ID, value = "nav-search-dropdown-card").click()

    select = Select(driver.find_element(by = By.ID, value = "searchDropdownBox"))
    time.sleep(2)
    select.select_by_visible_text('Watches')
    ele = driver.find_element(by = By.XPATH, value ='//*[@id="searchDropdownBox"]/option[42]').text
    # actions = ActionChains(driver)
    # actions.move_to_element(ele).perform()
    # driver.find_element(by = By.XPATH, value = '//*[@id="nav-search-dropdown-card"]').click()
    if(ele == "Watches"):
        print("TC_Amazon_SignUp_002 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_002 : Fail")
        assert False
        
def TC_Amazon_ProductSupport_003():
    get_URL()
    enterEmailOrPhnum("7674084250")
    continueButton()
    enterPassword("Srinu9491")
    signIn()
    driver.find_element(by = By.ID, value = "nav-search-dropdown-card").click()

    select = Select(driver.find_element(by = By.ID, value = "&searchDropdownBox"))
    time.sleep(2)
    select.select_by_visible_text('Watches')
    ele = driver.find_element(by = By.XPATH, value ='//*[@id="searchDropdownBox"]/option[42]').text
    if(ele == "Watches"):
        print("TC_Amazon_SignUp_003 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_003 : Fail")
        assert False

TC_Amazon_ProductSupport_002()
    
