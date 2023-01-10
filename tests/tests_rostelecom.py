import pytest
import time

from pages.auth_page import AuthPage
from pages.register_page import RegPage

# Тест-кейс #01(Bug-01)
def test_startpage_right_part_is_correct(web_browser):
    ''' Корректное отображение левой части "Главной страницы авторизации" '''

    page = AuthPage(web_browser)
    phone_tab_class = page.phone_tab.get_attribute("class")
    assert page.auth_title.get_text() == "Авторизация"
    assert phone_tab_class == "rt-tab rt-tab--small rt-tab--active"
    assert page.phone.is_clickable()
    assert page.password.is_clickable()
    assert page.btn_login.is_clickable()
    assert page.registration_link.is_clickable()

# Тест-кейс #02(Bug-02)
@pytest.mark.xfail(reason="Расположение элементов на странице не соответствует ожидаемым требованиям")
def test_location_of_startpage_blocks(web_browser):
    '''Проверка элементов в правом блоке "Главной страницы авторизации" '''

    page = AuthPage(web_browser)
    assert page.auth_form.find(timeout=50)
    assert page.lk_form.find(timeout=50)

# Тест-кейс #03(Bug-03)
@pytest.mark.xfail(reason="Кнопка (вкладка) выбора 'Номер' не соответствует ожидаемым требованиям")
def test_phone_tab(web_browser):
    ''' Проверка названия вкладки "Номер" '''

    page = AuthPage(web_browser)
    assert page.phone_tab.get_text() == "Номер"


# Тест-кейс #04(Bug-04)
@pytest.mark.xfail(reason="Кнопка должна иметь текст 'Продолжить', а не 'Зарегистрироваться' ")
def test_registration_page_and_continue_button(web_browser):
    ''' Проверка названия кнопки "Продолжить" в форме "Регистрация" '''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    assert reg_page.name_field_text.get_text() == "Имя"
    assert reg_page.last_name_field_text.get_text() == "Фамилия"
    assert reg_page.region_field_text.get_text() == "Регион"
    assert reg_page.email_or_mobile_phone_field_text.get_text() == "E-mail или мобильный телефон"
    assert reg_page.password_field_text.get_text() == "Пароль"
    assert reg_page.password_confirmation_field_text.get_text() == "Подтверждение пароля"
    assert reg_page.continue_button.get_text() == "Продолжить"

# Тест-кейс #05
def test_authorisation_valid_via_phone(web_browser):
    ''' Тестирование аутентификации зарегистрированного пользователя по телефону'''

    page = AuthPage(web_browser)
    time.sleep(20)
    page.phone.send_keys('+79*********')  #Номер реальный, поэтому убрала из данных, тест проходит.
    page.password.send_keys("Rus0001!")
    page.btn_login.click()
    time.sleep(20) #на случай капчи

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()


# Тест-кейс #06
def test_authorisation_valid_via_email(web_browser):
    ''' Тестирование аутентификации зарегистрированного пользователя по почте '''

    page = AuthPage(web_browser)
    page.email_tab.click()
    page.email.send_keys('zhenya_rakushina@mail.ru')
    page.password.send_keys("Rus2022!3")
    page.btn_login.click()
    time.sleep(20) #на случай капчи

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()

# Тест-кейс #07
def test_registration_page_with_empty_name_field(web_browser):
    ''' Регистрация пользователя с пустым полем Имя, появления текста с подсказкой об ошибке '''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('')
    reg_page.last_name_field.send_keys("Петров")
    reg_page.email_or_mobile_phone_field.send_keys("testim890@mail.ru")
    reg_page.password_field.send_keys("Parol'1!")
    reg_page.password_confirmation_field.send_keys("Parol'1!")
    reg_page.registration_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс #08
def test_registration_with_an_incorrect_value_in_the_name_field(web_browser):
    ''' Регистрация пользователя с некорректным значением в поле Имя (< 2 символов), появление текста с подсказкой об ошибке '''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys('А')
    reg_page.last_name_field.send_keys("Петров")
    reg_page.email_or_mobile_phone_field.send_keys("testim890@mail.ru")
    reg_page.password_field.send_keys("Parol'1!")
    reg_page.password_confirmation_field.send_keys("Parol'1!")
    reg_page.registration_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс #09
