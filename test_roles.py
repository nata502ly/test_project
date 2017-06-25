import pytest
from pulse_api_roles import PulseRestApi
from models_roles import Role

@pytest.fixture()
def app():
    return PulseRestApi()
def test_test_create(app):
    role = Role(name = "Master", type = "novel", level = "2", book = "Master and Margarite")
    response = app.create_object(role)

    assert response.status_code == 201
    role.id = response.json()["id"]
    assert response.json() == role.get_dict()
    assert app.get_object(role).json() == role.get_dict()