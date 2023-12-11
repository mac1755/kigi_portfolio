import mysql.connector
from config import *
from datetime import datetime
import pytz

# ===============================================
# クラスの作成
# ===============================================
class DB_Model:
    # ===============================================
    # 初期化で必要情報をセットする
    # ===============================================
    def __init__(self):
        self.created_at = datetime.now(pytz.timezone('Asia/Tokyo'))
        self.USER = USER_NAME
        self.PORT = PORT
        self.HOST = HOST
        self.PASSWORD = PASSWORD
        self.DATABASE = DB_NAME
        self.conn = None
        self.cur = None

    # ================================================
    # コネクションとカーソルを作成する
    # ================================================
    def start_connection(self):
        self.conn = mysql.connector.connect(
            host = self.HOST,
            port = self.PORT,
            user = self.USER,
            password = self.PASSWORD,
            database = self.DATABASE
        )
        self.cur = self.conn.cursor(dictionary=True, buffered=True)

    # ================================================
    # コネクションとカーソルを閉じる
    # ================================================
    def close_connection(self):
        self.cur.close()
        self.conn.close()

    # ================================================
    # ユーザーデータをすべて取得する
    # ================================================
    def all_get_data(self):
        self.start_connection()
        sql = GET_USER_NAME
        self.cur.execute(sql)
        result = self.cur.fetchall()
        self.close_connection()
        return result

    # ================================================
    # 新規のユーザーを追加する
    # ================================================
    def register_data(self, user_name):
        self.start_connection()
        sql = INSERT_USER_NAME
        val = (self.created_at, user_name)
        self.cur.execute(sql, val)
        self.conn.commit()
        self.close_connection()

    # ================================================
    # ユーザーを指定してニュースデータを取得する
    # ================================================
    def select_name_news_data(self, user):
        self.start_connection()
        sql = USER_NEWS_DATA
        val = (user,)
        self.cur.execute(sql, val)
        result = self.cur.fetchall()
        self.close_connection()
        return result

   # ================================================
    # IDを指定してニュースデータを取得する
    # ================================================
    def select_id_news_data(self, id):
        self.start_connection()
        sql = USER_NEWS_DATA_ID
        val = (id,)
        self.cur.execute(sql, val)
        result = self.cur.fetchall()
        self.close_connection()
        return result

  # ================================================
    # IDを指定してニュースデータを削除する
    # ================================================
    def select_id_delete_news_data(self, id):
        self.start_connection()
        sql = DELETE_USER_NEWS
        val = (id,)
        self.cur.execute(sql, val)
        self.conn.commit()
        self.close_connection()

    # ================================================
    # 新規の記事を追加する
    # ================================================
    def register_news_data(self, user_name, news_title, news_body):
        self.start_connection()
        sql = INSERT_NEWS_DATA
        val = (self.created_at, user_name, news_title, news_body)
        self.cur.execute(sql, val)
        self.conn.commit()
        self.close_connection()
