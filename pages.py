#Task 2
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    CALL_A_TAXI_BUTTON = (By.XPATH, '//button[contains(text(),"Call a taxi")]')
    SUPPORTIVE_PLAN_BUTTON = (By.XPATH, '//div[contains(text(), "Supportive")]')
    ACTIVE_PLAN = (By.XPATH, '//div[contains(@class, "tcard active")]//div[@class="tcard-title"]')
    CLICK_PHONE_NUMBER = (By.CLASS_NAME, "np-text")
    ENTER_PHONE_NUMBER = (By.ID, "phone")
    PAYMENT_METHOD = (By.CLASS_NAME, "pp-button")
    ADD_CARD = (By.XPATH, '//div[contains(text(), "Add card")]')
    CARD_NUMBER = (By.ID, "number")
    CVV_CODE = (By.XPATH, '//input[contains(@name, "code")]')
    LINK_CARD = (By.XPATH, '//button[contains(text(), "Link")]')
    CLOSE_PAYMENT_METHOD = (By.XPATH, '//div[@class="head" and text()="Payment method"]/parent::div//button[contains(@class, "close-button")]')
    CONFIRM_PHONE_NUMBER = (By.XPATH, '//button[contains(text(), "Next")]')
    SMS_CODE = (By.XPATH, '//input[contains(@placeholder, "xxxx")]')
    CONFIRM_SMS_CODE = (By.XPATH, '//button[contains(text(), "Confirm")]')
    MESSAGE_FOR_DRIVER = (By.ID, "comment")
    ORDER_REQUIREMENTS = (By.CLASS_NAME, 'reqs-head')
    BLANKET_AND_HANDKERCHIEFS = (By.XPATH, '//div[contains(.,"Blanket and handkerchiefs")]/ancestor::div//span[@class = "slider round"]')
    BLANKET_AND_HANDKERCHIEFS_CHECKED = (By.XPATH, '//div[contains(text(),"Blanket and handkerchiefs")]/ancestor::div//input[@type = "checkbox" and @checked]')
    ADD_ICE_CREAM = (By.XPATH, '//div[contains(text(), "Ice cream")]/ancestor::div//div[contains(@class, "counter-plus")]')
    ORDER_BUTTON = (By.CLASS_NAME, "smart-button")
    PAYMENT_METHOD_TEXT = (By.CLASS_NAME, "pp-value-text")
    ICE_CREAM_COUNTER = (By.XPATH, '//div[contains(text(), "Ice cream")]/ancestor::div//div[contains(@class, "counter-value")]')
    ORDER_MODAL_SHOWN = (By.CLASS_NAME, "order-body")


    def __init__(self, driver):
        self.driver = driver

    def enter_locations(self, from_text, to_text):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_text)
        self.driver.find_element(*self.TO_FIELD).send_keys(to_text)

    def click_call_a_taxi_button(self):
        self.driver.find_element(*self.CALL_A_TAXI_BUTTON).click()

    def click_supportive_plan_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUPPORTIVE_PLAN_BUTTON)).click()

    def enter_phone_number(self, phone_number):
        WebDriverWait (self.driver, 10).until(
            EC.visibility_of_element_located(self.ENTER_PHONE_NUMBER)).send_keys(phone_number)

    def click_payment_method(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PAYMENT_METHOD)).click()

    def click_add_card(self):
        self.driver.find_element(*self.ADD_CARD).click()

    def enter_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_number)

    def click_cvv_code(self):
        self.driver.find_element(*self.CVV_CODE).click()

    def enter_cvv_code(self, cvv_code):
        self.driver.find_element(*self.CVV_CODE).send_keys(cvv_code)

    def click_link_card(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Link")]'))).click()

    def click_close_payment_method(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CLOSE_PAYMENT_METHOD)).click()

    def click_phone_number(self):
        self.driver.find_element(*self.CLICK_PHONE_NUMBER).click()

    def click_confirm_phone_number(self):
        self.driver.find_element(*self.CONFIRM_PHONE_NUMBER).click()

    def enter_sms_code(self, sms_code):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SMS_CODE)).send_keys(sms_code)

    def click_confirm_sms_code(self):
        self.driver.find_element(*self.CONFIRM_SMS_CODE).click()

    def enter_message_for_driver(self, message):
        self.driver.find_element(*self.MESSAGE_FOR_DRIVER).send_keys(message)

    def click_order_requirements(self):
        self.driver.find_element(*self.ORDER_REQUIREMENTS).click()

    def click_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS).click()

    def is_blanket_and_handkerchiefs_checked(self):
        try:
            self.driver.find_element(*self.BLANKET_AND_HANDKERCHIEFS_CHECKED)
            return True
        except NoSuchElementException:
            return False

    def add_ice_cream(self):
        self.driver.find_element(*self.ADD_ICE_CREAM).click()

    def order_two_ice_creams(self):
        for i in range(2):
            self.add_ice_cream()

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def get_from_location(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")

    def get_to_location(self):
        return self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    def get_active_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN).text

    def get_phone_number(self):
        return self.driver.find_element(*self.ENTER_PHONE_NUMBER).get_attribute("value")

    def shift_focus_from_cvv(self):
        self.driver.find_element(*self.CVV_CODE).send_keys(Keys.TAB)

    def get_payment_method(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_TEXT).text

    def get_message_for_driver(self):
        return self.driver.find_element(*self.MESSAGE_FOR_DRIVER).get_attribute("value")

    def get_ice_cream_counter(self):
        return self.driver.find_element(*self.ICE_CREAM_COUNTER).text

    def is_search_modal_shown(self):
        try:
            return self.driver.find_element(*self.ORDER_MODAL_SHOWN).is_displayed()
        except NoSuchElementException:
            return False