def test_promote_manager_two_times(page):
    # Make sure db is empty
    page.goto("/reset_db")
    page.locator("button:has-text('proceed')").click()

    # Create an employee
    page.goto("/")
    page.goto("/add_employee")
    page.locator('input[name="name"]').fill("Kevin Tournepine")
    page.locator('input[name="email"]').fill("kevin.tournepine@gmail.com")
    page.locator('input[name="address_line1"]').fill("500 Voilorage")
    page.locator('input[name="city"]').fill("Voilorage")
    page.locator('input[name="zip_code"]').fill("50069")
    page.locator('input[name="hiring_date"]').fill("2025-01-28")
    page.locator('input[name="job_title"]').fill("Expert Fiscal")

    page.locator("button:has-text('Add')").click()

    # Goto employees list
    page.goto("/employees")

    # First Promotion
    page.locator("a:has-text('Edit')").click()
    page.locator("a:has-text('Promote as manager')").click()
    page.locator("button:has-text('proceed')").click()

    # Goto employees list
    page.goto("/employees")

    #Second Promotion
    page.locator("a:has-text('Edit')").click()

    # Check promotion still available
    assert page.is_visible(f"a:has-text('Promote as manager')")