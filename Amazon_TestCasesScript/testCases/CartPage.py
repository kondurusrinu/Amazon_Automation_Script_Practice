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

# Verify that when user clicks on add to cart, the product should be added to cart.
def TC_Amazon_Cart_002():
    get_URL()
    enterEmailOrPhnum("7674084250")
    continueButton()
    enterPassword("Srinu9491")
    signIn()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.ID, "nav-search-dropdown-card")))
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
    # driver_len = len(driver.window_handles)
    # print("Tabs opened in browser : ",driver_len)
    driver.switch_to.window(driver.window_handles[1])
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))
    driver.find_element(by = By.ID, value = "add-to-cart-button").click()
    time.sleep(4)
    driver.find_element(by = By.XPATH, value = '//*[@id="attach-sidesheet-view-cart-button"]/span/input').click() 
    time.sleep(5)
    addToCart = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery'))).text
    
    
    if(addToCart):
        print("AddToCart Pass")
        assert True
    else:
        assert False
        
    #driver.back()    
    
# Verify that item quantity should be increased if user adds same item in Cart again.
def TC_Amazon_Cart_004():
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))
    driver.find_element(by = By.ID, value = "add-to-cart-button").click()
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '//*[@id="attach-sidesheet-view-cart-button"]/span/input').click() 

    time.sleep(3)
    driver.refresh()
    time.sleep(3)
    cartCount = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nav-cart-count"]'))).text
    print(cartCount)
    
    if(cartCount == "4"):
        print("CartCount Pass")
        assert True
    else:
        assert False
        
#Verify that total amount of all items should be displayed to user.
def TC_Amazon_Cart_005():
    #WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sc-subtotal-amount-buybox"]')))
    time.sleep(5)
    driver.refresh()
    orderTotal = driver.find_element(by = By.XPATH, value = '//*[@id="sc-subtotal-amount-buybox"]').text
    print(orderTotal)
    final_total = orderTotal.replace("   ", "")
    if(final_total == "20,997.00"):
        print("OrderTotal Pass")
        assert True
    else:
        assert False



# Verify that user should not be able to add items in cart beyond a certain limit.    
def TC_Amazon_Cart_006():
    select = Select(driver.find_element(by = By.ID, value = "quantity"))
    select.select_by_visible_text('10+')
    time.sleep(3)
    action = ActionChains(driver)
    quan = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[1]/span/input')
    action.move_to_element(quan).double_click().send_keys("11").perform()
    #quan.clear()
    driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[1]/span/span[2]/span/span').click()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div[1]/div')))
    quantityError = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div[1]/div')
    #== 'This seller has a limit of 10 per customer. To see if more are available from another seller, go to the product detail page.
    if(quantityError):
        print("QuantityError Pass")
        assert True
    else:
        assert False
    time.sleep(3)    
    #driver.find_element(by = By.XPATH, value = '//*[@id="sc-item-C79408f54-af8e-4fb9-9d76-fba46c6ddf5b"]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[1]/span/input').clear()
    #driver.find_element(by = By.XPATH, value = '//*[@id="sc-item-C79408f54-af8e-4fb9-9d76-fba46c6ddf5b"]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[1]/span/input').send_keys("2")
    action = ActionChains(driver)
    quan = driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[1]/span/input')
    action.move_to_element(quan).double_click().send_keys("2").perform()
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div[2]/div[1]/div/div/div[2]/div[1]/span[1]/span/span/span/span').click()

# Verify that when user click on the Proceed to buy button then delivery address page should displayed    
def TC_Amazon_Cart_007():
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '//*[@id="sc-buy-box-ptc-button"]/span/input').click()
    buyNow = driver.find_element(by = By.XPATH, value = '//*[@id="addres-select"]/h1').text
    if(buyNow == 'Select a delivery address'):
        print("BuyNow Pass")
        assert True
    else:
        assert False
    driver.back()

