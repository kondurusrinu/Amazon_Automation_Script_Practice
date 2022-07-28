from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

signUp_URL = "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
logIn_URL="https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
signUp_a_URL = "https://www.amazon.in/ap/register?showRememberMe=true&openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26useRedirectOnSuccess%3D1%26signIn%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&prevRID=32F1QPJ51FX6HNPZ3RHT&openid.assoc_handle=inflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&pageId=inflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&mobileBrowserWeblabTreatment=C"   
#link_linktext = "Hello, Sign in"
link_linktext = "//*[@id='nav-link-accountList']"
button_creatAccount_id = "createAccountSubmit"
textbox_name_id = "ap_customer_name"
textbox_mobilePhone= "ap_phone_number"
textbox_email="ap_email"
link_countryCode_xpath = '//*[@id="auth-country-picker-container"]/span/span'
link_countryCode_in_xpath = '//*[@id="auth-country-picker_92"]'
textbox_password_id = "ap_password"

button_signUp_id = "continue"


link_email_xpath="//*[@id='ap_email']"
link_email_Continue="//*[@id='continue']"
textbox_password_xpath='//*[@id="ap_password"]'
button_signin_xpath='//*[@id="signInSubmit"]'
password_error_xpath='//*[@id="auth-error-message-box"]/div/div/ul/li/span'
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

def get_URL():
    driver.get(signUp_URL)
    driver.maximize_window()
    
def a_get_URL():
    driver.get(signUp_a_URL)
    driver.maximize_window()

def clickSignInLinkText():
    try:
        driver.find_element(by=By.XPATH, value = link_linktext).click()
    except:
        pass
    
def setName( name):
    driver.find_element(by=By.ID, value = textbox_name_id).clear()
    driver.find_element(by=By.ID, value = textbox_name_id).send_keys(name)
    
def setPhoneNumber(phoneNumber):
    driver.find_element(by=By.ID, value = textbox_mobilePhone).clear()
    driver.find_element(by=By.ID, value = textbox_mobilePhone).send_keys(phoneNumber)
    
def setEmail(email):
    driver.find_element(by=By.ID, value = textbox_email).clear()
    driver.find_element(by=By.ID, value = textbox_email).send_keys(email)
    
def clickCountryCodeIndia():
    a = ActionChains(driver)
    m = driver.find_element(by = By.XPATH, value = '//*[@id="auth-country-picker-container"]/span/span')
    a.move_to_element(m).click().perform()
    n = driver.find_element(by = By.LINK_TEXT, value = 'India +91')
    a.move_to_element(n).click().perform()
    #driver.find_element(by=By.XPATH, value = link_countryCode_in_xpath).click()
    
def setPassword(password):
    driver.find_element(by=By.ID, value = textbox_password_id).clear()
    driver.find_element(by=By.ID, value = textbox_password_id).send_keys(password)    

def clickContinue():
    time.sleep(3)
    driver.find_element(by=By.ID, value = button_signUp_id).click()
      
def login():
    driver.get(logIn_URL)

    driver.maximize_window()
    
def clickCreateAccount() :
    driver.find_element(by=By.ID, value = button_creatAccount_id).click()
        
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


def TC_Amazon_Integration_001():
    a_get_URL()
    setName("Anusha")
    setPhoneNumber("7857484397")
    
    clickCountryCodeIndia()
    setEmail("anuu45@gmail.com")
    setPassword("anusha#45")
    
    clickContinue()
    WebDriverWait(driver,200).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1').text
    
    if(verify == "Verify mobile number"):
        print("TC_Amazon_Integration_001: Pass")
        assert True
    else:
        print("TC_Amazon_Integration_001 : Fail")
        assert False
    
