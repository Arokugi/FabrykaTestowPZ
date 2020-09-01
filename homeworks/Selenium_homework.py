from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('/Users/Arek/PycharmProjects/kurs_taps_windows/chromedriver.exe')

driver.get('https://fabrykatestow.pl')

kurs_taps = driver.find_element_by_css_selector('#menu-item-506 > a')

kurs_taps.click()

element = driver.find_element_by_css_selector('#content > div > div > div > div > div > div > div > section.elementor-element.elementor-element-6acf69cc.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default.elementor-section.elementor-top-section > div.elementor-container.elementor-column-gap-default > div > div > div > div > section > div > div > div.elementor-element.elementor-element-416070db.elementor-column.elementor-col-50.elementor-inner-column > div > div > div.elementor-element.elementor-element-162580f4.elementor-widget.elementor-widget-image > div > div > img')

actions = ActionChains(driver)

actions.move_to_element(element).perform()

time.sleep(3)

driver.get_screenshot_as_file('moj_instruktor.png')

driver.quit()
