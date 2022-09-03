import pytest
from extensions import ApiActions
from utilities.CVUtil import readData
from utilities import customLogger, readProperties

url = readProperties.get_api_data("baseUrl")
path = "./TestData/users.csv"
customLogger.loggen()


def test01_getRequest():
    response = ApiActions.get(url)
    assert ApiActions.get_status_code(response) == 200


def test02_postRequest():
    request_json = ApiActions.parseToJson("./TestData/post_payload.json")
    response = ApiActions.post(url, request_json)
    id_res = ApiActions.get_values_from_json("id", response)
    print(id_res[0])
    assert ApiActions.get_value_from_json("name", response) == "morpheus"
    assert ApiActions.get_status_code(response) == 201


def test03_delete():
    response = ApiActions.delete(url)
    assert ApiActions.get_status_code(response) == 204


def test04_put():
    request_json = ApiActions.parseToJson("./TestData/update_payload.json")
    response = ApiActions.put(url, request_json)
    assert ApiActions.get_value_from_json("job", response) == "zion resident"
    assert ApiActions.get_status_code(response) == 200


@pytest.mark.parametrize("name,job", readData(path))
def test05_put(name, job):
    request_json = ApiActions.parseToJson("./TestData/update_payload.json")
    request_json["name"] = name
    request_json["job"] = job
    response = ApiActions.put(url, request_json)
    assert ApiActions.get_value_from_json("name", response) == name
    assert ApiActions.get_value_from_json("job", response) == job
    assert ApiActions.get_status_code(response) == 200
