# Sprint_7

API tests for the Yandex Scooter training service.

## Covered API

- create courier;
- login courier;
- create order;
- get orders list;
- delete courier;
- accept order;
- get order by track number.

## Install

```bash
pip install -r requirements.txt
```

## Run tests

```bash
pytest -v
```

## Allure

```bash
pytest tests --alluredir=allure_results
```
