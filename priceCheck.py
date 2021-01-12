import time
from selenium import webdriver
from selenium.common import exceptions

driverPath = r"webdrivers\\chromedriver.exe"
url = "https://www.flaconi.de/"

try:
    driver = webdriver.Chrome(driverPath)
    driver.get(url)
    driver.maximize_window()

    # alert = driver.switch_to.alert
    if driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]'):
        driver.find_element_by_xpath('//*[@id="uc-btn-accept-banner"]').click()

    # Navigate to parfum
    parfum = driver.find_element_by_xpath("//nav[@id='main-navigation']/ul/li[2]/a")
    parfum.click()
    time.sleep(3)

    # Navigate to first result
    firstPerfume = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[3]/div[1]/div/ul/li[1]/div[2]/a/img')
    firstPerfume.click()
    time.sleep(3)

    #
    itemPrice = float((driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[3]/div[1]/div[2]/div[3]/ul/li[1]/div/div[3]/span").text).replace("€", "").replace(" ", "").replace("*", "").replace(",", "."))

    #print(itemPrice)


    # Adding the perfume to cart
    addToCart = driver.find_element_by_css_selector("button.button-primary.loaderbox-trigger")
    addToCart.click()
    time.sleep(3)

    # Navigating to Cart
    navigateToCart = driver.find_element_by_css_selector("a.button-secondary.pull-right")
    navigateToCart.click()
    time.sleep(3)

    cartPrice = float((driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div[2]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[3]/span[1]").text.replace("€", "").replace(" ", "").replace(",", ".")))
    if cartPrice == itemPrice:
        print("Test Result - Pass.")
    else:
        print("Test Result - Failed. Displayed price and item price not matching.")
    #driver.close()

except exceptions.NoSuchElementException as e:
    print("Unable to locate web element. " + e.msg)

except exceptions.WebDriverException as e:
    print("Unable to load the chrome web driver. " + e.msg)
