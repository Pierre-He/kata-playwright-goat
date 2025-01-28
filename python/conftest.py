import pytest
from playwright.sync_api import Page

@pytest.fixture
def reset_database(page: Page):
    def _reset_database():
        page.goto("/reset_db")
        proceed_button = page.locator("button:has-text('proceed')")
        proceed_button.click()
    return _reset_database


@pytest.fixture
def add_employee(page: Page):
    def _add_employee(
        name="test_user",
        email="test_user@gmail.com",
        address="city test_user",
        city="Paris",
        zip_code="75020",
        hiring_date="2025-02-20",
        job_title="RH"
    ):
        # Formulaire d'ajout
        page.goto("/add_employee")
        page.get_by_placeholder("Name").fill(name)
        page.get_by_placeholder("Email").fill(email)
        page.locator("#id_address_line1").fill(address)
        page.get_by_placeholder("City").fill(city)
        page.get_by_placeholder("Zip code").fill(zip_code)
        page.get_by_placeholder("Hiring date").fill(hiring_date)
        page.get_by_placeholder("Job title").fill(job_title)
        page.get_by_role("button", name="Add").click()
    
    return _add_employee