# Verify that items in cart should be present if user logs out and logs in again.    
def TC_Amazon_Cart_008():    
    a = ActionChains(driver)
    m = driver.find_element(by = By.XPATH, value = '//*[@id="nav-link-accountList"]')
    a.move_to_element(m).perform()
    n = driver.find_element(by = By.LINK_TEXT, value = 'Sign Out')
    a.move_to_element(n).click().perform()
    enterEmailOrPhnum("7674084250")
    continueButton()
    enterPassword("Srinu9491")
    signIn()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="nav-cart"]')))
    try:
        driver.find_element(by = By.XPATH, value = '//*[@id="nav-cart"]').click()
    except:
        pass
    cartAfterSignOut = driver.find_element(by = By.LINK_TEXT, value = 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery').text
    if(cartAfterSignOut):
        print("CartAfterSignOut Pass")
        assert True
    else:
        assert False

# Verify that Quantity should be changeble in cart page and amount also should be updated        
def TC_Amazon_Cart_009():   
    select = Select(driver.find_element(by = By.ID, value = "quantity"))
    select.select_by_visible_text('3')  
    time.sleep(3)
    quantity = driver.find_element(by = By.XPATH, value = '//*[@id="sc-subtotal-amount-buybox"]/span').text
    final_total = quantity.replace("  ", "")
    if(final_total =='20,997.00'):
        print("Quantity and Amount Pass")
        assert True
    else:
        assert False  

# Verify that when user select zero(0) quantity the item should delete from the cart    
def TC_Amazon_Cart_010():   
    select = Select(driver.find_element(by = By.ID, value = "quantity"))
    select.select_by_visible_text('0 (Delete)') 
    zeroQuantity = driver.find_element(by = By.PARTIAL_LINK_TEXT, value = 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-...').text
    if(zeroQuantity):
        print("ZeroQuantity Pass")
        assert True
    else:
        assert False 
        
    driver.find_element(by = By.XPATH, value = '//*[@id="nav-logo-sprites"]').click() 
    time.sleep(3)
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
    # driver_len = len(driver.window_handles)
    # print("Tabs opened in browser : ",driver_len)
    driver.switch_to.window(driver.window_handles[2])
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))
    driver.find_element(by = By.ID, value = "add-to-cart-button").click()
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '//*[@id="attach-sidesheet-view-cart-button"]/span/input').click()    

# Verify that the last deleted item name shoud be displayed in the cart page    
def TC_Amazon_Cart_011():  
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/input')))
    driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div[2]/div[3]/div[4]/div/div[2]/div[1]/div/form/div[2]/div[3]/div[4]/div/div[1]/div/div/div[2]/div[1]/span[2]/span/input').click() 
    
    delete = driver.find_element(by = By.PARTIAL_LINK_TEXT, value = 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-...').text
    
    if(delete):
        print("Delete button Pass")
        assert True
    else:
        assert False
    driver.find_element(by = By.PARTIAL_LINK_TEXT, value = 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-...').click()
    # driver_len = len(driver.window_handles)
    # print("Tabs opened in browser : ",driver_len)
    driver.switch_to.window(driver.window_handles[2])
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))
    driver.find_element(by = By.ID, value = "add-to-cart-button").click()
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '//*[@id="attach-sidesheet-view-cart-button"]/span/input').click()   

# Verify that user is redirected to the product detail page when click on an item in the cart page    
def TC_Amazon_Cart_012():
    
    driver.find_element(by = By.LINK_TEXT, value = 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery').click()
    # driver_len = len(driver.window_handles)
    # print("Tabs opened in browser : ",driver_len)
    driver.switch_to.window(driver.window_handles[3])
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery')))
    pdp = driver.find_element(by = By.LINK_TEXT, value = 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery').text
    if(pdp):
        print("Product Details page Pass")
        assert True
    else:
        assert False
        
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-button"]')))
    driver.find_element(by = By.ID, value = "add-to-cart-button").click()
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '//*[@id="attach-sidesheet-view-cart-button"]/span/input').click()  
    

TC_Amazon_Cart_002()
#TC_Amazon_Cart_004()
#TC_Amazon_Cart_005()
# TC_Amazon_Cart_006()
# TC_Amazon_Cart_007()
# TC_Amazon_Cart_008()
# TC_Amazon_Cart_009()
# TC_Amazon_Cart_010()
TC_Amazon_Cart_011()
TC_Amazon_Cart_012()
# TC_Amazon_SignUp_004()
# TC_Amazon_SignUp_005()


# def TC():
#     get_URL()
#     enterEmailOrPhnum("7674084250")
#     continueButton()
#     enterPassword("Srinu9491")
#     signIn()
#     driver.find_element(by = By.ID, value = "nav-search-dropdown-card").click()
#
#     select = Select(driver.find_element(by = By.ID, value = "searchDropdownBox"))
#     select.select_by_visible_text('Electronics')
#     driver.find_element(by = By.ID, value = "twotabsearchtextbox").send_keys("mobile")
#     try:
#         driver.find_element(by = By.ID, value = "nav-search-submit-button").click()
#     except:
#         pass
#     #driver.back()
#     driver.find_element(by = By.LINK_TEXT, value = 'Redmi 9A Sport (Coral Green, 2GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery').click()
#     # driver_len = len(driver.window_handles)
#     # print("Tabs opened in browser : ",driver_len)
#     driver.switch_to.window(driver.window_handles[1])
#     driver.find_element(by = By.XPATH, value = '//*[@id="buy-now-button"]').click()
#     time.sleep(3)
#
#     driver.find_element(by = By.XPATH, value = '/html/body/div[5]/div/div[2]/div[2]/div/div[2]/div[1]/form/div[1]/div/div/div[2]/div[2]/div/div/div/div/div[1]/span/div/label/input').click()
#
#
#
#
# TC()        


