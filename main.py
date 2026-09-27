#Task 3
import time
import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:

#Task 1
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.get(data.URBAN_ROUTES_URL)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        assert urban_routes_page.get_from_location() == data.ADDRESS_FROM
        assert urban_routes_page.get_to_location() == data.ADDRESS_TO


    def test_select_plan(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_call_a_taxi_button()
        urban_routes_page.click_supportive_plan_button()
        assert urban_routes_page.get_active_plan() == data.SUPPORTIVE_PLAN


    def test_fill_phone_number(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_phone_number()
        urban_routes_page.enter_phone_number(data.PHONE_NUMBER)
        urban_routes_page.click_confirm_phone_number()
        sms_code = helpers.retrieve_phone_code(self.driver)
        urban_routes_page.enter_sms_code(sms_code)
        urban_routes_page.click_confirm_sms_code()
        assert urban_routes_page.get_phone_number() == data.PHONE_NUMBER



    def test_fill_card(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_payment_method()
        urban_routes_page.click_add_card()
        urban_routes_page.enter_card_number(data.CARD_NUMBER)
        urban_routes_page.click_cvv_code()
        urban_routes_page.enter_cvv_code(data.CARD_CODE)
        urban_routes_page.shift_focus_from_cvv()
        urban_routes_page.click_link_card()
        assert urban_routes_page.get_payment_method() == data.PAYMENT_METHOD_TEXT
        urban_routes_page.click_close_payment_method()

    def test_comment_for_driver(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.enter_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert urban_routes_page.get_message_for_driver() == data.MESSAGE_FOR_DRIVER


    def test_order_blanket_and_handkerchiefs(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_blanket_and_handkerchiefs()
        assert urban_routes_page.is_blanket_and_handkerchiefs_checked()


    def test_order_2_ice_creams(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.order_two_ice_creams()
        assert urban_routes_page.get_ice_cream_counter() == "2"

    def test_car_search_model_appears(self):
        urban_routes_page = UrbanRoutesPage(self.driver)
        urban_routes_page.click_order_button()
        assert urban_routes_page.is_search_modal_shown()

#Task 1
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
