import pytest
from extensions import api_actions as api
from utilities.cv_util import read_data
from utilities import custom_logger, read_properties

url = read_properties.get_api_data("baseUrl")
path = "./TestData/users.csv"
custom_logger.loggen()


def test01_get_request():
    response = api.get(url)
    assert api.get_status_code(response) == 200


def test02_post_request():
    request_json = api.parseToJson("./TestData/post_payload.json")
    response = api.post(url, request_json)
    id_res = api.get_values_from_json("id", response)
    print(id_res[0])
    assert api.get_value_from_json("name", response) == "morpheus"
    assert api.get_status_code(response) == 201


def test03_delete():
    response = api.delete(url)
    assert api.get_status_code(response) == 204


def test04_put():
    request_json = api.parseToJson("./TestData/update_payload.json")
    response = api.put(url, request_json)
    assert api.get_value_from_json("job", response) == "zion resident"
    assert api.get_status_code(response) == 200


@pytest.mark.parametrize("name,job", read_data(path))
def test05_put(name, job):
    request_json = api.parseToJson("./TestData/update_payload.json")
    request_json["name"] = name
    request_json["job"] = job
    response = api.put(url, request_json)
    assert api.get_value_from_json("name", response) == name
    assert api.get_value_from_json("job", response) == job
    assert api.get_status_code(response) == 200
