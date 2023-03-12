from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
#import time
from selenium.webdriver.support.wait import WebDriverWait

from helper_tests import simple_assert, boolean_assert

#Constantsyp

SELENIUM_SITE = "https://www.selenium.dev/selenium/web/web-form.html"
ICEBERRY_SITE = "https://scar.sandbox.iceberry.se/"

#setup and teardown
@pytest.fixture
def load_driver():

    #beta vesion of using selenium manager
    driver = webdriver.Chrome()

    yield driver

    driver.quit()

#Tests

def test_lecture_1(load_driver):
    # Load seleium twebdriver
    driver = load_driver

    #load iceberry website
    driver.get(ICEBERRY_SITE)

    #test that iceberry is a part of the url
    boolean_assert("icebery" in driver.current_url, f"Expected iceberry in url, got: {driver.current_url}")

    #find the header element on the site by XPATH
    heading = driver.find_element(By.XPATH, "/html/body/div/main/header/div/h1")

    #test that the header contains the correct text
    boolean_assert("SCAR" in heading.text, f"Expected iceberry in url, got: {heading.text}")
    #test if exact text exist in headerwodows peak
    simple_assert(heading.text, "SCAR ENERGY DRINK")

    #find products page link
    products_link = driver.find_element(By.LINK_TEXT, "Products")

    #click on product page link
    products_link.click()

    #explicit wait
    scar_original = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.XPATH,"/html/body/div/main/section/div/main/a[1]/div/div[2]/h2"))

    #test that the text contains "scar originals"
    boolean_assert("Scar Original" in scar_original.text, f"Expected Scar Original in text for first product, got: {scar_original.text}")

    #tests that url states products
    boolean_assert("products" in driver.current_url, f"Expected products in url, got: {driver.current_url}")
