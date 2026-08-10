import allure

from data import (
    COURIER_ID_NOT_FOUND_MESSAGE,
    ORDER_ID_NOT_FOUND_MESSAGE,
    ORDER_SEARCH_MISSING_DATA_MESSAGE,
    ROUTE_NOT_FOUND_MESSAGE,
)
from helpers import accept_order, get_order_id_by_track


@allure.feature("Orders")
@allure.story("Accept order")
class TestAcceptOrder:
    @allure.title("Order can be accepted by courier")
    def test_order_can_be_accepted(self, order_factory, courier_id):
        order_response = order_factory(["BLACK"])
        order_id = get_order_id_by_track(order_response.json()["track"])

        response = accept_order(order_id, courier_id)

        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Accept order without courier id returns an error")
    def test_accept_order_without_courier_id_returns_error(self, order_factory):
        order_response = order_factory(["GREY"])
        order_id = get_order_id_by_track(order_response.json()["track"])

        response = accept_order(order_id)

        assert response.status_code == 400
        assert response.json()["message"] == ORDER_SEARCH_MISSING_DATA_MESSAGE

    @allure.title("Accept order with wrong courier id returns an error")
    def test_accept_order_with_wrong_courier_id_returns_error(self, order_factory):
        order_response = order_factory(["BLACK"])
        order_id = get_order_id_by_track(order_response.json()["track"])

        response = accept_order(order_id, 0)

        assert response.status_code == 404
        assert response.json()["message"] == COURIER_ID_NOT_FOUND_MESSAGE

    @allure.title("Accept order without order id returns an error")
    def test_accept_order_without_order_id_returns_error(self, courier_id):
        response = accept_order(courier_id=courier_id)

        assert response.status_code == 404
        assert response.json()["message"] == ROUTE_NOT_FOUND_MESSAGE

    @allure.title("Accept order with wrong order id returns an error")
    def test_accept_order_with_wrong_order_id_returns_error(self, courier_id):
        response = accept_order(0, courier_id)

        assert response.status_code == 404
        assert response.json()["message"] == ORDER_ID_NOT_FOUND_MESSAGE
