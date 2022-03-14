import selenium
from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time



URL="https://icampus.skku.edu/login"

driver = webdriver.Chrome(executable_path='chromedriver')
driver.get(url=URL)

time.sleep(0.5)

lg_id = driver.find_element(by=By.ID, value='userid')
lg_pw = driver.find_element(by=By.ID, value='password')
lg_btn = driver.find_element(by=By.ID, value='btnLoginBtn')

lg_id.send_keys("jjhking456")
lg_pw.send_keys("862486A!!")

time.sleep(0.5)

lg_btn.click()
time.sleep(3)

lg_bt = driver.find_elements_by_class_name('xn-main-lms-link-wrap')
# print(lg_bt)

for a in lg_bt:
    try:
        a.click()
    except:
        pass

time.sleep(2)
dashCard = driver.find_elements(by=By.CLASS_NAME, value='ic-DashboardCard')
temp = dashCard[1]
temp.click()
time.sleep(1)
contents = driver.find_elements(by=By.CLASS_NAME, value='context_external_tool_1')
contents[0].click()


try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME , 'gLFyf'))
    )
    classOf = driver.find_elements(by=By.CLASS_NAME, value='xn-section')
except:
    pass
print(classOf)

driver.quit()
# classOf[0].click()
# for card in dashCard:
    # card.click()
    # print(card.get_attribute('aria-label'))

# context_external_tool_1

