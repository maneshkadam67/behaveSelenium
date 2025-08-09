import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'User will navigate to Home Page')
def step_impl(context):
    context.driver =webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")


@when(u'User enters product name "{product_name}"')
def step_impl(context,product_name):
    time.sleep(2)
    search_box = context.driver.find_element(By.NAME,"search")
    #search_box = context.driver.find_element(By.NAME, "q")  # Replace with your actual locator
    search_box.clear()
    search_box.send_keys(product_name)
    context.product_name=product_name



@when(u'User click on search button')
def step_impl(context):
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()



@then(u'Valid {product_name} should get displayed in search results')
def step_impl(context,product_name):
    hp_text=context.driver.find_element(By.XPATH,"//div[@class='caption']").text
    assert product_name in hp_text,"Correct product is not displaying"



@then(u'Proper message should be displayed on screen')
def step_impl(context):
    assert context.driver.find_element(By.XPATH,"//*[@id='content']/p[2]").is_displayed()

@When(u'When User enters invalid product name "{product_name}"')
def step_impl(context,product_name):
    context.driver.find_element(By.NAME, "search").send_keys(product_name)
