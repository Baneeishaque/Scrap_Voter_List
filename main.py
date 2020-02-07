from selenium import webdriver
from selenium.webdriver.support.select import Select

# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:/Programs/chromedriver.exe")
driver.get("http://lsgelection.kerala.gov.in/voters/view")

# wait = WebDriverWait(driver, 100)
# wait.until(EC.element_to_be_clickable((By.ID, 'registration_online_district'))).click()
# wait.until(EC.element_to_be_clickable((By.ID, 'registration_online_localBody'))).click()
# wait.until(EC.element_to_be_clickable((By.ID, 'registration_online_ward'))).click()
# wait.until(EC.element_to_be_clickable((By.ID, 'registration_online_pollingStation'))).click()

district_selector = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/select')
district_selector.click()

# district_selector = Select(driver.find_element_by_id('registration_online_district'))
# district_selector=Select(driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div[1]/div[1]/select'))
# print(district_selector.options)

# for opt in district_selector.options:
#     district_selector.select_by_value('5')

local_body_selector = Select(driver.find_element_by_id('registration_online_localBody'))
for opt in local_body_selector.options:
    local_body_selector.select_by_visible_text('G10069-Thanalur')

ward_selector = Select(driver.find_element_by_id('registration_online_ward'))
for opt in ward_selector.options:
    ward_selector.select_by_visible_text('G10069004 - PANDIYATU')

polling_station_selector = Select(driver.find_element_by_id('registration_online_pollingStation'))
for opt in polling_station_selector.options:
    polling_station_selector.select_by_visible_text('001 - AL MADARASATHUL ISLAHIYA(PANDIYATT),TANALUR')

# 002 - BAYANUL HUDA MADRASSA, JARAM

submit_button = driver.find_element_by_id('form_submit')
submit_button.click()

driver.close()
