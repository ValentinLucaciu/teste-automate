from playwright.sync_api import Page, expect

def test_cautare_wikipedia(page: Page):
    # 1. Mergem pe Wikipedia în limba română
    page.goto("https://ro.wikipedia.org/")
    
    # 2. Căutăm bara de căutare și scriem "Python"
    # (Pe Wikipedia, bara de căutare are numele de clasă "cdx-text-input__input")
    page.get_by_placeholder("Căutare în Wikipedia").first.fill("Python")
    
    # 3. Apăsăm tasta Enter de la tastatură pentru a trimite căutarea
    page.keyboard.press("Enter")
    
    # 4. Verificăm dacă titlul principal al paginii pe care am ajuns este "Python"
    expect(page.locator("#firstHeading")).to_have_text("Python")