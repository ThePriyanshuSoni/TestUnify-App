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

    #Add customer page objects
    crm_customerid_textbox_id = "crmCustomerId"
    firstname_textbox_id = "firstName"
    lastname_textbox_id = "lastName"
    biller_dropdown_id = "billCycleId"
    label_dropdown_id = "tags"
    notes_textbox_id = "notes"
    services_dropdown_id = "services"
    internet_drop_select_xpath = "//li[@role='option']"
    email_textbox_id = "email"
    mobile_textbox_id = "phoneNo"
    name_textbox_id = "fullName"
    addressline_textbox_id = "addressLine"
    landmark_textbox_id = "landmark"
    pincode_textbox_id = "pincode"
    city_textbox_id = "city"
    country_dropdown_id = "country"
    india_drop_select_xpath = "//li[102]"
    state_dropdown_id = "state"
    up_drop_select_xpath = "//li[normalize-space()='Uttar Pradesh']"
    comment_textbox_id = "6486f58f3dca617e7fcabaa5"
    save_button_xpath = "//button[normalize-space()='Save']"
