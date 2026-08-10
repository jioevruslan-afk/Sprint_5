import allure
import pytest
import requests

from data import COURIER_NOT_FOUND_MESSAGE, LOGIN_MISSING_FIELD_MESSAGE
from helpers import generate_courier_data, login_courier
from urls import COURIER_LOGIN_URL


@allure.feature("Courier")
@allure.story("Login courier")
class TestLoginCourier:
    @allure.title("Existing courier can log in")
    def test_courier_can_login(self, courier):
        response = login_courier(courier)
        body = response.json()

        assert response.status_code == 200
        assert "id" in body
        assert isinstance(body["id"], int)

    @allure.title("Courier cannot log in without required field: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login"])
    def test_cannot_login_without_required_field(self, courier, missing_field):
        payload = {
            "login": courier["login"],
            "password": courier["password"],
        }
        payload.pop(missing_field)

        response = requests.post(COURIER_LOGIN_URL, json=payload, timeout=15)

        assert response.status_code == 400
        assert response.json()["message"] == LOGIN_MISSING_FIELD_MESSAGE

    @allure.title("Courier cannot log in with wrong credentials")
    @pytest.mark.parametrize(
        "field, value",
        [
            ("login", "wrong_login"),
            ("password", "wrong_password"),
        ],
    )
    def test_cannot_login_with_wrong_credentials(self, courier, field, value):
        payload = {
            "login": courier["login"],
            "password": courier["password"],
        }
        payload[field] = value

        response = requests.post(COURIER_LOGIN_URL, json=payload, timeout=15)

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND_MESSAGE

    @allure.title("Nonexistent courier cannot log in")
    def test_nonexistent_courier_cannot_login(self):
        response = login_courier(generate_courier_data())

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_NOT_FOUND_MESSAGE
