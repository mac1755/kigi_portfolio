from bs4 import BeautifulSoup
import requests

# =============================================================================
# ニュースの表示カテゴリ
# メインページから以下のカテゴリをプルダウンで選択し、選択されたカテゴリからURLを生成する。
# URLを生成したらタイトルと本文URLを全取得してページに表示する。
# =============================================================================
url_categorys = {
    '国内': "domestic",
    '国際': "world",
    '経済': "business",
    'エンターテイメント': "entertainment",
    'スポーツ': "sports",
    'IT': "it",
    '科学': "science",
}
# プルダウンを作成する時のカテゴリ名
category_names = {
    'domestic': "国内",
    'world': "国際",
    'business': "経済",
    'entertainment': "エンターテイメント",
    'sports': "スポーツ",
    'it': "IT",
    'science': "科学"
}

# ===========================================================
# HTMLをパースした結果を返す
# ===========================================================
def html_parser(url):
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup

# ===========================================================
# 最初のページで取得したURLから記事の詳細ページのURLを取得する
# ニュース一覧からユーザーが記事タイトル（詳細）をクリックした時に該当URLから詳細URLを取得して返す
# ===========================================================
def get_news_body_urls(url):
    soup = html_parser(url)
    news_body_elements = soup.find('a', class_="sc-eWLqKx gqAhZg")
    news_body_url = news_body_elements.get('href')
    soup = html_parser(news_body_url)
    try:
        data = soup.find('div', class_="article_body highLightSearchTarget").text
    except:
        data = ""
    return data

# ===========================================================
# カテゴリのURLからニュースのタイトルと本文URLを取得して結果を返す
# ページが読み込まれた時にそのまま実行可能
# ===========================================================
def get_news_base(url):
    soup = html_parser(url)
    news_link_url = soup.find_all('li', class_="newsFeed_item")

    news_item_urls = {}
    news_item_titles = []

    for elements in news_link_url:
        for element in elements:
            try:
                item_url = element.get('href')
                item_title = element.find('div', class_="newsFeed_item_title").text
                news_item_urls[item_title] = item_url
                news_item_titles.append(item_title)
            except:
                pass
    result = {'news_item_title': news_item_titles, 'news_item_urls': news_item_urls}
    return result



