from tests.helpers.support_functions import *
from selenium.webdriver import ActionChains


run do
  @driver.get "http://the-internet.herokuapp.com/drag_and_drop"

  dnd_javascript = File.read(Dir.pwd + '/dnd.js')
  @driver.execute_script(dnd_javascript+"jQuery('#column-a').simulateDragDrop({ dropTarget: '#column-b'});")

  @driver.find_element(id: 'column-a').text.should == 'B'
  @driver.find_element(id: 'column-b').text.should == 'A'
end
