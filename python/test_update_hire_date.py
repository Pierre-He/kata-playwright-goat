import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_update_hire_date(page, add_employee, reset_database):
    # Make sure db is empty
    reset_database()
    # Add an employee
    add_employee()
    
    # Naviguer vers la page de mise à jour du contrat
    page.get_by_role("link", name="Edit").nth(1).click()
    page.get_by_role("link", name="Update contract").click()
    
    # Localiser le champ "Hiring date"
    hiring_date_input = page.locator("input#id_hiring_date")

    # Vérifier si le champ est en lecture seule
    is_readonly = hiring_date_input.get_attribute("readonly")
    assert is_readonly is None, "Le champ 'Hiring date' est en lecture seule, mais il devrait être modifiable."

    # Remplir le champ avec une nouvelle date
    new_date = "2023-01-01"
    hiring_date_input.fill(new_date)

    # Vérifier que la valeur du champ a été mise à jour localement
    assert hiring_date_input.input_value() == new_date, \
        "Le champ 'Hiring date' n'a pas accepté la nouvelle valeur."

    # Soumettre le formulaire
    page.locator("button[type='submit']").click()

    # Revenir sur la page "Update contract"
    page.get_by_role("link", name="Update contract").click()

    # Vérifier que la nouvelle date est affichée correctement
    updated_hiring_date = page.locator("input#id_hiring_date").input_value()
    assert updated_hiring_date == new_date, \
        f"La date de 'Hiring date' n'a pas été correctement sauvegardée. Attendu : {new_date}, Observé : {updated_hiring_date}"
