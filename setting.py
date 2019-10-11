# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

APIKEY01 = os.environ.get("API_KEY_01")
