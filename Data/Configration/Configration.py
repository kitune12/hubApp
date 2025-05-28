import configparser
import os

def load_config():
    config = configparser.ConfigParser()
    path = os.path.join(os.path.dirname(__file__), "config.ini")
    config.read(path)
    return config