#Fill all the mandatory fields then user should be able to register    
def TC_Amazon_Integration_002():
    a_get_URL()
    setName("Anusha")
    setPhoneNumber("7898994397")
    
    clickCountryCodeIndia()

    setPassword("anusha#45")
    
    clickContinue()
    WebDriverWait(driver,200).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1').text
    
    if(verify == "Verify mobile number"):
        print("TC_Amazon_Integration_002: Pass")
        assert True
    else:
        print("TC_Amazon_Integration_002: Fail")
        assert False
    

#user enter registered mobile number then it should redirect to password page
def TC_Amazon_Integration_003():
    login()
    enterEmailOrPhnum("7659834107")
    continueButton()
    nextPage= driver.find_element(by = By.XPATH, value='//*[@id="authportal-main-section"]/div[2]/div[1]/div/div/form/div/div[1]/div[1]/div[1]/label' ).text
    if(nextPage == "Password"):
        print("TC_Amazon_Integration_003:Pass")
        assert True
    else:
        print("TC_Amazon_Integration_003:Fail")
        assert False
# user enter registered Email id then it should redirect to password page
def TC_Amazon_Integration_004():
    driver.find_element(by=By.XPATH,value='//*[@id="ap_change_login_claim"]').click()
    login()
    enterEmailOrPhnum("anushamurapaka20@gmail.com")
    continueButton()
    nextPage= driver.find_element(by = By.XPATH, value='//*[@id="authportal-main-section"]/div[2]/div[1]/div/div/form/div/div[1]/div[1]/div[1]/label' ).text
    if(nextPage == "Password"):
        print("TC_Amazon_Integration_004:Pass")
        assert True
    else:
        print("TC_Amazon_Integration_004:Fail")
        assert False
    
#when user click forgot password then it should redirect to Password Assistance page    
def TC_Amazon_Integration_005():
    
    driver.find_element(by=By.XPATH, value="//*[@id='auth-fpp-link-bottom']").click()
    clickForgotPassword=driver.find_element(by=By.XPATH, value="//*[@id='authportal-main-section']/div[2]/div/div[1]/div/form/h1").text
    if(clickForgotPassword=="Password assistance"):
        print("TC_Amazon_Integration_005:pass")
        assert True
    else:
        print("TC_Amazon_Integration_005:fail")
        assert False
#user enter valid password then it should redirect to Amazon home page        
def TC_Amazon_Integration_006():
    
    login()
    enterEmailOrPhnum("anushamurapaka20@gmail.com")
    continueButton()
    driver.find_element(by=By.XPATH, value = "//*[@id='ap_password']").send_keys("")
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'nav-logo-sprites')))
    try:
        driver.find_element(by=By.XPATH,value='//*[@id="nav-logo-sprites"]').click()
    except:
        pass
    
    password_er = driver.title
    if(password_er =="Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in"):
        print("TC_Amazon_Integration_006:Pass")
        assert True
    else:
        print("TC_Amazon_Integration_006:Fail")
        assert False
# user select any product in the Home page then it should redirect to product specification page
def TC_Amazon_Integration_007():
    time.sleep(3)
    driver.find_element(by=By.XPATH,value='//*[@id="nav-logo-sprites"]').click()
    try:
        driver.find_element(by=By.PARTIAL_LINK_TEXT,value='Apple iPhone 11').click()
    except:
        pass
    #driver.switch_to.window(driver.window_handles[1])
    product=driver.find_element(by=By.XPATH,value='//*[@id="title"]').text
    if(product=="Apple iPhone 11 (128GB) - White"):
        print("TC_Amazon_Integration_007:pass")
        assert True
    else:
        print("TC_Amazon_Integration_007:fail")
        assert False
#user click on any category menu displayed in home page then it should display related products
def TC_Amazon_Integration_008():
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='//*[@id="nav-xshop"]/a[1]').click()
    menuCategory=driver.find_element(by=By.XPATH,value='//*[@id="s-refinements"]/div[1]/ul/li[1]/span/span').text
    if(menuCategory=='Electronics'):
        print("TC_Amazon_Integration_008:pass")
        assert True
    else:
        print("TC_Amazon_Integration_008:fail")
        assert False
