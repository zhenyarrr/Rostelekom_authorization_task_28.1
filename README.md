Note: telephone number and email address of a real registered person were hidden 
in the positive test cases as it is confidential  // Телефон и эл. почты реального пользователя 
были скрыты в позитивных кейсах, т.к. это конфиденциальная информация.

Files
-----

[conftest.py](conftest.py) - contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[pages/base.py](pages/base.py) contains PageObject pattern implementation for Python.

[pages/auth_page.py](pages/auth_page.py) authorization page for working with autotests.

[pages/register_page.py](pages/register_page.py) registration page for working with autotests.

[pages/elements.py](pages/elements.py) contains helper class to define web elements on web pages.

[tests/tests_rostelecom.py](tests/tests_rostelecom.py) contains Web UI tests for Rostelecom (https://b2c.passport.rt.ru/)


Autotests description
-----
**test_startpage_right_part_is_correct**
Тест-кейс #01 - Корректное отображение левой части "Главной страницы авторизации"
Тест не проходит(Bug-01). Причина - расположение элементов на странице не соответствует ожидаемым требованиям.


**test_location_of_startpage_blocks**
Тест-кейс #02 - Проверка элементов в правом блоке "Главной страницы авторизации"
Тест не проходит(Bug-02). Причина - расположение элементов на странице не соответствует ожидаемым требованиям.


**test_phone_tab**
Тест-кейс #03 - Проверка названия вкладки "Номер"
Тест не проходит(Bug-03). Причина - Кнопка должна иметь текст 'Номер', а не 'Телефон', 
согласно требованиям.



**test_registration_page_and_continue_button**
Тест-кейс #04 - Проверка названия кнопки "Продолжить" в форме "Регистрация"
Тест не проходит(Bugs-04). Причина - Кнопка должна иметь текст 'Продолжить', а не 'Зарегистрироваться'


**test_authorisation_valid_via_phone**
Тест-кейс #05 - Тестирование аутентификации зарегистрированного пользователя по телефону.


**test_authorisation_valid_via_email**
Тест-кейс #06 - Тестирование аутентификации зарегистрированного пользователя по почте.


**test_registration_page_with_empty_name_field**
Тест-кейс #07 - Регистрация пользователя с пустым полем Имя, появления текста с подсказкой об ошибке.


**test_registration_with_an_incorrect_value_in_the_name_field**
Тест-кейс #08 - Регистрация пользователя с некорректным значением в поле Имя (< 2 символов),
появление текста с подсказкой об ошибке.


***test_registration_with_an_incorrect_value_in_the_last_name_field*
Тест-кейс #09 - Регистрация пользователя с некорректным значением в поле "Фамилия"(>30 символов),
появление текста с подсказкой об ошибке.


**test_registration_of_an_already_registered_user**
Тест-кейс #10 - Регистрация пользователя с уже зарегистрированным номером, 
отображается оповещающая форма.


**test_notification_form**
Тест-кейс #11 - Проверка элементов на всплывающем окне оповещения "Учётная запись уже существует"
Тест не проходит (Bug-05). Причина - Должна быть кнопка закрыть 'х'


**test_incorrect_password_during_registration**
Тест-кейс #12 - Некорректный пароль при регистрации пользователя(< 8 символов),
появления текст с подсказкой об ошибке



**test_incorrect_password_during_registration_no_numbers_OR_symbols**
Тест-кейс #13  - Некорректный пароль при регистрации пользователя(нет спецсимволов и цифр),
появления текста с подсказкой об ошибке



**test_authorization_of_a_user_with_an_invalid_password**
Тест-кейс #14 - Вход по неправильному паролю в форме "Авторизация" уже зарегистрированного пользователя,
надпись "Забыл пароль" перекрашивается в оранжевый цвет


**test_instead_of_cyrillic_invalid_characters**
Тест-кейс #15 - Недопустимые символы в поле ввода "Фамилия" в форме "Регистрация"


**test_password_and_password_confirmation_do_not_match**
Тест-кейс #16 - Поля ввода "Пароль" и "Подтверждение пароля" не совпадают в форме "Регистрация"


**test_invalid_email_or_mobile_phone**
Тест-кейс #17 - Невалидный email в поле ввода "Email или мобильный телефон" в форме "Регистрация"


**test_authorisation_valid_via_login**
Тест-кейс #18 - Тестирование аутентификации НЕзарегистрированного пользователя по Логину


**test_email_tab_is_highlited_when_password_recovery_via_email**
Тест-кейс #19 - Вкладка "Почта" выбирается автоматически, после ввода почты в форму "Восстановления пароля"


**test_page_password_recovery_is_correct**
Тест-кейс #20 - Корректное отображение "Страницы восстановления пароля"


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip install -r requirements.txt
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

    ```bash
    pytest -v --driver Chrome --driver-path ~/chrome tests/tests_rostelecom.py
    ```

Note:
~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.