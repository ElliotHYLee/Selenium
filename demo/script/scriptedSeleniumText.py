from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

firefox_cap = DesiredCapabilities.FIREFOX
firefox_cap['marionette'] = False

driver = webdriver.Firefox(capabilities=firefox_cap)
driver.get("https://elliothylee.github.io/Selenium/")

txtMeter = driver.find_element_by_id("txtMeter1")
txtMeter.clear()
txtMeter.send_keys("2")
driver.find_element_by_id("btn1").click()
txtFt = driver.find_element_by_id("txtFt")
assert txtFt.get_attribute('value') == "6.56168"

txtMeter2 = driver.find_element_by_id("txtMeter2")
txtMeter2.clear()
txtMeter2.send_keys("5000")
driver.find_element_by_id("btn2").click()
txtMile = driver.find_element_by_id("txtMile")
assert txtMile.get_attribute('value') == "3.106855"

txtMeter3 = driver.find_element_by_id("txtMeter3")
txtMeter3.clear()
txtMeter3.send_keys("20")
driver.find_element_by_id("btn3").click()
txtYard = driver.find_element_by_id("txtYard")
assert txtYard.get_attribute('value') == "21.8723"

txtMinute = driver.find_element_by_id("txtMinute")
txtMinute.clear()
txtMinute.send_keys("20")
driver.find_element_by_id("btn4").click()
txtSec = driver.find_element_by_id("txtSec")
assert txtSec.get_attribute('value') == "1200.8888"

driver.close()