#user should be able to  search based on product name,brand name or product specification.      
def TC_Amazon_Integration_009():
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='//*[@id="nav-logo-sprites"]').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').clear()
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys('H&M')
    try:
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
    except:
        pass
    brand=driver.find_element(by=By.LINK_TEXT, value ="Men's Fleece Hooded Hoodie").text
    if(brand=="Men's Fleece Hooded Hoodie"):
        print("TC_Amazon_Integration_009:pass")
        assert True
    else:
        print("TC_Amazon_Integration_009:Fail")
        assert False
#user should be perform search in different categories for example, Movies, Books, Grocery etc.         
def TC_Amazon_Integration_010():
    time.sleep(3)
    driver.find_element(by=By.XPATH,value='//*[@id="nav-logo-sprites"]').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').clear()
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys('Books')
    try:
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
    except:
        pass
    time.sleep(2)
    result=driver.find_element(by=By.LINK_TEXT, value ="Think & Grow Rich: THE 21st CENTURY EDITION").text
    if(result=="Think & Grow Rich: THE 21st CENTURY EDITION"):
        print("TC_Amazon_Integration_010:pass")
        assert True
    else:
        print("TC_Amazon_Integration_010:Fail")
        assert False
#when user select any product in the search results page then it should redirect to product specification page    
def TC_Amazon_Integration_011():
    time.sleep(4)
    driver.find_element(by=By.XPATH,value='//*[@id="nav-logo-sprites"]').click()
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').clear()
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input').send_keys('apple mobile')
    try:
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input').click()
    except:
        pass
    driver.find_element(by=By.LINK_TEXT, value ='Apple iPhone 11 (128GB) - White').click()
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(4)
    choosed=driver.find_element(by=By.XPATH,value='/html/body/div[4]/div[2]/div[3]/div[11]/div[3]/div/h1').text
    if(choosed=='Apple iPhone 11 (128GB) - White'):
        print("TC_Amazon_Integration_011:pass")
        assert True
    else:
        print("TC_Amazon_Integration_011:Fail")
        assert False

# Verify that user should be able to select the quantity 
def TC_Amazon_Integration_012():
    a = ActionChains(driver)
    m = driver.find_element(by = By.XPATH, value = '//*[@id="nav-link-accountList"]')
    a.move_to_element(m).perform()
    n = driver.find_element(by = By.LINK_TEXT, value = 'Sign Out')
    a.move_to_element(n).click().perform()
    #get_URL()
    enterEmailOrPhnum("7674084250")
    continueButton()
    enterPassword("Srinu9491")
    signIn()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, 'nav-search-dropdown-card')))
    driver.find_element(by = By.ID, value = "nav-search-dropdown-card").click()

    select = Select(driver.find_element(by = By.ID, value = "searchDropdownBox"))
    select.select_by_visible_text('Electronics')
    driver.find_element(by = By.ID, value = "twotabsearchtextbox").send_keys("mobile")
    try:
        driver.find_element(by = By.ID, value = "nav-search-submit-button").click()
    except:
        pass
    #driver.back()
    driver.find_element(by = By.LINK_TEXT, value = 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery').click()
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(3)
    select = Select(driver.find_element(by = By.ID, value = "quantity"))
    select.select_by_visible_text('3')
    quantity = driver.find_element(by = By.XPATH, value = '//*[@id="quantity"]').text
    if(quantity):
        print("TC_Amazon_Integration_012:pass")
        assert True
    else:
        assert False

# Verify that when user select different variant of the product then selected  variant should be displayed        
def TC_Amazon_Integration_013():
    driver.find_element(by = By.XPATH, value = '//*[@id="a-autoid-14-announce"]/div/div[1]/img').click()
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '//*[@id="a-autoid-17-announce"]').click()
    time.sleep(3)
    varient = driver.find_element(by = By.XPATH, value = '//*[@id="title"]').text
    if(varient == 'Redmi 9A Sport (Metallic Blue, 3GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery'):
        print("TC_Amazon_Integration_013:pass")
        assert True
    else:
        assert False    

