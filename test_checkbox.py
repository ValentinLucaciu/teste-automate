from playwright.sync_api import Page, expect
# 1. Importăm variabilele din fișierul config
import config 

def test_elemente_interfata(page: Page):
    # 2. În loc de link-ul lung scriem config.URL_CHECKBOXES
    page.goto(config.URL_CHECKBOXES)
    
    prima_bifa = page.locator("input[type='checkbox']").first
    prima_bifa.check()
    expect(prima_bifa).to_be_checked()
    
    # 3. În loc de al doilea link scriem config.URL_DROPDOWN
    page.goto(config.URL_DROPDOWN)
    
    page.locator("#dropdown").select_option(label="Option 2")
    expect(page.locator("#dropdown")).to_have_value("2")
    
    page.screenshot(path="final_dropdown_bifa.png")