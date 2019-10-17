# coding:utf-8
from behave import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import pageObject as homepage
import time


@Step('i open cn.bing.com')
def step_impl(context):
    homepage.Open(context)


@Step('input username and password: "{username}" "{password}"')
def step_impl(context, username, password):
    homepage.Login_Button(context).click()
    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, 'i0116')))
    homepage.Username_Inputbox(context).send_keys(username)
    time.sleep(2)
    homepage.Click_Nextstep(context)

    WebDriverWait(context.driver, 20).until(EC.presence_of_element_located((By.ID, 'i0118')))
    homepage.Password_Inputbox(context).send_keys(password)
    time.sleep(2)
    homepage.Click_Login(context)

    time.sleep(2)


@Step('login successfully')
def step_impl(context):
    assert homepage.Login_Button(context).get_attribute('aria-hidden').__contains__('true')

