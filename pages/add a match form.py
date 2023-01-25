from pages.base_page import BasePage


class ADD_A_MATCH_FORM(BasePage):
    button_add_lang_title_xpath = "//*[@type = 'button']/span[text()='Add language']"
    button_youtube_title_xpath = "// span[contains(text(), 'Youtube')]"
    button_clear_title_xpath = "// span[text() = 'Clear']"
    button_clear_xpath = "//span[text()='Clear']//parent::button"
    email_label_xpath = "//*[@name='email']//preceding::label"
    email_field_xpath = "//*[@name='email']"
    name_field_xpath = "//*[@type='text' and @name='name']"
    surname_field_xpath = "//*[@name='surname']"
    phone_field_xpath = "//*[@name='phone']"
    weight_field_xpath = "//*[@type='number' and @name='weight']"
    height_field_xpath = "//*[@name='height']"
    date_field_xpath = "//*[@type='date']"
    leg_field_xpath = "//*[@id='leg']"
    club_field_xpath = "//*[@name='club']"
    level_field_xpath = "//*[@name='level']"
    main_position_field_xpath = "//*[@name='mainPosition' and 'required']"
    second_position_field_xpath = "//*[@name='secondPosition']"
    district_field_xpath = "//*[@id='mui-component-select-district']"
    socials_button_xpath = "//*[@name='webLaczy']"
    web90_button_xpath = "//*[@name='web90']"
    facebook_button_xpath = "//*[@name='webFB']"

