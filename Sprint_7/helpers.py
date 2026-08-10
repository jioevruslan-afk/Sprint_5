from uuid import uuid4

import allure
import requests

from data import get_order_payload
from urls import (
    ACCEPT_ORDER_URL,
    CANCEL_ORDER_URL,
    COURIER_LOGIN_URL,
    COURIER_URL,
    ORDER_BY_TRACK_URL,
    ORDERS_URL,
)

REQUEST_TIMEOUT = 15


def generate_courier_data():
    suffix = uuid4().hex[:10]
    return {
        "login": f"courier_{suffix}",
        "password": f"pass_{suffix}",
        "firstName": f"Test_{suffix}",
    }


@allure.step("Create courier")
def create_courier(payload=None):
    courier_payload = payload or generate_courier_data()
    response = requests.post(COURIER_URL, json=courier_payload, timeout=REQUEST_TIMEOUT)
    return response, courier_payload


@allure.step("Log in courier")
def login_courier(payload):
    credentials = {
        "login": payload.get("login"),
        "password": payload.get("password"),
    }
    return requests.post(COURIER_LOGIN_URL, json=credentials, timeout=REQUEST_TIMEOUT)


@allure.step("Get courier id")
def get_courier_id(payload):
    response = login_courier(payload)
    if response.status_code != 200:
        return None
    return response.json().get("id")


@allure.step("Delete courier by id")
def delete_courier(courier_id):
    if courier_id is None:
        return None
    return requests.delete(f"{COURIER_URL}/{courier_id}", timeout=REQUEST_TIMEOUT)


@allure.step("Delete courier by credentials")
def delete_courier_by_credentials(payload):
    courier_id = get_courier_id(payload)
    return delete_courier(courier_id)


@allure.step("Create order")
def create_order(color=None):
    return requests.post(
        ORDERS_URL,
        json=get_order_payload(color),
        timeout=REQUEST_TIMEOUT,
    )


@allure.step("Cancel order")
def cancel_order(track):
    if track is None:
        return None
    return requests.put(
        CANCEL_ORDER_URL,
        params={"track": track},
        timeout=REQUEST_TIMEOUT,
    )


@allure.step("Get order by track")
def get_order_by_track(track=None):
    params = {} if track is None else {"t": track}
    return requests.get(ORDER_BY_TRACK_URL, params=params, timeout=REQUEST_TIMEOUT)


@allure.step("Get order id by track")
def get_order_id_by_track(track):
    response = get_order_by_track(track)
    if response.status_code != 200:
        return None
    return response.json().get("order", {}).get("id")


@allure.step("Accept order")
def accept_order(order_id=None, courier_id=None):
    url = ACCEPT_ORDER_URL if order_id is None else f"{ACCEPT_ORDER_URL}/{order_id}"
    params = {} if courier_id is None else {"courierId": courier_id}
    return requests.put(url, params=params, timeout=REQUEST_TIMEOUT)
