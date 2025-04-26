import json


class Config:
    def __init__(self, config_path="./utils/config.json"):
        with open(config_path, "r", encoding="utf-8") as file:
            self.config = json.load(file)

    def get(self, key):
        return self.config.get(key)

config = Config()