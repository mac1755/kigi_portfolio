import get_news
import db_model

db = db_model.DB_Model()

# カテゴリーリストを渡す
def get_category_name_list():
    return get_news.category_names

# formからのカテゴリ名でURLを生成
# url_categorysでURLとカテゴリを一致確認
def get_news_contents(category):
    set_category = get_news.url_categorys[category]
    vgm_url = f"https://news.yahoo.co.jp/topics/{set_category}"
    result = get_news.get_news_base(vgm_url)
    return result

def get_news_text(url):
    result = get_news.get_news_body_urls(url)
    return result

def get_news_main_content(url):
    result_data = get_news.get_news_body_urls(url)
    return result_data

def get_user_news_contents(user_name):
    result = db.select_name_news_data(user_name)
    return result

def get_user_news_titles(user_name, news_title):
    result = db.select_name_news_data(user_name)
    titles = [user_news_data['news_title'] for user_news_data in result]
    if news_title in titles:
        return False
    else:
        return True

def get_user_news_id(id):
    result = db.select_id_news_data(id)
    return result

def user_login(user):
    users = db.all_get_data()
    user_list = [us['user_name'] for us in users]
    if user in user_list:
        return True
    else:
        return False

def user_session(sess):
    if 'user' in sess:
        return True
    else:
        return False

def register_user(user_name):
    if user_login(user_name):
        return False
    else:
        db.register_data(user_name)
        return True

def register_news_data(user_name, news_title, news_body):
    db.register_news_data(user_name, news_title, news_body)

def delete_user_news(id):
    db.select_id_delete_news_data(id)