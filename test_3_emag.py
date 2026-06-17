from playwright.sync_api import Page, expect

def test_pret_emag(page: Page):
    # 1. Mergem pe pagina produsului de pe eMAG
    page.goto("https://www.emag.ro/set-rampa-auto-pentru-reparatii-3-tone-anvelope-pana-la-235-mm-2-bucati-10639r/pd/DC46D0MBM/")
    
    # 2. Pentru că eMAG are uneori o bară de acceptare cookie-uri care blochează ecranul,
    # îi dăm un mic timp să încarce pagina stabil.
    page.wait_for_timeout(2000) 
    
    # 3. Verificăm că prețul principal conține textul "369"
    # Folosim selectorul [data-test='main-price']!
    expect(page.locator("[data-test='main-price']")).to_contain_text("369")

    # test  