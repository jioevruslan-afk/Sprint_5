import allure

from data import ORDER_NOT_FOUND_MESSAGE, ORDER_SEARCH_MISSING_DATA_MESSAGE
from helpers import get_order_by_track


@allure.feature("Orders")
@allure.story("Get order by track")
class TestGetOrderByTrack:
    @allure.title("Order can be received by track number")
    def test_order_can_be_received_by_track_number(self, order_factory):
        created_order = order_factory(["BLACK", "GREY"])
        track = created_order.json()["track"]

        response = get_order_by_track(track)
        body = response.json()

        assert response.status_code == 200
        assert "order" in body
        assert body["order"]["track"] == track

    @allure.title("Get order without track number returns an error")
    def test_get_order_without_track_returns_error(self):
        response = get_order_by_track()

        assert response.status_code == 400
        assert response.json()["message"] == ORDER_SEARCH_MISSING_DATA_MESSAGE

    @allure.title("Get order with nonexistent track number returns an error")
    def test_get_order_with_nonexistent_track_returns_error(self):
        response = get_order_by_track(0)

        assert response.status_code == 404
        assert response.json()["message"] == ORDER_NOT_FOUND_MESSAGE
