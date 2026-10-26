from selenium import webdriver
from pages import UrbanRoutesPage
import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
            cls.driver.get(data.URBAN_ROUTES_URL)
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        page = UrbanRoutesPage(self.driver)
        page.set_from(data.ADDRESS_FROM)
        page.set_to(data.ADDRESS_TO)

    def test_select_plan(self):
        page = UrbanRoutesPage(self.driver)
        page.select_supportive_plan()

    def test_fill_phone_number(self):
        page = UrbanRoutesPage(self.driver)
        page.set_phone(data.PHONE_NUMBER)

    def test_fill_card(self):
        page = UrbanRoutesPage(self.driver)
        page.set_card_number(data.CARD_NUMBER)
        page.set_cvv(data.CARD_CODE)
        page.click_add_card_button()

    def test_comment_for_driver(self):
        page = UrbanRoutesPage(self.driver)
        page.set_message(data.MESSAGE_FOR_DRIVER)

    def test_order_blanket_and_handkerchiefs(self):
        page = UrbanRoutesPage(self.driver)
        page.click_blanket_checkbox()

    def test_order_2_ice_creams(self):
        page = UrbanRoutesPage(self.driver)
        for _ in range(2):
            page.click_ice_cream_plus_div()


        page = UrbanRoutesPage(self.driver)
        page.select_supportive_plan()
        page.set_message("hello there")
        page.click_call_taxi_button()
        assert page.is_car_search_modal_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