# Verify that when user click on Buy Now button then the Delivery & Payment page should be displayed        
def TC_Amazon_Integration_014():
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '//*[@id="buy-now-button"]').click()
    BuyNow  = driver.find_element(by = By.XPATH, value = '//*[@id="checkoutDisplayPage"]/div/div[2]/div[1]/h1').text
    driver.back()
    if(BuyNow == 'Select a payment method'):
        print("TC_Amazon_Integration_014:pass")
        assert True
    else:
        assert False 
        
# Verify that when user click on Add to cart button then cart page should be displayed        
def TC_Amazon_Integration_015():
    time.sleep(3)
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))
    driver.find_element(by = By.ID, value = "add-to-cart-button").click()
    time.sleep(4)
    driver.find_element(by = By.XPATH, value = '//*[@id="attach-sidesheet-view-cart-button"]').click() 
    time.sleep(4)
    addToCart = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, 'Redmi 9A Sport (Metallic Blue, 3GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery'))).text
    
    
    if(addToCart == 'Redmi 9A Sport (Metallic Blue, 3GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery'):
        print("TC_Amazon_Integration_015:pass")
        assert True
    else:
        assert False 

# Verify that user should be able to continue shopping after adding items to cart.        
def TC_Amazon_Integration_016():
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '//*[@id="nav-xshop"]/a[1]').click()
    time.sleep(2)
    continue_shopping = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, 'Dog food'))).text
    driver.back()
    if(continue_shopping == 'Dog food'):
        print("TC_Amazon_Integration_016:pass")
        assert True
    else:
        assert False 

# Verify that Quantity should be changeble in cart page and amount also should be updated        
def TC_Amazon_Integration_017():        
    time.sleep(2)
    select = Select(driver.find_element(by = By.XPATH, value = '//*[@id="quantity"]'))
    select.select_by_visible_text('3')
    cart_quantity = driver.find_element(by = By.XPATH, value = '//*[@id="quantity"]').text
    if(cart_quantity):
        print("TC_Amazon_Integration_017:pass")
        assert True
    else:
        assert False

# Verify that when user clicks on delete from cart button the item should be deleted from cart.
def TC_Amazon_Integration_018():     
    time.sleep(2)        
    driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/input').click()
    time.sleep(2)
    cart_delete = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, 'Redmi 9A Sport (Metallic Blue, 3GB RAM, 32GB Storage) | 2GHz Oct...'))).text
    if(cart_delete == 'Redmi 9A Sport (Metallic Blue, 3GB RAM, 32GB Storage) | 2GHz Oct...'):
        print("TC_Amazon_Integration_018:pass")
        assert True
    else:
        assert False     

# Verify that when user click on the Proceed to buy button then delivery address page should displayed     
def TC_Amazon_Integration_019():  
    driver.find_element(by = By.XPATH, value = '//*[@id="sc-buy-box-ptc-button"]/span/input').click()
    time.sleep(2)
    continue_shopping = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="addres-select"]/h1'))).text
    if(continue_shopping == 'Select a delivery address'):
        print("TC_Amazon_Integration_019:pass")
        assert True
    else:
        assert False     

# If the user have previously saved address, then verify that when user click on Delivery to this address button then Payment page should be displayed        
def TC_Amazon_Integration_020():  
    time.sleep(2)
    driver.find_element(by = By.XPATH, value = '//*[@id="address-book-entry-0"]/div[2]/span/a').click()
    time.sleep(3)
    delivery_address  = driver.find_element(by = By.XPATH, value = '//*[@id="checkoutDisplayPage"]/div/div[2]/div[1]/h1').text
    driver.back()
    if(delivery_address == 'Select a payment method'):
        print("TC_Amazon_Integration_020:pass")
        assert True
    else:
        assert False 
 
