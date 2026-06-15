from playwright.sync_api import Page, expect
from login_page import LoginPage

def test_login_invalid_cu_pom(page: Page):
    # 1. Inițializăm pagina folosind modelul POM
    login_pg = LoginPage(page)
    
    # 2. Executăm pașii cu funcții simple, logice
    login_pg.navigheaza()
    login_pg.login("utilizator_gresit", "parola_incorecta")
    
    # 3. Verificăm rezultatul
    expect(login_pg.error_message).to_be_visible()
    expect(login_pg.error_message).to_contain_text("Your username is invalid!")