from selenium.webdriver.common.by import By


class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    FROM_INPUT = (By.ID, "from")

    SUPPORTIVE_PLAN = (By.XPATH, "//div[text()='Supportive']")
    PHONE_INPUT = (By.ID, "phone")
    PAYMENT_METHOD_BUTTON = (By.XPATH, "//div[text()='Payment method']")
    TO_INPUT = (By.ID, "to")
    CVV_INPUT = (By.ID, "code")
    NUMBER_INPUT = (By.ID, "number")
    ADD_CARD_BUTTON = (By.XPATH, "//div[text()='Add card']")
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    MESSAGE_INPUT = (By.ID, "comment")
    BLANKET_CHECKBOX = (By.XPATH, "//div[text()='Blanket and handkerchiefs']/following-sibling::div//input")
    ICE_CREAM_PLUS_DIV = (By.XPATH, "//div[text()='Ice cream']/following-sibling::div//div[@class='counter-plus']")
    SEARCH_MODAL = (By.CLASS_NAME, "order")
    BUTTON_CALL_A_TAXI = (By.XPATH, "//button[text()='Call a taxi']")

    #part 2 #

    def set_from(self, address):
        element = self.driver.find_element(*self.FROM_INPUT)
        element.send_keys(address)

    def set_to(self, address):
        element = self.driver.find_element(*self.TO_INPUT)
        element.send_keys(address)

    def select_supportive_plan(self):
        element = self.driver.find_element(*self.SUPPORTIVE_PLAN)
        element.click()

    def set_phone(self,phone):
        element = self.driver.find_element(*self.PHONE_INPUT)
        element.send_keys(phone)

    def click_payment_method(self):
        element = self.driver.find_element(*self.PAYMENT_METHOD_BUTTON)
        element.click()

    def set_card_number(self,number):
        element = self.driver.find_element(*self.NUMBER_INPUT)
        element.send_keys(number)

    def set_cvv(self,cvv):
        element = self.driver.find_element(*self.CVV_INPUT)
        element.send_keys(cvv)

    def click_add_card_button(self):
        element = self.driver.find_element(*self.ADD_CARD_BUTTON)
        element.click()

    def click_link_button(self):
        element = self.driver.find_element(*self.LINK_BUTTON)
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