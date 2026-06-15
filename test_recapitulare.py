from playwright.sync_api import Page, expect

def test_recapitulare(page: Page):
    page.goto("https://www.emag.ro")

    page.hover("text=Laptop, Tablete & Telefoane")

    page.click("text=Laptopuri")

    page.click("text=asus")

    page.click("text=Refuză toate")

    expect(page.locator("h1")).to_contain_text("Laptopuri ASUS")

    page.wait_for_timeout(6000)
    