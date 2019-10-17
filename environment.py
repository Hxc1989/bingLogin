from selenium import webdriver


def before_all(context):
    context.driver = webdriver.Chrome()
def before_feature(context, feature):
    pass
def before_scenario(context, scenario):
    pass
def after_all(context):
    context.driver.quit()