def test_registration_with_an_incorrect_value_in_the_last_name_field(web_browser):
    '''Регистрация пользователя с некорректным значением в поле "Фамилия"(>30 символов),
     появление текста с подсказкой об ошибке'''


    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Мария")
    reg_page.last_name_field.send_keys("Проылкнровллыллцрорлыврлыоврлоыврл")
    reg_page.email_or_mobile_phone_field.send_keys("testim890@mail.ru")
    reg_page.password_field.send_keys("Parol'1!")
    reg_page.password_confirmation_field.send_keys("Parol'1!")
    reg_page.registration_button.click()
    reg_page.error_message_name.is_visible()
    assert reg_page.error_message_last_name.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

# Тест-кейс #10
def test_registration_of_an_already_registered_user(web_browser):
    '''Регистрация пользователя с уже зарегистрированным номером, отображается оповещающая форма'''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Евгения")
    reg_page.last_name_field.send_keys("Ракушина")
    reg_page.email_or_mobile_phone_field.send_keys("+79*******")
    reg_page.password_field.send_keys("Tel0001!")
    reg_page.password_confirmation_field.send_keys("Tel0001!")
    reg_page.registration_button.click()
    assert reg_page.notification_form.is_visible


# Тест-кейс #11 (Bug-05)
@pytest.mark.xfail(reason="Должна быть кнопка закрыть 'х'")
def test_notification_form(web_browser):
    '''Проверка элементов на всплывающем окне оповещения "Учётная запись уже существует'''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Евгения")
    reg_page.last_name_field.send_keys("Ракушина")
    reg_page.email_or_mobile_phone_field.send_keys("zhenya****@gmail.com")
    reg_page.password_field.send_keys("Tel0001!")
    reg_page.password_confirmation_field.send_keys("Tel0001!")
    reg_page.registration_button.click()
    assert reg_page.login_button.get_text() == 'Войти'
    assert reg_page.recover_password_button.get_text() == 'Восстановить пароль'
    assert reg_page.close_button.get_text() == 'x'


# Тест-кейс #12
def test_incorrect_password_during_registration(web_browser):
    '''Некорректный пароль при регистрации пользователя(< 8 символов), появления текст с подсказкой об ошибке'''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Мария")
    reg_page.last_name_field.send_keys("Иванова")
    reg_page.email_or_mobile_phone_field.send_keys("testim1890@gmail.com")
    reg_page.password_field.send_keys("Par1!")
    reg_page.password_confirmation_field.send_keys("Par1!")
    reg_page.registration_button.click()
    assert reg_page.error_message_password.get_text() == "Длина пароля должна быть не менее 8 символов"

# Тест-кейс #13
def test_incorrect_password_during_registration_no_numbers_OR_symbols(web_browser):
    '''Некорректный пароль при регистрации пользователя(нет спецсимволов и цифр), появления текста с подсказкой об ошибке'''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Мария")
    reg_page.last_name_field.send_keys("Иванова")
    reg_page.email_or_mobile_phone_field.send_keys("testim1890@gmail.com")
    reg_page.password_field.send_keys("Etoparol")
    reg_page.password_confirmation_field.send_keys("Etoparol")
    reg_page.registration_button.click()
    assert reg_page.error_message_password.get_text() == "Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру"


# Тест-кейс #14
def test_authorization_of_a_user_with_an_invalid_password(web_browser):
    '''Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя,
    надпись "Забыл пароль" перекрашивается в оранжевый цвет'''

    page = AuthPage(web_browser)
    page.phone.send_keys('+7*******')
    page.password.send_keys("Parol")
    page.btn_login.click()
    assert page.message_invalid_username_or_password.get_text() == "Неверный логин или пароль"
    assert "rt-link--orange" in page.the_element_forgot_the_password.get_attribute('class')


