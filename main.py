import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.wait import WebDriverWait




#you can use the beta version instead for path
os.environ['PATH'] += r"C:/Users/reedr/Documents/selenium drivers"
driver = webdriver.Chrome()
