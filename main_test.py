import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json = body,
                         headers = data.headers)

track_order = post_new_order(data.order_body).json()["track"]

def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_BY_TRACK_PATH + str(track),
                        headers = data.headers)

def test_track():
    response = get_order_by_track(track_order)

    assert response.status_code == 200