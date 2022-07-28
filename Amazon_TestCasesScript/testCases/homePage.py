from selenium import webdriver
import chromedriver_autoinstaller

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()


base_URL="https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
link_email_xpath='//*[@id="ap_email"]'
link_email_Continue='//*[@id="continue"]'
textbox_password_xpath='//*[@id="ap_password"]'
button_signin_xpath='//*[@id="signInSubmit"]'
password_error_xpath='//*[@id="auth-error-message-box"]/div/h4'

def login():
    driver.get(base_URL)

    driver.maximize_window()

def enterEmailOrPhnum(email):
    driver.find_element(by=By.XPATH, value =link_email_xpath).send_keys(email)
def continueButton ():
    driver.find_element(by=By.XPATH, value=link_email_Continue)
    driver.find_element(by=By.XPATH, value=link_email_Continue).click()

#for password functionality
def enterPassword (password):
    driver.find_element(by=By.XPATH, value = textbox_password_xpath)
    driver.find_element(by=By.XPATH, value = textbox_password_xpath).send_keys(password)
def signIn ():
    driver.find_element(by = By.XPATH, value =button_signin_xpath)
    driver.find_element(by = By.XPATH, value =button_signin_xpath).click()
    
#after login home page is displayed or not and check the title  
def TC_homePage_001():
    login()
    enterEmailOrPhnum("anushamurapaka@gmail.com")
    continueButton()
    enterPassword("ANUSHA@20")
    signIn()
    
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'nav-logo-sprites')))
    driver.find_element(by=By.XPATH,value='//*[@id="nav-logo-sprites"]').click()
    password_er = driver.title
    if(password_er == "Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"):
        print("TC_homePage_001 : Pass")
        assert True
    else:
        print("TC_homePage_001 : Fail")
        assert False
    

#user name is displayed on home page or not
def TC_homePage_003():
    userName=driver.find_element(by=By.XPATH,value='//*[@id="nav-link-accountList"]/div').text
    if(userName=="Hello, Anusha"):
        print("TC_homePage_003:pass")
        assert True
    else:
        print("TC_homePage_003:fail")
        assert False
        
#featured products are displayed on home page  
def TC_homePage_004():
    products=driver.find_element(by=By.XPATH,value='//*[@id="nav-xshop"]/a[2]').text
    if(products=="Buy Again"):
        print("TC_homePage_004:pass")
        assert True
    else:
        print("TC_homePage_004:fail")
        assert False
#search functinality       
def TC_homePage_005():
    search=driver.find_element(by=By.XPATH,value='//*[@id="nav-search-bar-form"]/div[2]/div[1]')
    if(search):
        print("TC_homePage_005:pass")
        assert True
    else:
        print("TC_homePage_005:fail")
        assert False

#    
def TC_homePage_007():
    product=driver.find_element(by=By.PARTIAL_LINK_TEXT,value="ADISA Women's &…").click()
    if(product):
        print("TC_homePage_007:pass")
        assert True
    else:
        print("TC_homePage_007:fail")
        assert False
    

def TC_homePage_009():
    driver.find_element(by=By.XPATH,value='//*[@id="nav-logo-sprites"]').click()
    driver.find_element(by=By.XPATH,value='//*[@id="nav-link-accountList"]').click()
    account=driver.find_element(by=By.XPATH,value='//*[@id="a-page"]/div[2]/div/div[1]/h1').text
    if(account=="Your Account"):
        print("TC_homePage_009:pass")
        assert True
    else:
        print("TC_homePage_009:fail")
        assert False
    
    
TC_homePage_001()
TC_homePage_003()
TC_homePage_004()
TC_homePage_005()
TC_homePage_007()

TC_homePage_009()


    
    
    
    
    
    
    
    
    
    
    
    