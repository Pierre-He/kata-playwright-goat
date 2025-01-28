from datetime import date
from conftest import *

def test_invalid_date(page) -> None:
    # reset_database(page)
    page.goto("https://g.se1.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("test_employe_date")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("testemploye.date@gmail.com")
    page.get_by_role("group", name="Address").click()
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("XX")
    page.locator("html").click()
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("XX")
    page.get_by_placeholder("Zip code").click()
    page.get_by_placeholder("Zip code").fill("12345")
    page.get_by_placeholder("Hiring date").click()
    page.get_by_placeholder("Hiring date").fill("1000-01-01")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("test_job_date")
    page.get_by_role("button", name="Add").click()
    assert page.url == "https://g.se1.hr.dmerej.info/add_employee" # Vérifie qu'on reste sur le formulaire
    # assert page.get_by_text("Invalid date").is_visible()  # Vérifie l'erreur
    page.get_by_placeholder("Hiring date").fill(date.today().strftime("%Y-%m-%d"))
    page.get_by_role("button", name="Add").click()
    assert page.url == "https://g.se1.hr.dmerej.info/employees"
    assert page.locator("tbody").to_contain_text("test_employe_date")

