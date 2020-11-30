from tests.helpers.support_functions import *

login_info = 'loggedInMessage'

def login_info_displayed(driver_instance):
    elem = wait_for_visibility_of_element(driver_instance, login_info)
    return elem.is_displayed()