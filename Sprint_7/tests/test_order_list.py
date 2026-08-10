import allure
import requests

from urls import ORDERS_URL


@allure.feature("Orders")
@allure.story("Order list")
class TestOrderList:
    @allure.title("Orders list is returned in response body")
    def test_orders_list_is_returned(self):
        response = requests.get(
            ORDERS_URL,
            params={"limit": 1, "page": 0},
            timeout=30,
        )
        body = response.json()

        assert response.status_code == 200
        assert "orders" in body
        assert isinstance(body["orders"], list)
