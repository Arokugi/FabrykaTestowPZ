from tests.helpers.support_functions import *
import time

iframe_tab = 'iframe-header'
iframe_content = 'iframe-content'
button_1 =  '//*[@id="simpleButton1"]'
button_2 = '//*[@id="simpleButton2"]'
button_message = '//*[@id="whichButtonIsClickedMessage"]'


def click_iframe_tab(driver_instance):
    elem = driver_instance.find_element_by_id(iframe_tab)
    elem.click()

def iframe_content_visible(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, iframe_content)
    return elem.is_displayed()

def button_1_click(driver_instance):
    elem = driver_instance.find_element_by_xpath(button_1)
    elem.click()

def button_2_click(driver_instance):
    elem = driver_instance.find_element_by_xpath(button_2)
    elem.click()

def button_message_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, button_message)
    return elem.is_displayed()

