from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#for login functionality
import chromedriver_autoinstaller


chromedriver_autoinstaller.install()
driver = webdriver.Chrome()

base_URL="https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&"
link_email_xpath="//*[@id='ap_email']"
link_email_Continue="//*[@id='continue']"
textbox_password_xpath="//*[@id='ap_password']"
button_signin_xpath="//*[@id='signInSubmit']"
password_error_xpath="//*[@id='auth-error-message-box']/div/div/ul/li/span"
#It will install ChromeDriver Automatically




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
    
def TC_Amazon_002():
    login()
    enterEmailOrPhnum("7659834107")
    continueButton()
    enterPassword("Anusha@1")
    signIn()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, password_error_xpath)))
    password_er = driver.find_element(by = By.XPATH, value= password_error_xpath).text
    if(password_er == "Your password is incorrect"):
        print("TC_Amazon_002:Pass")
        assert True
    else:
        print("TC_Amazon_002:Fail")
        assert False
#Forgot password
def TC_Amazon_003():
    login()
    enterEmailOrPhnum("anushamurapaka20@gmail.com")
    continueButton()
    enterPassword("Anusha@1")
    signIn()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, password_error_xpath)))
    password_er = driver.find_element(by = By.XPATH, value= password_error_xpath).text
    if(password_er == "Your password is incorrect"):
        print("TC_Amazon_003 : Pass")
        assert True
    else:
        print("TC_Amazon_003:Fail")
        assert False
#invalid username AND password
def TC_Amazon_004():
    login()
    enterEmailOrPhnum("7659834107")
    continueButton()
    driver.find_element(by=By.XPATH, value = "//*[@id='ap_password']").send_keys("")
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'nav-logo-sprites')))
    password_er = driver.title
    if(password_er == "Amazon.com. Spend less. Smile more."):
        print("TC_Amazon_004 : Pass")
        assert True
    else:
        print("TC_Amazon_004 : Fail")
        assert False
    driver.find_element(by = By.XPATH, value="//*[@id='nav-hamburger-menu']").click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hmenu-content']/ul[1]/li[25]/a")))
    driver.find_element(by=By.XPATH, value="//*[@id='hmenu-content']/ul[1]/li[25]/a").click()
    
       
   
#enter unregistred email       
def TC_Amazon_005():
    login()
    enterEmailOrPhnum("anusi@gmail.com")
    continueButton()
    
    email_er = driver.find_element(by = By.XPATH, value="//*[@id='auth-error-message-box']/div/h4").text
    if(email_er == "There was a problem"):
        print("TC_Amazon_005:Pass")
        assert True
    else:
        print("TC_Amazon_005:Fail")
        assert False
        
#without entering mail or phone click continue      
def TC_Amazon_006():
    login()
    continueButton()
    blankCheckbox=  driver.find_element(by = By.XPATH, value="//*[@id='auth-email-missing-alert']/div/div").text
    if(blankCheckbox=="Enter your email or mobile phone number"):
        print("TC_Amazon_006:pass")
        assert True
    else:
        print("TC_Amazon_006:fail")
        assert False
#click on create your account
def TC_Amazon_007():
    login()
    driver.find_element(by=By.XPATH, value = "//*[@id='createAccountSubmit']").click()
    createAcc= driver.find_element(by=By.XPATH, value = "//*[@id='ap_register_form']/div/div/h1").text
    if(createAcc == "Create account"):
        print("TC_Amazon_007:pass")
        assert True
    else:
        print("TC_Amazon_007:fail")
        assert False

     
#conditions of use redirecting to conditions of  page      
def TC_Amazon_009():
    login()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id='legalTextRow']/a[1]")))
    driver.find_element(by = By.XPATH, value="//*[@id='legalTextRow']/a[1]").click()
    element = driver.find_element(by=By.XPATH,value='//*[@id="a-page"]/div[2]/div[2]/div[1]/div[1]/div[3]/h2[1]').text
    if( element=="Please read these conditions carefully."):
        print("TC_Amazon_009:pass")
        assert True
        
    else:
        print("TC_Amazon_009:fail")
        assert False
        
    

    
    
