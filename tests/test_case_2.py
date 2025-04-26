import time
from pages.main_page import MainPage
from pages.best_sellers_page import BestSellersPage
from pages.game_page import GamePage
def test_case_2(browser):


    main_page = MainPage(browser)
    main_page.open()

    assert "Steam" in browser.title

    main_page.hover_and_wait_for_popup()

    main_page.click_best_sellers()

    top_sellers_page = BestSellersPage(browser)
    
    assert "Steam Charts" in browser.title

    top_sellers_page.click_more_top_sellers()

    assert "Steam Search" in browser.title

    control_count, results_count = top_sellers_page.select_filters()

    assert top_sellers_page.is_linux_checkbox_selected()
    assert top_sellers_page.is_lan_coop_checkbox_selected()
    assert top_sellers_page.is_action_checkbox_selected()
    

    assert control_count ==  results_count 
   

    first_game_title, first_game_price, first_game_release_date = top_sellers_page.get_first_game_info()

    top_sellers_page.open_first_game()

    assert first_game_title in browser.title
    game_page = GamePage(browser)

    game_title = game_page.get_game_title()
    game_price = game_page.get_game_price()
    game_release_date = game_page.get_game_release_date()
    
    assert first_game_title == game_title
    assert first_game_price == game_price
    assert first_game_release_date in game_release_date