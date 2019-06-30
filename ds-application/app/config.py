from os import getenv

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    ENV = getenv('FLASK_ENV')
