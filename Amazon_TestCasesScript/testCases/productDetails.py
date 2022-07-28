'''
Created on 28-Jun-2022

@author: kondsrin
'''
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

# Verify that price of product is displayed.
def TC_Amazon_SignUp_003():
    get_URL()
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
    driver_len = len(driver.window_handles)
    print("Tabs opened in browser : ",driver_len)
    driver.switch_to.window(driver.window_handles[1])
    
    productPrice = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="corePrice_desktop"]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]'))).text
    #productPrice = driver.find_element(by = By.XPATH, value = '//*[@id="corePrice_desktop"]/div/table').text
    if(productPrice):
        print("Price passed")
        assert True
    else:
        assert False

# Verify that product reviews are mentioned.        
def TC_Amazon_SignUp_004():  
    reviews = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="customer_review-R2BKDINI6JO085"]/div[2]'))).text
    if(reviews):
        print("Review passed")
        assert True
    else:
        assert False

# Verify that product specifications are displayed.
def TC_Amazon_SignUp_005():        
    features = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="feature-bullets"]'))).text
    if(features):
        print("Specification passed")
        assert True
    else:
        assert False

# Verify that information about IN-Stock/Out-Stock are displayed.
def TC_Amazon_SignUp_006():     
    inStock = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="availability"]/span'))).text
    if(inStock):
        print("InStock/OutStock passed")
        assert True
    else:
        assert False

# Verify that customer ratings should be displayed for the product        
def TC_Amazon_SignUp_007():     
    ratings = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="acrCustomerReviewLink"]'))).text
    if(ratings):
        print("ratings passed")
        assert True
    else:
        assert False

# Verify that all the variations of product are displayed.        
def TC_Amazon_SignUp_008():     
    variations = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="variation_style_name"]/ul'))).text
    if(variations):
        print("Variations passed")
        assert True
    else:
        assert False   
# Verify that shipping information about product are displayed.
def TC_Amazon_SignUp_009():         
    shipping = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]/span'))).text
    if(shipping):
        print("shipping passed")
        assert True
    else:
        assert False 

# Verify that Add to cart button should work
def TC_Amazon_SignUp_010():     
    driver.find_element(by = By.ID, value = "add-to-cart-button").click() 
    try:
        driver.find_element(by = By.XPATH, value = '//*[@id="nav-cart"]').click() 
    except:
        pass
    addToCart = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.LINK_TEXT, 'Redmi 9A Sport (Coral Green, 3GB RAM, 32GB Storage) | 2GHz Octa-core Helio G25 Processor | 5000 mAh Battery'))).text
    if(addToCart):
        print("addToCart passed")
        assert True
    else:
        assert False  
         
    
    
# Verify that product suggestions related to product should be displayed.  
def TC_Amazon_SignUp_011():  
    driver.back()  
    time.sleep(3)      
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sp_detail"]/div[1]/div[1]/h2')))
    relatedProducts = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="sp_detail"]/div[1]/div[1]/h2'))).text
    if(relatedProducts):
        print("relatedProducts passed")
        assert True
    else:
        assert False 
        
# Verify that when user click on Buy Now button the Delivery & Payment page should be displayed        
def TC_Amazon_SignUp_012():        
    try:
        driver.find_element(by = By.ID, value = 'buy-now-button').click() 
    except:
        pass
    buyNow = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="checkoutDisplayPage"]/div/div[2]/div[1]/h1'))).text
    if(buyNow):
        print("buyNow passed")
        assert True
    else:
        assert False   
    driver.back() 
 
