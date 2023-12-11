import os
from dotenv import load_dotenv

load_dotenv()
USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')
DB_NAME = os.getenv('DB_NAME')

GET_USER_NAME = os.getenv('GET_USER_NAME')
INSERT_USER_NAME = os.getenv('INSERT_USER_NAME')
USER_NEWS_DATA = os.getenv('USER_NEWS_DATA')
INSERT_NEWS_DATA = os.getenv('INSERT_NEWS_DATA')
USER_NEWS_DATA_ID = os.getenv('USER_NEWS_DATA_ID')
DELETE_USER_NEWS = os.getenv('DELETE_USER_NEWS')