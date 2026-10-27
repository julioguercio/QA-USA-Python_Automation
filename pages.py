import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException

class UrbanRoutesPage:

    def __init__(self, driver):
        self.driver = driver

    FROM_INPUT = (By.ID, "from")

    SUPPORTIVE_PLAN = (By.XPATH, "//div[text()='Supportive']")
    ACTIVE_SUPPORTIVE_PLAN = (
        By.XPATH,
        "//div[contains(@class, 'tcard') and "
        "contains(@class, 'active') and "
        ".//*[text()='Supportive']]")
    PHONE_INPUT = (By.ID, "phone")
    TO_INPUT = (By.ID, "to")
    NUMBER_INPUT = (By.ID, "number")
    PAYMENT_METHOD_BUTTON = (By.CLASS_NAME, "pp-text")
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    MESSAGE_INPUT = (By.ID, "comment")
    BLANKET_CHECKBOX = (By.XPATH, "//div[text()='Blanket and handkerchiefs']/following-sibling::div//span")
    ICE_CREAM_PLUS_DIV = (By.XPATH, "//div[text()='Ice cream']/following-sibling::div//div[@class='counter-plus']")
    SEARCH_MODAL = (By.CLASS_NAME, "order")
    BUTTON_CALL_A_TAXI = (By.XPATH, "//button[text()='Call a taxi']")
    ADD_CARD_BUTTON = (By.XPATH, "//div[@class='pp-title' and text()='Add card']")
    CVV_INPUT = (By.XPATH, "//input[@id='code' and @class='card-input']")

    #part 2 #

    def set_from(self, address):
        element = self.driver.find_element(*self.FROM_INPUT)
        element.send_keys(address)

    def get_from(self):
        element = self.driver.find_element(*self.FROM_INPUT)
        return element.get_attribute("value")

    def set_to(self, address):
        element = self.driver.find_element(*self.TO_INPUT)
        element.send_keys(address)

    def select_supportive_plan(self):
        self.click_call_taxi_button()
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUPPORTIVE_PLAN)
        )
        element.click()

    def is_supportive_active(self):
        element = self.driver.find_element(*self.ACTIVE_SUPPORTIVE_PLAN)
        return element.is_displayed()

    def set_phone(self,phone):
        element = self.driver.find_element(*self.PHONE_INPUT)
        element.send_keys(phone)

    def get_phone(self):
        element = self.driver.find_element(*self.PHONE_INPUT)
        return element.get_attribute("value")

    def click_payment_method(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.PAYMENT_METHOD_BUTTON)
        )
        element.click()

    def get_card_number(self):
        element = self.driver.find_element(*self.NUMBER_INPUT)
        return element.get_attribute("value")

    def set_card_number(self, number):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.NUMBER_INPUT)
        )
        element.send_keys(number)


    def set_cvv(self, cvv):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.CVV_INPUT)
        )
        element.send_keys(cvv)

    def click_add_card_button(self):
        attempts = 0
        while attempts < 3:
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.ADD_CARD_BUTTON)
                )
                element.click()
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NUMBER_INPUT))
                return
            except StaleElementReferenceException:
                attempts += 1

    def click_link_button(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.LINK_BUTTON)
        )
        element.click()

    def set_message(self,message):
        element = self.driver.find_element(*self.MESSAGE_INPUT)
        element.send_keys(message)

    def click_blanket_checkbox(self):
        element = self.driver.find_element(*self.BLANKET_CHECKBOX)
        element.click()

    def click_ice_cream_plus_div(self):
        element =self.driver.find_element(*self.ICE_CREAM_PLUS_DIV)
        element.click()

    def is_car_search_modal_displayed(self):
        element = self.driver.find_element(*self.SEARCH_MODAL)
        return element.is_displayed()

    def click_call_taxi_button(self):
        element = self.driver.find_element(*self.BUTTON_CALL_A_TAXI)
        element.click()