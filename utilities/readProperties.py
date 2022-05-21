import configparser
from os.path import dirname


config = configparser.RawConfigParser()
config.read(dirname(dirname(__file__)) + "/Configurations/config.ini")


class ReadConfig:
    @staticmethod
    def get_web_data(key):
        return config.get("web info", key)

    @staticmethod
    def get_api_data(key):
        return config.get("api info", key)
