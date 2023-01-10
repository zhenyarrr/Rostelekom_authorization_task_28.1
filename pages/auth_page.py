from pages.base import WebPage
from pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = 'https://b2c.passport.rt.ru'

        super().__init__(web_driver, url)

    phone_tab = WebElement(xpath='//*[@id="t-btn-tab-phone"]')
    phone = WebElement(xpath='//*[@id="username"]')
    email_tab = WebElement(xpath='//*[@id="t-btn-tab-mail"]')
    email = WebElement(xpath='//*[@id="username"]')
    login_tab = WebElement(xpath='//*[@id="t-btn-tab-login"]')
    login = WebElement(xpath='//*[@id="username"]')
    litsevoy_schot_tab = WebElement(xpath='//*[@id="t-btn-tab-ls"]')

    password = WebElement(id='password')
    authentication_tabs = WebElement(xpath='//*[@id="page-right"]/div/div/div/form/div[1]/div[1]')

    btn_login = WebElement(xpath='//*[@id="kc-login"]')
    auth_title = WebElement(xpath='//*[@id="page-right"]/div/div/h1')
    registration_link = WebElement(xpath='//*[@id="kc-register"]')
    phone_tab = WebElement(id='t-btn-tab-phone')
    logo_lk = WebElement(xpath='//*[@id="page-left"]/div/div[1]/svg/path[2]')

    # тут ниже у двух одинаковые xpath
    auth_form = WebElement(xpath='//*[@id="page-right"]/div/div')
    lk_form = WebElement(xpath='//*[@id="page-left"]/div')
    message_invalid_username_or_password = WebElement(xpath='//*[@id="form-error-message"]')
    the_element_forgot_the_password = WebElement(xpath='//*[@id="forgot_password"]')
    btn_reset = WebElement(id='reset')
    btn_reset_back = WebElement(id='reset-back')



    #password_recovery form
    captcha = WebElement(xpath='//*[@id="captcha"]')

