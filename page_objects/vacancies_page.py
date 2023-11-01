from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class VacanciesPage(BasePage):
    __url = "https://cz.careers.veeam.com/vacancies"
    __cookies = (By.XPATH, "//div[@id='cookiescript_accept']")
    __departmentsField = (By.XPATH, "//button[contains(text(),'All departments')]")
    __languagesField = (By.XPATH, "//button[contains(text(),'All languages')]")
    __departmentOption = (By.XPATH, "//a[contains(text(),'Research & Development')]")
    __languageOption = (By.XPATH, "//label[contains(text(),'English')]")
    __filteredResults = (By.XPATH, "//a[@class='card card-sm card-no-hover']")

    ### AT THE MOMENT THIS TEST IS SUBMITTED, THERE ARE 3 OPEN VACANCIES AT VEEAM CARRER FOR THIS FILTER.
    __expectedCount = 3

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)
        super()._maximize()

    def close_cookies(self):
        super()._click(self.__cookies)

    def filter_department(self):
        super()._click(self.__departmentsField)
        super()._click(self.__departmentOption)

    def filter_language(self):
        super()._click(self.__languagesField)
        super()._click(self.__languageOption)

    def verify_results(self):
        __result = super()._find_elements(self.__filteredResults)
        assert len(__result) == self.__expectedCount, "The jobs count were not as expected."
