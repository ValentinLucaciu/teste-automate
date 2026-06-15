from playwright.sync_api import Page, expect

def test_flux_cumparaturi(page: Page):
    # 1. Mergem pe site
    page.goto("https://www.saucedemo.com/")
    
    # 2. Ne logăm (folosind codul tău care a mers)
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    
    # 3. Verificăm că am ajuns pe pagina de produse
    expect(page.locator("[data-test='title']")).to_have_text("Products")
    
    # 4. PAS NOU: Dăm click pe butonul "Add to cart" al rucsacului
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    
    # 5. PAS NOU: Dăm click la dreapta sus pe iconița de coș
    page.locator("[data-test='shopping-cart-link']").click()
    
    # 6. PAS NOU: Verificăm că am ajuns în coș (titlul paginii trebuie să fie "Your Cart")
    expect(page.locator("[data-test='title']")).to_have_text("Your Cart")
    
    # 7. PAS NOU: Verificăm că rucsacul (Sauce Labs Backpack) se află în listă
    expect(page.locator("[data-test='inventory-item-name']")).to_have_text("Sauce Labs Backpack")