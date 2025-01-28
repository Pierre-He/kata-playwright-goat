from conftest import reset_database, add_employee

def test_promote_manager_two_times(page, reset_database, add_employee):
    # Make sure db is empty
    reset_database()

    # Create an employee
    add_employee()

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