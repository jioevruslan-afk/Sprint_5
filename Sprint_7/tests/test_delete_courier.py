import allure
import requests

from data import DELETE_COURIER_NOT_FOUND_MESSAGE, ROUTE_NOT_FOUND_MESSAGE
from helpers import delete_courier, get_courier_id
from urls import COURIER_URL


@allure.feature("Courier")
@allure.story("Delete courier")
class TestDeleteCourier:
    @allure.title("Courier can be deleted")
    def test_courier_can_be_deleted(self, courier):
        courier_id = get_courier_id(courier)
        response = delete_courier(courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Delete courier without id returns an error")
    def test_delete_courier_without_id_returns_error(self):
        response = requests.delete(COURIER_URL, timeout=15)

        assert response.status_code == 404
        assert response.json()["message"] == ROUTE_NOT_FOUND_MESSAGE

    @allure.title("Delete courier with nonexistent id returns an error")
    def test_delete_courier_with_nonexistent_id_returns_error(self):
        response = delete_courier(0)

        assert response.status_code == 404
        assert response.json()["message"] == DELETE_COURIER_NOT_FOUND_MESSAGE
