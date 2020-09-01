from selenium import webdriver

import time

driver = webdriver.Chrome('/Users/Arek/PycharmProjects/kurs_taps_windows/chromedriver.exe')


driver.get('https://google.pl')

search_box = driver.find_element_by_name('q')

search_box.send_keys('Arkadiusz Kugler przewodnik')

search_box.submit()

time.sleep(6)

driver.quit()

