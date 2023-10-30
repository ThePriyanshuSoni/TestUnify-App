from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from UnifyNG.POM.Locators.Locators import Locators
import random
import string


class AddNgCreatorPage():

    def __init__(self, driver):
        self.driver = driver
        self.form_title_textbox_id        = "formTitle"
        self.save_button_xpath            = "//button[normalize-space()='Save']"
        self.discard_button_xpath         = "//button[normalize-space()='Discard']"
        # Builder Page Locators
        self.text_form_xpath              = "//span[normalize-space()='Text']"
        self.text_area_form_xpath         = "//span[normalize-space()='Text Area']"
        self.email_form_xpath             = "//span[normalize-space()='Email']"
        self.checkbox_form_xpath          = "//span[normalize-space()='Checkbox']"
        self.select_form_xpath            = "//span[normalize-space()='Select']"
        self.number_form_xpath            = "//span[normalize-space()='Number']"
        self.radio_form_xpath             = "//span[normalize-space()='Radio']"
        self.date_form_xpath              = "//span[normalize-space()='Date']"
        self.datetime_form_xpath          = "//span[normalize-space()='DateTime']"
        self.subform_form_xpath           = "//span[normalize-space()='Sub-Form']"
        self.preview_button_xpath         = "//button[normalize-space()='Preview']"
        self.back_button_xpath            = "//button[normalize-space()='Back']"

        # Action Button Locators
        self.action_three_dot_button_xpath = "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/button[1]/*[name()='svg'][1]"
        self.dot_edit_xpath                = "//li[normalize-space()='Edit']"
        self.dot_delete_xpath              = "//li[normalize-space()='Delete']"
        self.dot_rename_form_xpath         = "//li[normalize-space()='Rename form']"
        self.dot_export_xpath              = "//li[normalize-space()='Export']"
        self.pencil_edit_icon_xpath        = "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/span[1]/*[name()='svg'][1]/*[name()='path'][1]"
        self.delete_icon_xpath             = "//div[@class='MuiBox-root css-0']//div[1]//div[1]//div[2]//span[1]//span[3]//*[name()='svg']//*[name()='path' and contains(@d,'M6 19c0 1.')]"
        # NG Creator List Locators
        self.first_form_name_list_xpath    = "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]"
        self.add_data_button_xpath         = "//button[normalize-space()='Add Data']"
        self.add_text_textbox_xpath        = "/html[1]/body[1]/div[1]/div[2]/div[1]/main[1]/div[4]/div[1]/input[1]"

        # POP UP Locators
        self.text_field_name_textbox_xpath   = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]"
        self.text_placeholder_textbox_xpath  = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[2]/div[1]/div[1]/input[1]"
        self.text_regex_textbox_xpath        = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[3]/div[1]/div[1]/input[1]"

        self.search_checkbox_id              = "is_searchable"
        self.mandatory_field_checkbox_id     = "is_required"

        self.text_a_field_name_textbox_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]"
        self.text_a_placeholder_textbox_xpath= "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[2]/div[1]/div[1]/input[1]"
        self.text_a_regex_textbox_xpath      = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[3]/div[1]/div[1]/input[1]"

        self.email_field_name_textbox_xpath  = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]"
        self.email_placeholder_textbox_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[2]/div[1]/div[1]/input[1]"
        self.email_regex_textbox_xpath       = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[3]/div[1]/div[1]/input[1]"

        self.checkbox_field_name_textbox_xpath  = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]"
        self.checkbox_regex_textbox_xpath       = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[2]/div[1]/div[1]/input[1]"

        self.select_field_name_textbox_xpath  = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]"
        self.select_regex_textbox_xpath       = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[2]/div[1]/div[1]/input[1]"
        self.select_add_option_button_xpath = "//button[normalize-space()='Add Option']"
        self.select_option_textbox_xpath = "//input[@placeholder='Option']"
        self.select_remove_button_xpath = "//button[normalize-space()='Remove Option']"

        self.number_field_name_textbox_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]"
        self.number_placeholder_textbox_xpath= "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[2]/div[1]/div[1]/input[1]"
        self.number_regex_textbox_xpath      = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[3]/div[1]/div[1]/input[1]"

        self.date_field_name_textbox_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]"

        self.datetime_field_name_textbox_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]"

        self.subform_field_name_textbox_xpath = "//body/div[@role='presentation']/div[@role='presentation']/div[@role='dialog']/div[@class='MuiDialogContent-root css-ypiqx9-MuiDialogContent-root']/div/div[1]/div[1]/div[1]/input[1]"
        self.subform_add_new__row_button_xpath = "//button[normalize-space()='Add New Row']"
        self.subform_select_field_dropdown_id  = "subform_fields"
        self.text_drop_select_xpath            = "//li[normalize-space()='Text']"
        self.add_data_placeholder_textbox_xpath= "//input[@class='additionalData']"
        self.save_button_placeholder_xpath     = "//button[@class='MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium css-rb3asp-MuiButtonBase-root-MuiButton-root']"

        self.close_icon_button_xpath           = "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-sizeMedium css-lc2yqr-MuiButtonBase-root-MuiIconButton-root']//*[name()='svg']"

    def enter_form_title(self, title):
        self.driver.find_element(By.ID, self.form_title_textbox_id).send_keys(title)

    def clear_form_title_backspace(self):
        self.driver.find_element(By.ID, self.form_title_textbox_id).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)

    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.save_button_xpath).click()

    def click_discard_button(self):
        self.driver.find_element(By.XPATH, self.discard_button_xpath).click()

    def click_back_button(self):
        self.driver.find_element(By.XPATH, self.back_button_xpath).click()

    # Text Form in Builder Page
    def click_text_form(self):
        self.driver.find_element(By.XPATH, self.text_form_xpath).click()

    def enter_text_field_name(self, text1):
        self.driver.find_element(By.XPATH, self.text_field_name_textbox_xpath).send_keys(text1)

    def enter_text_placeholder(self, text1):
        self.driver.find_element(By.XPATH, self.text_placeholder_textbox_xpath).send_keys(text1)

    def enter_text_regex(self, f3):
        self.driver.find_element(By.XPATH, self.text_regex_textbox_xpath).send_keys(f3)

    # Text Area Form in Builder Page

    def click_text_area_form(self):
        self.driver.find_element(By.XPATH, self.text_area_form_xpath).click()

    def enter_text_a_field_name(self, f1):
        self.driver.find_element(By.XPATH, self.text_field_name_textbox_xpath).send_keys(f1)

    def enter_text_a_placeholder(self, f2):
        self.driver.find_element(By.XPATH, self.text_placeholder_textbox_xpath).send_keys(f2)

    def enter_text_a_regex(self, f3):
        self.driver.find_element(By.XPATH, self.text_regex_textbox_xpath).send_keys(f3)

    # Email in Builder Page

    def click_email_form(self):
        self.driver.find_element(By.XPATH, self.email_form_xpath).click()

    def enter_email_field_name(self, k1):
        self.driver.find_element(By.XPATH, self.email_field_name_textbox_xpath).send_keys(k1)

    def enter_email_placeholder(self, k2):
        self.driver.find_element(By.XPATH, self.email_placeholder_textbox_xpath).send_keys(k2)

    def enter_email_regex(self, f3):
        self.driver.find_element(By.XPATH, self.email_regex_textbox_xpath).send_keys(f3)

    # Checkbox in Builder Page

    def click_checkbox_form(self):
        self.driver.find_element(By.XPATH, self.checkbox_form_xpath).click()

    def enter_checkbox_field_name(self, f2):
        self.driver.find_element(By.XPATH, self.checkbox_field_name_textbox_xpath).send_keys(f2)

    def enter_checkbox_regex(self, f3):
        self.driver.find_element(By.XPATH, self.checkbox_regex_textbox_xpath).send_keys(f3)

    # Select in Builder Page

    def click_select_form(self):
        self.driver.find_element(By.XPATH, self.select_form_xpath).click()

    def enter_select_field_name(self, p1):
        self.driver.find_element(By.XPATH, self.select_field_name_textbox_xpath).send_keys(p1)

    def enter_select_regex(self, f3):
        self.driver.find_element(By.XPATH, self.select_regex_textbox_xpath).send_keys(f3)

    def click_add_option(self):
        self.driver.find_element(By.XPATH, self.select_add_option_button_xpath).click()

    def enter_option(self):
        self.driver.find_element(By.XPATH, self.select_option_textbox_xpath).send_keys(''.join(random.choices(string.ascii_lowercase, k=8)))

    def click_remove_option(self):
        self.driver.find_element(By.XPATH, self.select_remove_button_xpath).click()

    # Number in Builder Page

    def click_number_form(self):
        self.driver.find_element(By.XPATH, self.number_form_xpath).click()

    def enter_number_field_name(self, q1):
        self.driver.find_element(By.XPATH, self.number_field_name_textbox_xpath).send_keys(q1)

    def enter_number_placeholder(self, q2):
        self.driver.find_element(By.XPATH, self.number_placeholder_textbox_xpath).send_keys(q2)

    def enter_number_regex(self, f3):
        self.driver.find_element(By.XPATH, self.number_regex_textbox_xpath).send_keys(f3)

    # Radio in Builder Page

    def click_radio_form(self):
        self.driver.find_element(By.XPATH, self.radio_form_xpath).click()

    # Date in Builder Page

    def click_date_form(self):
        self.driver.find_element(By.XPATH, self.date_form_xpath).click()

    def enter_date_field_name(self):
        self.driver.find_element(By.XPATH, self.date_field_name_textbox_xpath).send_keys(''.join(random.choices(string.ascii_lowercase, k=8)))

    # DateTime in Builder Page

    def click_datetime_form(self):
        self.driver.find_element(By.XPATH, self.datetime_form_xpath).click()

    def enter_datetime_field_name(self):
        self.driver.find_element(By.XPATH, self.datetime_field_name_textbox_xpath).send_keys(''.join(random.choices(string.ascii_lowercase, k=8)))

    # Sub-Form in Builder Page

    def click_sub_form(self):
        self.driver.find_element(By.XPATH, self.subform_form_xpath).click()

    def enter_sub_form_field_name(self):
        self.driver.find_element(By.XPATH, self.subform_field_name_textbox_xpath).send_keys(''.join(random.choices(string.ascii_lowercase, k=8)))


    def click_search_option(self):
        self.driver.find_element(By.ID, self.search_checkbox_id).click()

    def click_mandatory(self):
        self.driver.find_element(By.ID, self.mandatory_field_checkbox_id).click()

    def click_preview(self):
        self.driver.find_element(By.XPATH, self.preview_button_xpath).click()

    def click_action_three_dot(self):
        self.driver.find_element(By.XPATH, self.action_three_dot_button_xpath).click()

    def click_action_edit(self):
        self.driver.find_element(By.XPATH, self.dot_edit_xpath).click()

    def click_action_delete(self):
        self.driver.find_element(By.XPATH, self.dot_delete_xpath).click()

    def click_dot_rename_form(self):
        self.driver.find_element(By.XPATH, self.dot_rename_form_xpath).click()

    def click_dot_export(self):
        self.driver.find_element(By.XPATH, self.dot_export_xpath).click()

    def click_pencil_edit(self):
        self.driver.find_element(By.XPATH, self.pencil_edit_icon_xpath).click()

    def click_delete_icon(self):
        self.driver.find_element(By.XPATH, self.delete_icon_xpath).click()

    def click_add_new_row(self):
        self.driver.find_element(By.XPATH, self.subform_add_new__row_button_xpath).click()

    def click_select_field(self):
        self.driver.find_element(By.ID, self.subform_select_field_dropdown_id).click()

    def click_dropdown_text(self):
        self.driver.find_element(By.XPATH, self.text_drop_select_xpath).click()

    # NG Creator List Locators

    def click_first_form_name(self):
        self.driver.find_element(By.XPATH, self.first_form_name_list_xpath).click()

    def click_add_data_button(self):
        self.driver.find_element(By.XPATH, self.add_data_button_xpath).click()

    def enter_text_data(self, a):
        self.driver.find_element(By.XPATH, self.add_text_textbox_xpath).send_keys(a)

    def enter_add_data_placeholder(self, a1):
        self.driver.find_element(By.XPATH, self.add_data_placeholder_textbox_xpath).send_keys(a1)

    def click_save_button_placeholder(self):
        self.driver.find_element(By.XPATH, self.save_button_placeholder_xpath).click()

    def click_close_button_icon(self):
        self.driver.find_element(By.XPATH, self.close_icon_button_xpath).click()
