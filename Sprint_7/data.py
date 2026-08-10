from copy import deepcopy


CREATE_COURIER_MISSING_FIELD_MESSAGE = "Недостаточно данных для создания учетной записи"
DUPLICATE_COURIER_MESSAGE = "Этот логин уже используется. Попробуйте другой."
LOGIN_MISSING_FIELD_MESSAGE = "Недостаточно данных для входа"
COURIER_NOT_FOUND_MESSAGE = "Учетная запись не найдена"
DELETE_COURIER_MISSING_ID_MESSAGE = "Недостаточно данных для удаления курьера"
DELETE_COURIER_NOT_FOUND_MESSAGE = "Курьера с таким id нет."
ROUTE_NOT_FOUND_MESSAGE = "Not Found."
ORDER_SEARCH_MISSING_DATA_MESSAGE = "Недостаточно данных для поиска"
ORDER_NOT_FOUND_MESSAGE = "Заказ не найден"
ORDER_ID_NOT_FOUND_MESSAGE = "Заказа с таким id не существует"
COURIER_ID_NOT_FOUND_MESSAGE = "Курьера с таким id не существует"

ORDER_PAYLOAD = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2026-08-11",
    "comment": "Saske, come back to Konoha",
}


def get_order_payload(color=None):
    payload = deepcopy(ORDER_PAYLOAD)
    if color is not None:
        payload["color"] = color
    return payload
