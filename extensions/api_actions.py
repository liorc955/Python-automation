import json

import allure
import requests
import jsonpath
from utilities import read_properties

url = read_properties.get_api_data("baseUrl")


@allure.step("Parse Json File to Python Dictionary")
def parseToJson(path):
    with open(path, mode="r") as file:
        return json.load(file)


@allure.step("Get Data")
def get():
    return requests.get(url)


@allure.step("Post Data")
def post(request_json):
    return requests.post(url, request_json)


@allure.step("Update Data")
def put(request_json):
    return requests.put(url, request_json)


@allure.step("Delete Data")
def delete():
    return requests.delete(url)


@allure.step("Extract a Value From JSON")
def get_value_from_json(key, response):
    response_json = json.loads(response.content)
    return response_json[key]


@allure.step("Extract Values From JSON")
def get_values_from_json(key, response):
    response_json = json.loads(response.content)
    return jsonpath.jsonpath(response_json, key)


@allure.step("Get Status Code")
def get_status_code(response):
    return response.status_code