# Verify that user should be able to redirect to payment page after Fillied all the required details and clicking on use this  address       
def TC_Amazon_Integration_021():
    time.sleep(2)
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="address-ui-widgets-enterAddressFullName"]')))
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressFullName"]').clear()
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressFullName"]').send_keys("anusha")
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressPhoneNumber"]').clear()
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressPhoneNumber"]').send_keys("7659834107")
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressPostalCode"]').clear()
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressPostalCode"]').send_keys("532001")
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressLine1"]').clear()
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressLine1"]').send_keys("vamsadara colony")
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressLine2"]').clear()
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-enterAddressLine2"]').send_keys("Illisipuram ")
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-landmark"]').clear()
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-landmark"]').send_keys("church")
    driver.find_element(by=By.XPATH,value='//*[@id="address-ui-widgets-form-submit-button"]/span/input').click()
    #driver.find_element(by=By.XPATH,value='//*[@id="shippingOptionFormId"]/div[2]/div[2]/div/span[1]').click()
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/div[1]/h1'))) 
    err=driver.find_element(by=By.XPATH, value='/html/body/div[5]/div[2]/div[1]/h1').text
    if(err=="Select a payment method"):
        print("TC_Amazon_Integration_021:pass")
        assert True
    else:
        assert False    

# Verify that user can able to add UPI method  
def TC_Amazon_Integration_022():  
    time.sleep(2)
    # driver.find_element(by = By.XPATH, value = '//*[@id="pp-S3dJfj-134"]').click()
    # driver.find_element(by = By.XPATH, value = '//*[@id="pp-S3dJfj-144"]').send_keys("234")
    actions = ActionChains(driver)
    element = driver.find_element(by = By.NAME, value = 'ppw-instrumentRowSelection')
    actions.move_to_element(element).click().perform()
    #driver.find_element(by = By.NAME, value = 'ppw-instrumentRowSelection').click()
    driver.find_element(by = By.NAME, value = 'addCreditCardVerificationNumber0').send_keys('345')
    time.sleep(3)
    driver.find_element(by = By.CLASS_NAME, value = 'a-label a-checkbox-label').click()
    UPI = driver.find_element(by = By.NAME, value = 'ppw-widgetEvent:SetPaymentPlanSelectContinueEvent').text
    
    if(UPI == ''):
        print("TC_Amazon_Integration_022:pass")
        assert True
    else:
        assert False 

# After enter the card details, verify that user click on the continue button then Place order page should be displayed        
def TC_Amazon_Integration_023():  
    time.sleep(2)
    driver.find_element(by = By.XPATH, value = '//*[@id="pp-Gp8TQD-252"]/span/input').click()
    time.sleep(3)
    delivery_address  = driver.find_element(by = By.XPATH, value = '//*[@id="checkoutDisplayPage"]/div/div[2]/div[1]/h1').text
    driver.back()
    if(delivery_address == 'Select a payment method'):
        print("TC_Amazon_Integration_023:pass")
        assert True
    else:
        assert False 
        


TC_Amazon_Integration_001()
TC_Amazon_Integration_002()
TC_Amazon_Integration_003()
TC_Amazon_Integration_004()
TC_Amazon_Integration_005()
TC_Amazon_Integration_006()
TC_Amazon_Integration_007()
TC_Amazon_Integration_008()
TC_Amazon_Integration_009()
TC_Amazon_Integration_010()
TC_Amazon_Integration_011()
TC_Amazon_Integration_012()
TC_Amazon_Integration_013()
TC_Amazon_Integration_014()
TC_Amazon_Integration_015()   
TC_Amazon_Integration_016()
TC_Amazon_Integration_017()
TC_Amazon_Integration_018()
TC_Amazon_Integration_019()
TC_Amazon_Integration_020()
TC_Amazon_Integration_021()
#TC_Amazon_Integration_022()
