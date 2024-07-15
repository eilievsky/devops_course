import time
from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome(webdriver.ChromeOptions())  # Optional argument, if not specified will search path.
driver.get('C:/Users/evgeny.Iliev2/PycharmProjects/devops/lesson4/tip_calc/index.html');
time.sleep(5) # Let the user actually see something!
driver.find_element(by="id",value='billamt' ).send_keys('100')
driver.find_element(by="xpath",value='//*[@id="serviceQual"]/option[3]').click()
driver.find_element(by="xpath", value = '//*[@id="musicQuality"]/option[3]').click()
driver.find_element(by='id',value='peopleamt').send_keys('5')
driver.find_element(by='id',value="calculate").click()

expected = '5.00'
actual = driver.find_element(by='id',value='tip').text
assert expected == actual, f"Expected {expected} vs actual {actual}"
time.sleep(10) # Let the user actually see something!
# search_box.submit()
# time.sleep(5) # Let the user actually see something!

# driver.quit()
# #
# webdriver.Chrome()