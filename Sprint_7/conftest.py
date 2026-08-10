import pytest

from helpers import (
    cancel_order,
    create_courier,
    create_order,
    delete_courier_by_credentials,
    generate_courier_data,
    get_courier_id,
)


@pytest.fixture
def courier():
    payload = generate_courier_data()
    response, payload = create_courier(payload)
    assert response.status_code == 201
    yield payload
    delete_courier_by_credentials(payload)


@pytest.fixture
def courier_id(courier):
    courier_id = get_courier_id(courier)
    assert courier_id is not None
    return courier_id


@pytest.fixture
def order_factory():
    tracks = []

    def _create_order(color=None):
        response = create_order(color)
        if response.status_code == 201:
            tracks.append(response.json().get("track"))
        return response

    yield _create_order

    for track in tracks:
        cancel_order(track)
