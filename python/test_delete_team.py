def test_delete_team(page):
    # Make sure db is empty
    page.goto("/reset_db")
    proceed_button = page.locator("button:has-text('proceed')")
    proceed_button.click()

    # Create a team 
    page.goto("/add_team")
    name_input = page.locator('input[name="name"]')
    team_name = "my team"
    name_input.fill(team_name)
    page.click("text='Add'")

    # Create User
    page.goto("/add_employee")
    user_name = "User"
    page.locator('input[name="name"]').fill(user_name)
    page.locator('input[name="email"]').fill("test@test.tst")
    page.locator('input[name="address_line1"]').fill("111 avenu de JeSaisPas")
    page.locator('input[name="city"]').fill("Paris")
    page.locator('input[name="zip_code"]').fill("75018")
    page.locator('input[name="hiring_date"]').fill("2024-02-12")
    page.locator('input[name="job_title"]').fill("Test")
    page.click("text='Add'")

    # Add user to a team
    page.goto("/employees")
    page.click('text="Edit"')
    page.click("a:has-text('Add to team')")
    page.locator("select[name='team']").select_option(label=team_name + " team")
    page.click("text='Add'")

    # Delete team
    page.goto("/teams")
    page.click("text='Delete'")
    page.click("text='Proceed'")

    # Check the new team is there
    assert not page.is_visible(f"td:has-text('{team_name}')")
    page.goto("/employees")
    assert page.is_visible(f"td:has-text('{user_name}')")

