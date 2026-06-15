from playwright.sync_api import playwright

# Testul 1: Verificăm că putem CITI o postare (GET)
def test_citire_postare(playwright):
    # Inițializăm contextul de API direct din Playwright
    api_context = playwright.request.new_context()
    
    # Trimitem cererea către postarea cu ID-ul 1
    response = api_context.get("https://jsonplaceholder.typicode.com/posts/1")
    
    # Verificăm statusul: 200 OK
    assert response.status == 200
    
    # Extragerea datelor în format JSON
    date_postare = response.json()
    
    # Verificăm că postarea aparține utilizatorului cu userId = 1
    assert date_postare["userId"] == 1
    # Verificăm că ID-ul postării este cel corect
    assert date_postare["id"] == 1
    
    print("\n[GET SUCCESS] Am citit cu succes postarea 1!")


# Testul 2: Verificăm că putem CREA o postare nouă (POST)
def test_creare_postare_noua(playwright):
    api_context = playwright.request.new_context()
    
    # Datele pe care vrem să le trimitem către server (Corpul cererii / Request Body)
    date_noi = {
        "title": "Curs de QA Automation",
        "body": "Invat testare API cu Playwright si Python.",
        "userId": 99
    }
    
    # Trimitem o cerere POST și punem datele în parametrul 'data'
    response = api_context.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=date_noi
    )
    
    # La crearea de date, serverele corecte întorc statusul 201 (Created) în loc de 200
    assert response.status == 201
    
    # Verificăm că serverul a primit datele și ne-a generat un ID nou (de obicei 101)
    date_salvate = response.json()
    assert date_salvate["title"] == "Curs de QA Automation"
    assert "id" in date_salvate
    
    print(f"\n[POST SUCCESS] Postare creata! Serverul a alocat ID-ul: {date_salvate['id']}")