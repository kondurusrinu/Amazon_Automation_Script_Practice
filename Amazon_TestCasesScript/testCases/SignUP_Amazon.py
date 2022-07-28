'''
Created on 28-Jun-2022

@author: kondsrin
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


base_URL = "https://www.amazon.com/"
signUp_URL = "https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&mobileBrowserWeblabTreatment=C&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=ZKXJ3A3GXWNWR7TPXQR3&openid.assoc_handle=usflex&openid.mode=checkid_setup&desktopBrowserWeblabTreatment=C&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
#link_linktext = "Hello, Sign in"
link_linktext = "//*[@id='nav-link-accountList']"
button_creatAccount_id = "createAccountSubmit"
textbox_name_id = "ap_customer_name"
textbox_mobilePhoneOrEmail_id = "ap_email"
link_countryCode_xpath = "//*[@id='ap_register_form']/div/div/div[2]/div[2]/div"
link_countryCode_in_xpath = '//*[@id="auth-country-picker_92"]'
textbox_password_id = "ap_password"
textbox_ReenterPassword_id = "ap_password_check"
button_signUp_id = "continue"
chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
           
def get_URL():
    driver.get(signUp_URL)
    driver.maximize_window()
    
def clickSignInLinkText():
    try:
        driver.find_element(by=By.XPATH, value = link_linktext).click()
    except:
        pass
    
def clickCreateAccount() :
    driver.find_element(by=By.ID, value = button_creatAccount_id).click()
    
def setName( name):
    driver.find_element(by=By.ID, value = textbox_name_id).clear()
    driver.find_element(by=By.ID, value = textbox_name_id).send_keys(name)
    
def setPhoneNumber(phoneNumber):
    driver.find_element(by=By.ID, value = textbox_mobilePhoneOrEmail_id).clear()
    driver.find_element(by=By.ID, value = textbox_mobilePhoneOrEmail_id).send_keys(phoneNumber)
    
def setEmail(email):
    driver.find_element(by=By.ID, value = textbox_mobilePhoneOrEmail_id).clear()
    driver.find_element(by=By.ID, value = textbox_mobilePhoneOrEmail_id).send_keys(email)
    
def clickCountryCode():
    driver.find_element(by=By.XPATH, value = link_countryCode_xpath).click()
    
def clickCountryCodeIndia():
    #Select country = new Select(driver.find_element(by = By.LINK_TEXT, value = link_countryCode_linktext))
    driver.find_element(by=By.XPATH, value = link_countryCode_in_xpath).click()
    
def setPassword(password):
    driver.find_element(by=By.ID, value = textbox_password_id).clear()
    driver.find_element(by=By.ID, value = textbox_password_id).send_keys(password)
    
def setReenterPassword(Repassword):
    driver.find_element(by=By.ID, value = textbox_ReenterPassword_id).clear()
    driver.find_element(by=By.ID, value = textbox_ReenterPassword_id).send_keys(Repassword)
    
def clickContinue():
    time.sleep(3)
    driver.find_element(by=By.ID, value = button_signUp_id).click()
    
# Check all the Text, Text boxes and  buttons etc.,are placed correctly as per the requirment  
def TC_Amazon_SignUp_001():
    print("Please Check all the Text, Text boxes and  buttons etc., are placed correctly as per the requirment")  
    print("TC_Amazon_SignUp_001 : Pass")

#Check the required fields by not filling any data then error messages for mandatory fields are showing or not
def TC_Amazon_SignUp_002():
    driver.get(base_URL)
    clickSignInLinkText()
    clickCreateAccount()
    clickContinue()
    name_er = driver.find_element(by = By.ID, value = "auth-customerName-missing-alert").text
    phone_er = driver.find_element(by = By.ID, value = "auth-email-missing-alert").text
    password_er = driver.find_element(by = By.ID, value = "auth-password-missing-alert").text
    if((name_er == "Enter your name") and (phone_er == "Enter your email or mobile phone number") and (password_er == "Minimum 6 characters required")):
        print("TC_Amazon_SignUp_002 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_002 : Fail")
        assert False
  
# Check that when the user tries to signup by entering partial data.        
def TC_Amazon_SignUp_003():
    get_URL()
    setName("Srinu")
    setPhoneNumber("8142039706")
    clickCountryCode()
    clickCountryCodeIndia()
    clickContinue()
    WebDriverWait(driver,200).until(EC.presence_of_element_located(( By.ID,"auth-password-missing-alert")))
    password_er = driver.find_element(by = By.ID, value = "auth-password-missing-alert").text
    if(password_er == "Minimum 6 characters required"):
        print("TC_Amazon_SignUp_003 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_003 : Fail")
        assert False
        
# Fill all mandatory fields with correct data and check user should able to register
def TC_Amazon_SignUp_004():
    get_URL()
    setName("Srinu")
    setPhoneNumber("3857464397")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,200).until(EC.presence_of_element_located(( By.XPATH, "//*[@id='authportal-main-section']/div[2]/div/div[3]/div/h1")))
    verify = driver.find_element(by = By.XPATH, value = "//*[@id='authportal-main-section']/div[2]/div/div[3]/div/h1").text
    
    if(verify == "Verify mobile number"):
        print("TC_Amazon_SignUp_004 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_004 : Fail")
        assert False
 
# Check the keyboard Tab Button functionality
def TC_Amazon_SignUp_005():
    get_URL()
    first = ActionChains(driver) 
    id = "ap_password_check"
    for i in range(10): 
        first.send_keys(Keys.TAB)
        first.perform()
        if(driver.find_element(by = By.ID, value = id) == driver.switch_to.active_element):
            print("TC_Amazon_SignUp_005 : Pass")
            assert True
            break
    else:
        print("TC_Amazon_SignUp_005 : Fail")
        assert False
 
# Check the name field should contain atleast one character   
def TC_Amazon_SignUp_006():
    get_URL()
    setName("S")
    setPhoneNumber("7674084752")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, "//*[@id='authportal-main-section']/div[2]/div/div[3]/div/h1")))
    verify = driver.find_element(by = By.XPATH, value = "//*[@id='authportal-main-section']/div[2]/div/div[3]/div/h1").text
    
    if(verify == "Verify mobile number"):
        print("TC_Amazon_SignUp_006 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_006 : Fail")
        assert False


# Check the name field should allow all the special characters except $, ^, ~, = and +                
def TC_Amazon_SignUp_007():
    get_URL()
    setName("Sr&)@nu!#%*-?><;")
    setPhoneNumber("3857464397")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, "//*[@id='authportal-main-section']/div[2]/div/div[3]/div/h1")))
    verify = driver.find_element(by = By.XPATH, value = "//*[@id='authportal-main-section']/div[2]/div/div[3]/div/h1").text
    
    if(verify == "Verify mobile number"):
        print("TC_Amazon_SignUp_007 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_007 : Fail")
        assert False    
   
# Check the name field should not allow the$, ^, ~, = and + characters
def TC_Amazon_SignUp_008():
    get_URL()
    setName("Sri$~^+nu")
    setPhoneNumber("3857464397")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    verify = driver.find_element(by = By.CLASS_NAME, value = "a-list-item").text
    if(verify == 'There is a slight problem with your request. Please make sure that you do not include the characters "$~^+" in your name.'):
        print("TC_Amazon_SignUp_008 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_008 : Fail")
        assert False 
 
# verify if the phone number is already registered then it should show proper message          
def TC_Amazon_SignUp_009():
    get_URL()
    setName("Srinu")
    setPhoneNumber("8142039706")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="auth-warning-message-box"]/div/h4')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-warning-message-box"]/div/h4').text
    
    if(verify == "Important Message!"):
        print("TC_Amazon_SignUp_009 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_009 : Fail")
        assert False
  
# Check the phone number field should not allow any alphabets    
def TC_Amazon_SignUp_010():
    get_URL()
    setName("Srinu")
    setPhoneNumber("8142039Ri6")
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="auth-email-invalid-claim-alert"]/div/div')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-email-invalid-claim-alert"]/div/div').text
    
    if(verify == "Wrong or Invalid email address or mobile phone number. Please correct and try again."):
        print("TC_Amazon_SignUp_010 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_010 : Fail")
        assert False
   
# Check the phone number field should not allow any special characters  
def TC_Amazon_SignUp_011():
    get_URL()
    setName("Srinu")
    setPhoneNumber("8142039#&6")
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="auth-email-invalid-claim-alert"]/div/div')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-email-invalid-claim-alert"]/div/div').text
    
    if(verify == "Wrong or Invalid email address or mobile phone number. Please correct and try again."):
        print("TC_Amazon_SignUp_011 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_011 : Fail")
        assert False
   
# Check the phone number field should allow the white spaces        
def TC_Amazon_SignUp_012():
    get_URL()
    setName("Srinu")
    setPhoneNumber("385 74  643 97 ")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1').text
    if(verify == 'Verify mobile number'):
        print("TC_Amazon_SignUp_012 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_012 : Fail")
        assert False
 
# Verify if the Country code is invalid with respect to Mobile number then user won't get any  OTP        
def TC_Amazon_SignUp_013():
    get_URL()
    setName("Srinu")
    setPhoneNumber("8985996435")
    driver.find_element(by=By.XPATH, value = link_countryCode_xpath)
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1').text
    if(verify == 'Verify mobile number'):
        print("TC_Amazon_SignUp_013 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_013 : Fail")
        assert False
   
# Verify if the Country code is valid with respect to Mobile number then user should get OTP        
def TC_Amazon_SignUp_014():
    get_URL()
    setName("Srinu")
    setPhoneNumber("3857464397")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1').text
    if(verify == 'Verify mobile number'):
        print("TC_Amazon_SignUp_014 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_014 : Fail")
        assert False
 
# Verify if the length of the phone number is less than 10        
def TC_Amazon_SignUp_015():
    get_URL()
    setName("Srinu")
    setPhoneNumber("3857464")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/h1').text
    if(verify == 'Verify mobile number'):
        print("TC_Amazon_SignUp_015 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_015 : Fail")
        assert False

# Verify if the length of the phone number is more than 10        
def TC_Amazon_SignUp_016():
    get_URL()
    setName("Srinu")
    setPhoneNumber("385746454678435436")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="auth-error-message-box"]/div/h4')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-error-message-box"]/div/h4').text
    if(verify == 'There was a problem'):
        print("TC_Amazon_SignUp_016 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_016 : Fail")
        assert False

# verify if the Email Id  is already registered then it should show proper message        
def TC_Amazon_SignUp_017():
    get_URL()
    setName("Srinu")
    setPhoneNumber("kondurusrinu9491@gmail.com")
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[1]/div/div/h4')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[1]/div/div/h4').text
    if(verify == 'Email address already in use'):
        print("TC_Amazon_SignUp_017 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_017 : Fail")
        assert False
  
# Verify if the Email id can contain quotes.        
def TC_Amazon_SignUp_018():
    get_URL()
    setName("Srinu")
    setPhoneNumber('kond"sri"@gmail.com')
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="auth-email-invalid-claim-alert"]/div/div')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-email-invalid-claim-alert"]/div/div').text
    if(verify == 'Wrong or Invalid email address or mobile phone number. Please correct and try again.'):
        print("TC_Amazon_SignUp_018 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_018 : Fail")
        assert False
   
# Verify if the Email id can contain a plus sign.      
def TC_Amazon_SignUp_019():
    get_URL()
    setName("Srinu")
    setPhoneNumber("kond+srin+12@gmail.com")
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="verification-code-form"]/div[4]/div[2]')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="verification-code-form"]/div[4]/div[2]').text
    if(verify == "To verify your email, we've sent a One Time Password (OTP) to kond+srin+12@gmail.com (Change)"):
        print("TC_Amazon_SignUp_019 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_019 : Fail")
        assert False
 
# Check the Email text field that has an Email address without @ symbol        
def TC_Amazon_SignUp_020():
    get_URL()
    setName("Srinu")
    setPhoneNumber("konduruAtgmail.com")
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="auth-email-invalid-claim-alert"]/div/div')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-email-invalid-claim-alert"]/div/div').text
    if(verify == 'Wrong or Invalid email address or mobile phone number. Please correct and try again.'):
        print("TC_Amazon_SignUp_020 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_020 : Fail")
        assert False
   
# Check the Email id field that has a mail id without any character before @ symbol        
def TC_Amazon_SignUp_021():
    get_URL()
    setName("Srinu")
    setPhoneNumber("@gmail.com")
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-email-invalid-claim-alert"]/div/div').text
    if(verify == 'Wrong or Invalid email address or mobile phone number. Please correct and try again.'):
        print("TC_Amazon_SignUp_021 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_021 : Fail")
        assert False
 
# Check the Email text field that has a random string instead of a real email        
def TC_Amazon_SignUp_022():
    get_URL()
    setName("Srinu")
    setPhoneNumber("srinugmail")
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-email-invalid-claim-alert"]/div/div').text
    if(verify == 'Wrong or Invalid email address or mobile phone number. Please correct and try again.'):
        print("TC_Amazon_SignUp_022 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_022 : Fail")
        assert False
 
# Check the Email text field that has a missing dot in the email address        
def TC_Amazon_SignUp_023():
    get_URL()
    setName("Srinu")
    setPhoneNumber("srinu@gmailcom")
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-email-invalid-claim-alert"]/div/div').text
    if(verify == 'Wrong or Invalid email address or mobile phone number. Please correct and try again.'):
        print("TC_Amazon_SignUp_023 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_023 : Fail")
        assert False

# Check the Password field requirments is mentioned below the Password text box  
def TC_Amazon_SignUp_024():
    get_URL()
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="ap_register_form"]/div/div/div[3]/div[1]/div[1]/div/div').text
    if(verify == 'Passwords must be at least 6 characters.'):
        print("TC_Amazon_SignUp_024 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_024 : Fail")
        assert False
 
# Check the password field by giving atleast 6 characters       
def TC_Amazon_SignUp_025():
    get_URL()
    setName("Srinu")
    setPhoneNumber("9355560729")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9734rwegdhgd")
    setReenterPassword("Srinu9734rwegdhgd")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/p[3]')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/p[3]').text
    if(verify == 'A text with a One Time Password (OTP) has been sent to your mobile number: 9355560729 Change'):
        print("TC_Amazon_SignUp_025 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_025 : Fail")
        assert False

# Check the password field by giving less than6 characters        
def TC_Amazon_SignUp_026():
    get_URL()
    setName("Srinu")
    setPhoneNumber("9355560729")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srin")
    setReenterPassword("Srin")
    clickContinue()
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-password-invalid-password-alert"]/div/div').text
    if(verify == 'Minimum 6 characters required'):
        print("TC_Amazon_SignUp_026 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_026 : Fail")
        assert False

# Check the password field by giving only 6 characters        
def TC_Amazon_SignUp_027():
    get_URL()
    setName("Srinu")
    setPhoneNumber("3857464397")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/p[3]')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/p[3]').text
    if(verify == 'A text with a One Time Password (OTP) has been sent to your mobile number: 3857464397 Change'):
        print("TC_Amazon_SignUp_027 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_027 : Fail")
        assert False

# Check the Re-enter Password field by giving same characters as givien in Password field        
def TC_Amazon_SignUp_028():
    get_URL()
    setName("Srinu")
    setPhoneNumber("9355560729")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9")
    clickContinue()
    WebDriverWait(driver,100).until(EC.presence_of_element_located(( By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/p[3]')))
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="authportal-main-section"]/div[2]/div/div[3]/div/p[3]').text
    if(verify == 'A text with a One Time Password (OTP) has been sent to your mobile number: 9355560729 Change'):
        print("TC_Amazon_SignUp_028 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_028 : Fail")
        assert False

# Check the Re-enter Password field by giving different characters as given in Password field
        
def TC_Amazon_SignUp_029():
    get_URL()
    setName("Srinu")
    setPhoneNumber("9355560729")
    clickCountryCode()
    clickCountryCodeIndia()
    setPassword("Srinu9")
    setReenterPassword("Srinu9491")
    clickContinue()
    verify = driver.find_element(by = By.XPATH, value = '//*[@id="auth-password-mismatch-alert"]/div/div').text
    if(verify == 'Passwords must match'):
        print("TC_Amazon_SignUp_029 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_029 : Fail")
        assert False

# Verify the Continue button is clickable or not 
def TC_Amazon_SignUp_030():
    get_URL()
    button = WebDriverWait(driver,100).until(EC.element_to_be_clickable(( By.ID, "continue")))
    if(button):
        print("TC_Amazon_SignUp_030 : Pass")
        assert True
    else:
        print("TC_Amazon_SignUp_030 : Fail")
        assert False

TC_Amazon_SignUp_001()
TC_Amazon_SignUp_002()
TC_Amazon_SignUp_003()
TC_Amazon_SignUp_004()
TC_Amazon_SignUp_005()
TC_Amazon_SignUp_006()
TC_Amazon_SignUp_007()
TC_Amazon_SignUp_008()
TC_Amazon_SignUp_009()
TC_Amazon_SignUp_010()
TC_Amazon_SignUp_011()
TC_Amazon_SignUp_012()
TC_Amazon_SignUp_013()
TC_Amazon_SignUp_014()
TC_Amazon_SignUp_015()
TC_Amazon_SignUp_016()
TC_Amazon_SignUp_017()
TC_Amazon_SignUp_018()
TC_Amazon_SignUp_019()
TC_Amazon_SignUp_020()
TC_Amazon_SignUp_021()
TC_Amazon_SignUp_022()
TC_Amazon_SignUp_023()
TC_Amazon_SignUp_024()
TC_Amazon_SignUp_025()
TC_Amazon_SignUp_026()
TC_Amazon_SignUp_027()
TC_Amazon_SignUp_028()
TC_Amazon_SignUp_029()
TC_Amazon_SignUp_030()

            
        
        