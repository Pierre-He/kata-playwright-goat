import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://g.se1.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("test_employee")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("test_employee@gmail.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("117 Avenue de l'endroit")
    page.locator("#id_address_line2").click()
    page.get_by_placeholder("Hiring date").fill("2025-01-25")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("Test_job")
    page.get_by_role("button", name="Add").click()
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("Test_City")
    page.get_by_role("button", name="Add").click()
    page.get_by_placeholder("Zip code").click()
    page.get_by_placeholder("Zip code").fill("12345")
    page.get_by_role("button", name="Add").click()
    expect(page.get_by_role("cell", name="test_employee", exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name="test_employee@gmail.com")).to_be_visible()
    expect(page.get_by_role("cell", name="no")).to_be_visible()
    expect(page.get_by_role("cell", name="Edit")).to_be_visible()
    expect(page.get_by_role("cell", name="Delete")).to_be_visible()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
