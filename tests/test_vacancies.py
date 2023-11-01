import pytest

from page_objects.vacancies_page import VacanciesPage


class TestVacancies:

    @pytest.mark.vacancies
    def test_vacancies(self, driver):
        vacancies_page = VacanciesPage(driver)
        vacancies_page.open()
        vacancies_page.close_cookies()
        vacancies_page.filter_department()
        vacancies_page.filter_language()
        vacancies_page.verify_results()
