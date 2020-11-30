
from tests.helpers.support_functions import *
import time

authorisation_tab = 'basicauth-header'
authorisation_content = 'basicauth-content'
username_content = 'ba_username'
username_input = '//*[@id="ba_username"]'
password_content = 'ba_password'
password_input = '//*[@id="ba_password"]'
button_id = '//*[@id="content"]/button'


def click_authorisation_tab(driver_instance):
    elem = driver_instance.find_element_by_id(authorisation_tab)
    elem.click()


def authorisation_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, username_content)
    return elem.is_displayed()


def send_keys_to_authorisation(driver_instance):
    wait_for_visibility_of_element(driver_instance, authorisation_content, time_to_wait=1)
    elem1 = driver_instance.find_element_by_xpath(username_input)
    elem1.send_keys('admin')
    elem2 = driver_instance.find_element_by_xpath(password_input)
    elem2.send_keys('admin')
    driver_instance.find_element_by_xpath(button_id).click()