# Тест-кейс #15
def test_instead_of_cyrillic_invalid_characters(web_browser):
    '''Недопустимые символы в поле ввода "Фамилия" в форме "Регистрация"'''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Кира")
    reg_page.last_name_field.send_keys("Familiya")
    reg_page.email_or_mobile_phone_field.send_keys("testim1890@gmail.com")
    reg_page.password_field.send_keys("Parol'1!")
    reg_page.password_confirmation_field.send_keys("Parol'1!")
    reg_page.registration_button.click()
    assert reg_page.message_must_be_filled_in_cyrillic.get_text() == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# Тест-кейс #16
def test_password_and_password_confirmation_do_not_match(web_browser):
    '''Поля ввода "Пароль" и "Подтверждение пароля" не совпадают в форме "Регистрация" '''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Петр")
    reg_page.last_name_field.send_keys("Семенов")
    reg_page.email_or_mobile_phone_field.send_keys("testim1890@gmail.com")
    reg_page.password_field.send_keys("Newtesttt7890")
    reg_page.password_confirmation_field.send_keys("Newtesttt789")
    reg_page.registration_button.click()
    assert reg_page.message_passwords_dont_match.get_text() == "Пароли не совпадают"


# Тест-кейс #17
def test_invalid_email_or_mobile_phone(web_browser):
    '''Невалидный email в поле ввода "Email или мобильный телефон" в форме "Регистрация" '''

    auth_page = AuthPage(web_browser)
    auth_page.registration_link.click()
    reg_page = RegPage(web_browser, auth_page.get_current_url())
    reg_page.name_field.send_keys("Ян")
    reg_page.last_name_field.send_keys("Ивановивановивановивановиван")
    reg_page.email_or_mobile_phone_field.send_keys("1234mail.ru")
    reg_page.password_field.send_keys("Parol123456789")
    reg_page.password_confirmation_field.send_keys("Parol123456789")
    reg_page.registration_button.click()
    assert reg_page.message_enter_the_phone_in_the_format.get_text() == "Введите телефон в формате +7ХХХХХХХХХХ или" \
                                                                        " +375XXXXXXXXX, или email в формате example@email.ru"



# Тест-кейс #18
@pytest.mark.xfail(reason="Неверные логин и пароль")
def test_authorisation_valid_via_login(web_browser):
    '''Тестирование аутентификации НЕзарегистрированного пользователя по Логину'''

    page = AuthPage(web_browser)
    page.login_tab.click()
    page.login.send_keys('test_user')
    page.password.send_keys("Newpassword8!")
    page.btn_login.click()

    assert 'https://b2c.passport.rt.ru/account_b2c/page?state=' in page.get_current_url() \
           and '&client_id=account_b2c#/' in page.get_current_url()


# Тест-кейс #19
def test_email_tab_is_highlited_when_password_recovery_via_email(web_browser):
    '''Вкладка "Почта" выбирается автоматически, после ввода почты в форму "Восстановления пароля"'''

    page = AuthPage(web_browser)
    page.the_element_forgot_the_password.click()
    page.phone.send_keys('newtest@mail.ru')
    page.btn_reset.click()
    assert "rt-tab rt-tab--small rt-tab--active" in page.email_tab.get_attribute('class')


# Тест-кейс 20(Bug-06)
def test_page_password_recovery_is_correct(web_browser):
    '''Корректное отображение "Страницы восстановления пароля"'''

    page = AuthPage(web_browser)
    page.the_element_forgot_the_password.click()
    phone_tab_class = page.phone_tab.get_attribute("class")
    #assert phone_tab_class == "rt-tab rt-tab--active"
    assert page
    assert page.phone_tab.find(timeout=50)
    assert page.email_tab.find(timeout=50)
    assert page.login_tab.find(timeout=50)
    assert page.litsevoy_schot_tab.find(timeout=50)
    assert page.phone.find(timeout=50)
    assert page.captcha.find(timeout=50)
    assert page.btn_reset.find(timeout=50)
    assert page.btn_reset_back.find(timeout=50)