#click privacy notice redirecting to privacy notice page  
def TC_Amazon_011():
    login()
    driver.find_element(by = By.XPATH, value= "//*[@id='legalTextRow']/a[2]").click()
    linkPrivacy = driver.find_element(by=By.XPATH, value='//*[@id="a-page"]/div[2]/div[2]/div[1]/div[1]/div[3]/div/h1').text
    if(linkPrivacy == "Amazon.com Privacy Notice"):
        print("TC_Amazon_011:pass")
        assert True
    else:
        print("TC_Amazon_011:fail")
        assert False
#click on need help to show forgotpassword and others signin options        
def TC_Amazon_012():
    login()
    driver.find_element(by=By.XPATH, value = "//*[@id='authportal-main-section']/div[2]/div/div[1]/form/div/div/div/div[3]/div/a/span").click()
    forgotPass=driver.find_element(by=By.XPATH,value='//*[@id="auth-fpp-link-bottom"]').text
    otherSignIn=driver.find_element(by=By.XPATH,value='//*[@id="ap-other-signin-issues-link"]').text
    
    if((forgotPass =="Forgot your password?") and (otherSignIn=="Other issues with Sign-In")):
        print("TC_Amazon_012:pass")
        assert True
    else:
        print("TC_Amazon_012:fail")
        assert False
        

#click forgot password to redirecting to password assistance page
def TC_Amazon_013():
    login()
    driver.find_element(by=By.XPATH, value = "//*[@id='authportal-main-section']/div[2]/div/div[1]/form/div/div/div/div[3]/div/a/span").click()
    driver.find_element(by=By.XPATH, value="//*[@id='auth-fpp-link-bottom']").click()
    clickForgotPassword=driver.find_element(by=By.XPATH, value="//*[@id='authportal-main-section']/div[2]/div/div[1]/div/form/h1").text
    if(clickForgotPassword=="Password assistance"):
        print("TC_Amazon_013:pass")
        assert True
    else:
        print("TC_Amazon_013:fail")
        assert False
#click signin issues to redirect the page into account and login issues        
def TC_Amazon_014():
    login()
    driver.find_element(by=By.XPATH, value = "//*[@id='authportal-main-section']/div[2]/div/div[1]/form/div/div/div/div[3]/div/a/span").click()
    driver.find_element(by=By.XPATH, value="//*[@id='ap-other-signin-issues-link']").click()
    signIssues=driver.find_element(by=By.XPATH,value="//*[@id='a-page']/div[2]/div[1]/h1").text
    if(signIssues=="Account & Login Issues"):
        print("TC_Amazon_014:pass")
        assert True
    else:
        print("TC_Amazon_014:fail")
        assert False
#enter valid email or phone num and password and it shows homepage title        
def TC_Amazon_015():
    login()
    enterEmailOrPhnum("7659834107")
    continueButton()
    driver.find_element(by=By.XPATH, value = "//*[@id='ap_password']").send_keys("")
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, 'nav-logo-sprites')))
    password_er = driver.title
    if(password_er == "Amazon.com. Spend less. Smile more."):
        print("TC_Amazon_015 : Pass")
        assert True
    else:
        print("TC_Amazon_015: Fail")
        assert False
    driver.find_element(by = By.XPATH, value="//*[@id='nav-hamburger-menu']").click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hmenu-content']/ul[1]/li[25]/a")))
    driver.find_element(by=By.XPATH, value="//*[@id='hmenu-content']/ul[1]/li[25]/a").click()
    
       
    
#valid username and invalid password      
def TC_Amazon_016():
    login()
    enterEmailOrPhnum("7659834107")
    continueButton()
    enterPassword("Anusha@2")
    signIn()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, password_error_xpath)))
    password_er = driver.find_element(by = By.XPATH, value= password_error_xpath).text
    if(password_er == "Your password is incorrect"):
        print("TC_Amazon_016:Pass")
        assert True
    else:
        print("TC_Amazon_016:Fail")
        assert False
