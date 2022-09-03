import json

import allure
import requests
import jsonpath


@allure.step("Parse Json File to Python Dictionary")
def parseToJson(path):
    file = open(path, "r")
    data_input = file.read()
    return json.loads(data_input)


@allure.step("Get Data")
def get(url):
    return requests.get(url)


@allure.step("Post Data")
def post(url, request_json):
    return requests.post(url, request_json)


@allure.step("Update Data")
def put(url, request_json):
    return requests.put(url, request_json)


@allure.step("Delete Data")
def delete(url):
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
