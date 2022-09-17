import pytest
from extensions import apiActions
from utilities.cvUtil import readData
from utilities import customLogger, readProperties

url = readProperties.get_api_data("baseUrl")
path = "./TestData/users.csv"
customLogger.loggen()


def test01_getRequest():
    response = apiActions.get(url)
    assert apiActions.get_status_code(response) == 200


def test02_postRequest():
    request_json = apiActions.parseToJson("./TestData/post_payload.json")
    response = apiActions.post(url, request_json)
    id_res = apiActions.get_values_from_json("id", response)
    print(id_res[0])
    assert apiActions.get_value_from_json("name", response) == "morpheus"
    assert apiActions.get_status_code(response) == 201


def test03_delete():
    response = apiActions.delete(url)
    assert apiActions.get_status_code(response) == 204


def test04_put():
    request_json = apiActions.parseToJson("./TestData/update_payload.json")
    response = apiActions.put(url, request_json)
    assert apiActions.get_value_from_json("job", response) == "zion resident"
    assert apiActions.get_status_code(response) == 200


@pytest.mark.parametrize("name,job", readData(path))
def test05_put(name, job):
    request_json = apiActions.parseToJson("./TestData/update_payload.json")
    request_json["name"] = name
    request_json["job"] = job
    response = apiActions.put(url, request_json)
    assert apiActions.get_value_from_json("name", response) == name
    assert apiActions.get_value_from_json("job", response) == job
    assert apiActions.get_status_code(response) == 200
