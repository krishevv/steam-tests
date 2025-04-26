from pages.main_page import MainPage
from pages.about_page import AboutPage

def test_case_1(browser):
    main_page = MainPage(browser)
    

    main_page.click_about()
    about_page = AboutPage(browser)

    assert "Ultimate" in browser.title

    current_players = about_page.get_current_players()
    peak_players = about_page.get_peak_players()
    
    assert current_players < peak_players, "Число игроков сейчас не меньше, чем онлайн"

    about_page.click_store()

    assert "Welcome" in browser.title