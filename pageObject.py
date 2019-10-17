def Open(context):
    context.driver.get('https://cn.bing.com')
    context.driver.maximize_window()


def Search_TextBox(context):
    return context.driver.find_element_by_id('sb_form_q')


def Submit_Button(context):
    return context.driver.find_element_by_id('sb_form_go')


def Driver_Title(context):
    return context.driver.title


def Login_Button(context):
    return context.driver.find_element_by_id('id_s')


def Username_Inputbox(context):
    return context.driver.find_element_by_id('i0116')


def Password_Inputbox(context):
    return context.driver.find_element_by_id('i0118')


def Click_Nextstep(context):
    context.driver.find_element_by_id('idSIButton9').click()


def Click_Login(context):
    context.driver.find_element_by_id('idSIButton9').click()
