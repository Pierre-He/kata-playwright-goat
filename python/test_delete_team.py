from conftest import reset_database, add_employee

def test_delete_team(page, reset_database, add_employee):
    # Make sure db is empty
    reset_database()

    # Create a team 
    page.goto("/add_team")
    name_input = page.locator('input[name="name"]')
    team_name = "my team"
    name_input.fill(team_name)
    page.click("text='Add'")

    # Create User
    add_employee()

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
    assert page.is_visible(f"td:has-text('test_user')")

