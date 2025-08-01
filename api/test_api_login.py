import pytest
import requests
import allure


@allure.title('Тест успешного логина')

@allure.description('Проверка успешного логина через API')

def test_login_api():
    url = 'https://parterra.ru/utils/'
    payload = {
        'auth[email]':'rufus2116@gmail.com',
        'auth[password]':'Lielvarde143',
        'action':'auth',
        'type':'header'
    }
    headers = {
        'content-type':'text/html; charset=UTF-8',
        'accept':'application/json, text/javascript, */*; q=0.01'
    }
    session = requests.Session()

    with allure.step('Делаем запрос'):
        response = session.post(url,headers=headers,data=payload)

    with allure.step('Проверяем статус код'):
        assert response.status_code == 200

    with allure.step('Получаем PHPSESSID'):
        phpsessid = session.cookies.get('PHPSESSID')
        print("PHPSESSID:", phpsessid)
