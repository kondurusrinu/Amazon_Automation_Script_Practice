from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
#after clicking to the proceed to buy option it will redirecting to address page or not  
def getProductsViaScrollDown() :

    element = driver.find_element(by = By.XPATH, value ='//*[@id="addres-select"]/h1')
    
    action = ActionChains(driver)
    
    action.moveToElement(element).build().perform()
       
       
def TC_Addresspage_001():
    login()
    enterEmailOrPhnum("7674084250")
    continueButton()
    enterPassword("Srinu9491")
    signIn()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nav-cart"]')))
    print("Cart Located")
    WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/div/div[1]/div[3]/div/a[5]'))).click()
    x = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/div[1]/div[1]/h1'))).text
    print(x)    
    #driver.find_element(by=By.XPATH,value='//*[@id="nav-cart"]').click()
    print("Cart clicked")
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[1]/div[1]/div/form/div/div[3]/span/span/input')))
    driver.find_element(by=By.XPATH,value='/html/body/div[1]/div[2]/div[3]/div[4]/div/div[1]/div[1]/div/form/div/div[3]/span/span/input').click()
    element = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="addres-select"]/h1'))).text
    #element=driver.find_element(by = By.XPATH, value='//*[@id="addres-select"]/h1').text
    print(element)
    if(element=="Select a delivery address"):
        print("TC_Addresspage_001:pass")
        assert True
    else:
        print("TC_Addresspage_001:fail")
        assert False

def TC_Addresspage_005():
    login()
    enterEmailOrPhnum("7659834107")
    continueButton()
    enterPassword("Anusha@20")
    signIn()
    driver.find_element(by=By.XPATH,value='//*[@id="nav-cart-count"]').click()
    driver.find_element(by=By.XPATH,value='//*[@id="sc-buy-box-ptc-button"]/span/input').click()
    driver.find_element(by=By.XPATH,value='//*[@id="address-book-entry-1"]/div[3]/div[1]/div/span/a').click()
    s=driver.find_element(by=By.XPATH,value='/html/body/div[5]/div[2]/div[1]/h1').text
    if(s=="Please update the delivery address."):
        print("TC_Addresspage_005:pass")
        assert True
    else:
        print("TC_Addresspage_005:fail")
        assert False












TC_Addresspage_001()
    
    
    
    
    
    
    
    
    
    