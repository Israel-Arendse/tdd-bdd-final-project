######################################################################
# Copyright 2016, 2021 John J. Rofrano. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
######################################################################

# pylint: disable=function-redefined, missing-function-docstring
# flake8: noqa
"""
Web Steps

Steps file for web interactions with Selenium

For information on Waiting until elements are present in the HTML see:
    https://selenium-python.readthedocs.io/waits.html
"""
import logging
from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions

ID_PREFIX = 'product_'


@when('I visit the "Home Page"')
def step_impl(context):
    """ Make a call to the base URL """
    context.driver.get(context.base_url)
    # Uncomment next line to take a screenshot of the web page
    context.driver.save_screenshot('home_page.png')

@then('I should see "{message}" in the title')
def step_impl(context, message):
    """ Check the document title for a message """
    assert(message in context.driver.title)

@then('I should not see "{text_string}"')
def step_impl(context, text_string):
    element = context.driver.find_element(By.TAG_NAME, 'body')
    assert(text_string not in element.text)

@when('I set the "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(text_string)

@when('I select "{text}" in the "{element_name}" dropdown')
def step_impl(context, text, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = Select(context.driver.find_element(By.ID, element_id))
    element.select_by_visible_text(text)

@then('I should see "{text}" in the "{element_name}" dropdown')
def step_impl(context, text, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = Select(context.driver.find_element(By.ID, element_id))
    assert(element.first_selected_option.text == text)

@then('the "{element_name}" field should be empty')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = context.driver.find_element(By.ID, element_id)
    assert(element.get_attribute('value') == u'')

##################################################################
# These two function simulate copy and paste
##################################################################
@when('I copy the "{element_name}" field')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    context.clipboard = element.get_attribute('value')
    logging.info('Clipboard contains: %s', context.clipboard)

@when('I paste the "{element_name}" field')
def step_impl(context, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(context.clipboard)

##################################################################
# This code works because of the following naming convention:
# The buttons have an id in the html hat is the button text
# in lowercase followed by '-btn' so the Clean button has an id of
# id='clear-btn'. That allows us to lowercase the name and add '-btn'
# to get the element id of any button
##################################################################

## UPDATE CODE HERE ##

@when(u'I press the "Create" button')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I press the "Create" button')
	
	
@then(u'I should see the message "Success"')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should see the message "Success"')
	
	
@when(u'I press the "Clear" button')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I press the "Clear" button')
	
	
@when(u'I press the "Retrieve" button')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I press the "Retrieve" button')
	
	
@when(u'I vist the "Home Page"')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I vist the "Home Page"')
	
	
when(u'I click the "Search" button')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I click the "Search" button')
	
	
@when(u'I press the "Name" to "Fedora"')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I press the "Name" to "Fedora"')
	

@when(u'I press the "Update" button')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I press the "Update" button')
	
	
@when(u'I press the "Search" button')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I press the "Search" button')
	
	
@then(u'I should see "Fedora" in the results')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should see "Fedora" in the results')
	
	
@then(u'I should not see "Hat" in the results')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should not see "Hat" in the results')
	
	
@then(u'I should see "Full bed sheets" in  the "Description" field')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should see "Full bed sheets" in  the "Description" field')
	
	
@when(u'I press the "Delete" button')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I press the "Delete" button')
	
	
@then(u'I should see the message "Product has been deleted"')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should see the message "Product has been deleted"')
	
	
@then(u'I should not see "Sheets" in the results')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should not see "Sheets" in the results')
	
	
@then(u'I should see "Hat" in the results')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should see "Hat" in the results')
	
	
@then(u'I should see "Shoes" in the results')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should see "Shoes" in the results')
	
	
@then(u'I should see "Big Mac" in the results')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should see "Big Mac" in the results')
	
	
@then(u'I should see "Sheets" in the results')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should see "Sheets" in the results')
	
	
@when(u'I select the "Food" category')
def step_impl(context):
	raise NotImplementedError(u'STEP: When I select the "Food" category')
	
	
@then(u'I should not see "Shoes" in the results')
def step_impl(context):
	raise NotImplementedError(u'STEP: Then I should not see "Shoes" in the results')
	
	
@then(u'I should not see "Sheets" in the resuts')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should not see "Sheets" in the results')

@when(u'I click the "Search" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click the "Search" button')

##################################################################
# This code works because of the following naming convention:
# The id field for text input in the html is the element name
# prefixed by ID_PREFIX so the Name field has an id='pet_name'
# We can then lowercase the name and prefix with pet_ to get the id
##################################################################

@then('I should see "{text_string}" in the "{element_name}" field')
def step_impl(context, text_string, element_name):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element_value(
            (By.ID, element_id),
            text_string
        )
    )
    assert(found)

@when('I change "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = ID_PREFIX + element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(text_string)
