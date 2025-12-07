# Павел Колыванов, 38-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request

def test_track():
    response = sender_stand_request.get_order_by_track(sender_stand_request.track_order)

    assert response.status_code == 200