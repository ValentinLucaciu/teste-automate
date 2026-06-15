import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    # Inițializăm browserul
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Navigăm pe eMAG
    page.goto("https://www.emag.ro")
    
    # 1. Gestionare Cookie-uri
    if page.get_by_role("button", name="Acceptă tot").is_visible():
        page.get_by_role("button", name="Acceptă tot").click()
        
    # 2. Deschidem meniul prin Hover
    page.get_by_text("Laptop, Tablete & Telefoane").first.hover()
    
    # 3. Click pe Laptopuri Gaming (varianta flexibilă)
    page.get_by_role("link", name="Laptopuri Gaming", exact=False).click()
    
    # 4. Intrăm pe primul laptop din listă
    page.locator(".card-v2-title").first.click()
    
    # 5. Targetăm fix butonul de favorite din zona principală a paginii
    # Folosim locatorul părintelui (#main-container) și căutăm butonul în interiorul lui
    buton_favorite = page.locator("#main-container").get_by_role("button", name="Adauga la Favorite")
    
    # Îi dăm un force=True în caz că eMAG îl consideră tehnic "disabled" în prima sutime de secundă
    buton_favorite.click(force=True)
    
    # 6. Verificarea finală
    expect(page.locator("body")).to_contain_text("Favorite", exact=False)
    
    # Închidem sesiunea curat
    context.close()
    browser.close()

# Linia de pornire a scriptului
with sync_playwright() as playwright:
    run(playwright)