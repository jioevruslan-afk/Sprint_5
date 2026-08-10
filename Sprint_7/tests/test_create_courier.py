import allure
import pytest
import requests

from data import (
    CREATE_COURIER_MISSING_FIELD_MESSAGE,
    DUPLICATE_COURIER_MESSAGE,
)
from helpers import create_courier, delete_courier_by_credentials, generate_courier_data
from urls import COURIER_URL


@allure.feature("Courier")
@allure.story("Create courier")
class TestCreateCourier:
    @allure.title("Courier can be created with valid required fields")
    def test_courier_can_be_created(self):
        response, payload = create_courier()

        try:
            assert response.status_code == 201
            assert response.json() == {"ok": True}
        finally:
            delete_courier_by_credentials(payload)

    @allure.title("Two couriers with the same login cannot be created")
    def test_cannot_create_two_same_couriers(self):
        payload = generate_courier_data()
        first_response, _ = create_courier(payload)
        second_response, _ = create_courier(payload)

        try:
            assert first_response.status_code == 201
            assert second_response.status_code == 409
            assert second_response.json()["message"] == DUPLICATE_COURIER_MESSAGE
        finally:
            delete_courier_by_credentials(payload)

    @allure.title("Courier cannot be created without required field: {missing_field}")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_cannot_create_courier_without_required_field(self, missing_field):
        payload = generate_courier_data()
        payload.pop(missing_field)

        response = requests.post(COURIER_URL, json=payload, timeout=15)

        assert response.status_code == 400
        assert response.json()["message"] == CREATE_COURIER_MISSING_FIELD_MESSAGE

    @allure.title("Courier can be created without optional firstName")
    def test_courier_can_be_created_without_first_name(self):
        payload = generate_courier_data()
        payload.pop("firstName")

        response, _ = create_courier(payload)

        try:
            assert response.status_code == 201
            assert response.json() == {"ok": True}
        finally:
            delete_courier_by_credentials(payload)
