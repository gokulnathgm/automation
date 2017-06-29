import os
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import username, password

# Accepts source branch, target branch and assignee from command line
source_branch = sys.argv[1]
target_branch = sys.argv[2]
assignee = sys.argv[3]

# Sets up chrome web driver for selenium
chromedriver = "/home/Gokul/Documents/selenium-web-drivers/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# Takes up user credentials of GitLab from config file and logs in
driver.get("https://code.qburst.com/users/sign_in")
driver.find_element_by_id('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)
driver.find_element_by_name('commit').click()

# Creates a new merge request
driver.get("https://code.qburst.com/ctools/api/ct_api/merge_requests")
driver.find_element_by_link_text('New merge request').click()

# Selects the appropriate source branch
driver.find_element_by_xpath('//*[@data-field-name="merge_request[source_branch]"]').click()
xpath = '//*[@title="' + source_branch + '"]'
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
driver.find_element_by_xpath(xpath).click()

# Selects the appropriate target branch
driver.find_element_by_xpath('//*[@data-field-name="merge_request[target_branch]"]').click()
xpath = '//*[@title="' + target_branch + '"]'
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
targets = driver.find_elements_by_xpath(xpath)
targets[1].click()

driver.find_element_by_name('commit').click()

title = driver.find_element_by_id('merge_request_title')
text = title.get_attribute('value')

# Selects the appropriate assignee
driver.find_element_by_xpath('//*[@data-default-label="Assignee"]').click()
xpath = '//*[@id="new_merge_request"]/div[3]/div/div[1]/div/div/div/div/div[3]/ul/li/a/span[contains(text(), "' + assignee + '")]'
element = WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(
        (By.XPATH, xpath)))
driver.find_element_by_xpath(xpath).click()

# Creates the merge request
if not text.startswith('WIP'):
    driver.find_element_by_name('commit').click()
