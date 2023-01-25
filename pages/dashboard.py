from pages.base_page import BasePage


class Dashboard(BasePage):
    button_add_player_xpath = "//a[@href='/en/players/add']//child::button"
    page_title_xpath = "//h6[contains(text(),'Scouts')]"
    text_main_page_xpath = "// *[contains(text(), 'Main page')]"
    title_last_created_player_xpath = "//*[contains(text(), 'Activity')]//following-sibling::h6[1]"
    activity_block_wrapper_xpath = "//*[contains(text(), 'Activity')]//parent::div"
    players_count_block_wrapper_xpath = "//*[contains(text(), 'Players count')]//parent::div"
    players_count_xpath = "// *[contains(text(), 'Players count')] // following::b[1]"
    dev_team_contact_link_xpath = "//a[contains(@href, 'T3X4CAKNU')]"
    main_logo_xpath = "//*[@title='Logo Scouts Panel']"
    sign_out_button_xpath = "//*[text()='Sign out']//ancestor::div[@role='button']"
    john_snow_link_xpath = "//*[contains(@href, '63d05870071e730cb08ff867')]"
    a_a_button_xpath = "//*[contains(@href, '63d04c79071e730cb08ff81a')]/button"
    rrr_eee_button_title_xpath = "//span[starts-with(text(), 'rrr')]"



