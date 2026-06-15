# test_login.py
from playwright.sync_api import Page, expect
# Importăm toate datele din fișierul config creat mai sus
import config 

def test_autentificare_cu_succes(page: Page):
    # Folosim variabila din config în loc de link-ul scris direct
    page.goto(config.SITE_URL)
    
    # Completăm câmpurile folosind datele din config
    page.locator("#username").fill(config.USER_VALID)
    page.locator("#password").fill(config.PAROLA_VALIDA)
    page.get_by_role("button", name="Submit").click()
    
    # Facem screenshot-ul pe care l-ai învățat data trecută
    page.screenshot(path="ecran_succes.png")
    
    # Aserțiune: verificăm dacă am ajuns pe pagina corectă
    expect(page).to_have_url("https://practicetestautomation.com/logged-in-successfully/")


def test_autentificare_esuata(page: Page):
    page.goto(config.SITE_URL)
    
    # Folosim username-ul valid, dar parola greșită din config
    page.locator("#username").fill(config.USER_VALID)
    page.locator("#password").fill(config.PAROLA_GRESITA)
    page.get_by_role("button", name="Submit").click()
    
    # Aserțiune pentru mesajul roșu de eroare
    mesaj_eroare = page.locator("#error")
    expect(mesaj_eroare).to_be_visible()
    expect(mesaj_eroare).to_contain_text("Your password is invalid!")