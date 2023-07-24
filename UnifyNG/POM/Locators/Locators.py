class Locators():

    #login page objects
    tenantName_textbox_id = "tenant"
    continue_button_xpath = "//button[normalize-space()='Continue']"
    username_textbox_id = "username"
    password_textbox_id = "password"
    tenantLogin_Button_id = "kc-login"
    invalidUsername_message_xpath = "//span[@id='input-error']"

    #home page objects
    account_link_xpath = "//button[@aria-label='account of current user']//*[name()='svg']"
    account_logout_xpath = "//li[normalize-space()='Logout']"
