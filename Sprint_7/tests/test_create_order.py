import allure
import pytest


@allure.feature("Orders")
@allure.story("Create order")
class TestCreateOrder:
    @allure.title("Order can be created with color: {color}")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"],
            None,
        ],
    )
    def test_order_can_be_created_with_different_color_options(self, order_factory, color):
        response = order_factory(color)
        body = response.json()

        assert response.status_code == 201
        assert "track" in body
        assert isinstance(body["track"], int)