#enter username and leave blank checkbox for password field       
def TC_Amazon_017():
    login()
    enterEmailOrPhnum("anushamurapaka20@gmail.com")
    continueButton()
    signIn()
    blankPass=driver.find_element(by=By.XPATH,value="//*[@id='auth-password-missing-alert']/div/div").text
    if(blankPass=="Enter your password"):
        print("TC_Amazon_017:Pass")
        assert True
    else:
        print("TC_Amazon_017:Fail")
        assert False
        
        
#enter username and click change link   
def TC_Amazon_018():
    login()
    enterEmailOrPhnum("7659834107")
    driver.find_element(by=By.XPATH, value="//*[@id='continue']").click()
    driver.find_element(by=By.XPATH,value="//*[@id='ap_change_login_claim']").click()
    clickChange= driver.find_element(by=By.XPATH,value="//*[@id='authportal-main-section']/div[2]/div/div[1]/form/div/div/div/h1").text
    if(clickChange=="Sign-In"):
        print("TC_Amazon_019:pass")
        assert True
    else:
        print("TC_Amazon_019:fail")
        assert False
#for keep me signed in
def TC_Amazon_021():
    login()
    enterEmailOrPhnum("7659834107")
    continueButton()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="authportal-main-section"]/div[2]/div[1]/div/div/form/div/div[2]/div/div/label/div/label/input')))
    driver.find_element(by=By.XPATH, value='//*[@id="authportal-main-section"]/div[2]/div[1]/div/div/form/div/div[2]/div/div/label/div/label/input').click()
    driver.find_element(by=By.XPATH, value = "//*[@id='ap_password']").send_keys("")
    WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, "//*[@id='nav-hamburger-menu']/span")))
    click=driver.find_element(by=By.XPATH,value="//*[@id='nav-hamburger-menu']/span").text
    if(click=="All"):
        print("TC_Amazon_021:pass")
        assert True
    else:
        print("TC_Amazon_021:fail")
        assert False
    driver.find_element(by = By.XPATH, value="//*[@id='nav-hamburger-menu']").click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hmenu-content']/ul[1]/li[25]/a")))
    driver.find_element(by=By.XPATH, value="//*[@id='hmenu-content']/ul[1]/li[25]/a").click()
    
       
    
    
    
    
        
#for details
def TC_Amazon_022():
    login()
    enterEmailOrPhnum("7659834107")
    continueButton()
    driver.find_element(by=By.XPATH, value='//*[@id="remember_me_learn_more_link"]').click()
    click=driver.find_element(by=By.XPATH,value='//*[@id="a-popover-header-1"]').text
    if(click=='"Keep Me Signed In" Checkbox'):
        print("TC_Amazon_022:pass")
        assert True
    else:
        print("TC_Amazon_022:fail")
        assert False
#for OTP       
def TC_Amazon_023():
    login()
    enterEmailOrPhnum("7659834107")
    continueButton()
    driver.find_element(by=By.XPATH, value='//*[@id="continue"]').click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="verification-code-form"]/div[4]/div[1]/h1')))
    enterOtp=driver.find_element(by=By.XPATH,value='//*[@id="verification-code-form"]/div[4]/div[1]/h1').text
    if(enterOtp=="Authentication required"):
        print("TC_Amazon_023:pass")
        assert True
    else:
        print("TC_Amazon_023:fail")
        assert False
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id='nav-hamburger-menu']")))   
    driver.find_element(by = By.XPATH, value="//*[@id='nav-hamburger-menu']").click()
    WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, "//*[@id='hmenu-content']/ul[1]/li[25]/a")))
    driver.find_element(by=By.XPATH, value="//*[@id='hmenu-content']/ul[1]/li[25]/a").click()

    
    
    
    
    
    


TC_Amazon_002()
TC_Amazon_003()
TC_Amazon_004()

TC_Amazon_005()
TC_Amazon_006()
TC_Amazon_007()
TC_Amazon_009()

TC_Amazon_011()

TC_Amazon_012()
TC_Amazon_013()
TC_Amazon_014()
TC_Amazon_015()
TC_Amazon_016()
TC_Amazon_017()
TC_Amazon_018()
TC_Amazon_021()
TC_Amazon_022()

TC_Amazon_023()





