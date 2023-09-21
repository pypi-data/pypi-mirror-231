from trading212.http_request import Client
import pytest
import requests_mock
import re

c = Client('FAKE_API_KEY')
matcher = re.compile(f'{c.BASE_URL}/*')

GET_END_POINTS = dict(
    get_exchanges='/equity/metadata/exchanges',
    get_instruments='/equity/metadata/instruments',
    get_pies='/equity/pies',
    get_orders='/equity/orders/',
    get_account_cash='/equity/account/cash',
    get_account='/equity/account/info',
    get_positions='/equity/positions',
    get_exports='/history/exports'
)

PARAM_END_POINTS = dict(
    get_pie='/equity/pies/42',
    delete_pie='/equity/pies/42',
    get_order='/equity/orders/42',
    delete_order='/equity/orders/42',
    get_position='/equity/orders/42'
)

COMPLEX_ENDPOINTS = dict(
    create_pie=['/equity/pies', [1, 1, 1, 1, 1, 'test']],
    update_pie=['/equity/pies/1', [1, 1, 1, 1, 1, 1, 'test']],
    get_export=['/history/exports', [1, 'FAKE', 1]],
    place_limit_order=['/equity/orders/limit', [1, 'FAKE', 1, 1]],
    place_market_order=['/equity/orders/market', [1, 'FAKE']],
    place_stop_order=['/equity/orders/limit', [1, 'FAKE', 1, 1]],
    place_stop_limit_order=['/equity/orders/limit', [1, 'FAKE', 1, 1, 1]],
    get_order_history=['/equity/history/orders', [1, 'FAKE', 1]],
    get_dividends=['/history/dividends', [1, 'FAKE', 1]],
    get_transactions=['/history/transactions', [1, 'FAKE']],
)

def test_get_exchanges_bad_key():
    client = Client('FAKE')
    with pytest.raises(Exception):
        client.get_exchanges()

def test_get():
    client = Client('FAKE')
    for call_back, url in GET_END_POINTS.items():
        with requests_mock.Mocker() as m:
            m.get(matcher, json={'mock': 'mock'})
            resp = getattr(client, call_back)()
            assert resp['mock'] == 'mock'

def test_get_params():
    client = Client('FAKE')
    for call_back, url in PARAM_END_POINTS.items():
        with requests_mock.Mocker() as mp:
            mp.get(matcher, json={'mock': 'mock'})
            mp.delete(matcher, json={'mock': 'mock'})
            resp = getattr(client, call_back)(42)
            assert resp['mock'] == 'mock'

def test_complex_params():
    client = Client('FAKE')
    for call_back, details in COMPLEX_ENDPOINTS.items():
        with requests_mock.Mocker() as cp:
            cp.post(matcher, json={'mock': 'mock'})
            cp.get(matcher, json={'mock': 'mock'})
            resp = getattr(client, call_back)(*details[1])
            assert resp['mock'] == 'mock'
