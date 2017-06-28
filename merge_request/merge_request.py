import os

from config import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chromedriver = "/home/Gokul/Documents/selenium-web-drivers/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://code.qburst.com/users/sign_in")
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_name('commit').click()
driver.get("https://code.qburst.com/ctools/api/ct_api/merge_requests")
driver.find_element_by_link_text('New merge request').click()
source = driver.find_element_by_xpath("//*[contains(text(), 'Select source branch')]").click()
develop = driver.find_element_by_xpath('//*[@title="develop"]').click()
driver.find_element_by_name('commit').click()
title = driver.find_element_by_id('merge_request_title')
text = title.get_attribute('value')
assignee = driver.find_element_by_xpath('//*[@data-default-label="Assignee"]').click()
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="new_merge_request"]/div[3]/div/div[1]/div/div/div/div/div[3]/ul/li[16]/a/strong')))
assignee = driver.find_element_by_xpath(
    '//*[@id="new_merge_request"]/div[3]/div/div[1]/div/div/div/div/div[3]/ul/li[16]/a/strong').click()
if not text.startsith('WIP'):
    driver.find_element_by_name('commit').click()