# Verify that Add to Wish List button should work    
def TC_Amazon_SignUp_013():
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-wishlist-button-submit"]')))
    driver.find_element(by = By.XPATH, value = '//*[@id="add-to-wishlist-button-submit"]').click()
    print("clicked")
    # driver_len = len(driver.window_handles)
    # print(driver_len)
    # #driver.switch_to.window(driver.window_handles[1])
    #
    # a = ActionChains(driver)
    # #identify element
    # m = driver.find_element(by = By.XPATH, value = '//*[@id="nav-link-accountList"]')
    # #hover over element
    # a.move_to_element(m).perform()
    # #identify sub menu element
    # n = driver.find_element(by = By.LINK_TEXT, value = 'Your Wish List')
    # # hover over element and click
    # a.move_to_element(n).click().perform()
    #WebDriverWait(driver, 10).until(EC.alert_is_present())
    #print("Alert notified")
    time.sleep(3)
    #driver.switch_to.frame(driver.find_element(by = By.XPATH, value ='//*[@id="a-popover-12"]/div'))

    print("Alert came")
    driver.find_element(by = By.XPATH, value = '//*[@id="huc-view-your-list-button"]/span/a').click()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="itemName_I1AE7BD87R4O6L"]')))
    wishList = driver.find_element(by = By.XPATH, value = '//*[@id="itemName_I1AE7BD87R4O6L"]')
    if(wishList):
        print("WishList passed")
        assert True
    else:
        assert False 
         
    driver.back()    
    
# Verify that user should be able to select the quantity     
def TC_Amazon_SignUp_014(): 
    
    select = Select(driver.find_element(by = By.ID, value = "quantity"))
    select.select_by_visible_text('3')
    quantity = driver.find_element(by = By.XPATH, value = '//*[@id="quantity"]').text
    if(quantity):
        print("Quantity passed")
        assert True
    else:
        assert False

# Verify that Breadcrumb navigation should display for the product    
def TC_Amazon_SignUp_015(): 
    try:
        driver.find_element(by = By.XPATH, value = '//*[@id="nav-logo-sprites"]').click()
    except:
        pass
    # WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="I_gqM-BY3FwipQeQFtfQCg"]/div[2]/div/a[1]/div/img')))
    # driver.find_element(by = By.XPATH, value = '//*[@id="I_gqM-BY3FwipQeQFtfQCg"]/div[2]/div/a[1]/div/img').click()
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Redmi 9A Sport (Coral…')))
    try:
        driver.find_element(by = By.PARTIAL_LINK_TEXT, value = 'Redmi 9A Sport (Coral…').click()
    except:
        pass
    WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, '//*[@id="productTitle"]')))
    breadCrumb = driver.find_element(by = By.XPATH, value = '//*[@id="productTitle"]').text
    if(breadCrumb):
        print("BreadCrumb passed")
        assert True
    else:
        assert False    
  
# Verify that Seller information should display in the product details page    
def TC_Amazon_SignUp_016(): 
    
    sellerInfo = driver.find_element(by = By.XPATH, value = '//*[@id="merchant-info"]').text
    if(sellerInfo):
        print("SellerInfo passed")
        assert True
    else:
        assert False

# Verify that when user click on the Share button then dropdown should displayed with applicable items        
def TC_Amazon_SignUp_017(): 
    
    # driver.find_element(by = By.XPATH, value = '//*[@id="imageBlock_feature_div"]/span[1]/div/i').click()
    # shareButton = driver.find_element(by = By.XPATH, value = '/html/body/div[7]/div/div[1]/div/div[1]/a/span[2]').text
    a = ActionChains(driver)
    m = driver.find_element(by = By.XPATH, value = '//*[@id="imageBlock_feature_div"]/span[1]/div/i')
    a.move_to_element(m).click().perform()
    n = driver.find_element(by = By.LINK_TEXT, value = 'Pinterest')
    a.move_to_element(n).click().perform()
    time.sleep(2)
    driver_len = len(driver.window_handles)
    print("Tabs opened in browser : ",driver_len)
    driver.switch_to.window(driver.window_handles[2])
    time.sleep(3)
    actual = driver.title
    if(actual == 'Pinterest'):
        print("ShareButton passed")
        assert True
    else:
        assert False

# Verify that when user click on product image then a pop-up should displayed with product images        
def TC_Amazon_SignUp_018(): 
    
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
    driver.find_element(by = By.XPATH, value = '//*[@id="landingImage"]').click()
    productImages = driver.find_element(by = By.XPATH, value = '//*[@id="ivImage_1"]/div')
    if(productImages):
        print("ProductImages passed")
        assert True
    else:
        assert False
        



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
