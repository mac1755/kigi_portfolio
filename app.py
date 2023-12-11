from flask import Flask, render_template, request,redirect, session
from datetime import timedelta
import controller

app = Flask(__name__)

# Sessionの管理
app.secret_key = 'cate'
app.secret_key = 'data'
app.secret_key = 'user'
app.permanent_session_lifetime = timedelta(minutes=20)

# test
in_user = "test"

# メインページ
@app.route('/', methods=['GET', 'POST'])
def index():
    session['cate'] = ""
    session['data'] = ""
    if 'user' in session:
        category = controller.get_category_name_list()
        if request.method == "GET":
            return render_template('index.html', category=category)
        else:
            select_category = request.form.get("category")
            session['cate'] = select_category
            return redirect('/result')
    else:
        return redirect('/login')

# ログインページ
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        session['user'] = ""
        return render_template('login.html')
    else:
        user = request.form.get('user')
        if controller.user_login(user):
            session['user'] = user
            return redirect('/')
        else:
            return redirect('login')

# 新規ユーザー登録
@app.route('/user_register', methods=['GET', 'POST'])
def user_register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        register_user = request.form.get('register_name')
        if controller.register_user(register_user):
            return redirect('/login')
        else:
            return redirect('/user_register')

# ニュース一覧ページ
@app.route('/result', methods=["GET", "POST"])
def result_page():
    if 'user' in session:
        if request.method == "GET" and 'cate' in session:
            try:
                news_data = controller.get_news_contents(session['cate'])
                session['data'] = news_data
                counter = len(news_data['news_item_title'])
                return render_template('result.html', news_data=news_data, counter=counter)
            except:
                return redirect('/')
        else:
            news_title = request.form.get('news_title')
            return redirect(f'/news/{news_title}')
    else:
        return redirect('/login')

# ニュース詳細ページ
@app.route('/news/<news_title>', methods=['GET', 'POST'])
def news(news_title):
    if 'user' in session:
        news_data = session['data']
        news_titles = news_data['news_item_title'][int(news_title)]
        news_url = news_data['news_item_urls'][news_titles]
        news_content = controller.get_news_main_content(news_url)
        if request.method == 'GET':
            return render_template('news.html', news_title=news_titles, news_content=news_content)
        else:
            # 記事を保存
            if controller.get_user_news_titles(user_name=session['user'], news_title=news_titles):
                controller.register_news_data(user_name=session['user'], news_title=news_titles, news_body=news_content)
                return redirect(f'/result')
            else:
                return render_template('news.html', news_title=news_title, news_content=news_content)
    else:
        return redirect('/login')

# ユーザーのお気に入り記事を表示
@app.route('/set_news', methods=['GET', 'POST'])
def set_news():
    if 'user' in session:
        news_data = controller.get_user_news_contents(session['user'])
        if request.method == 'GET':
            return render_template('set_news_view.html', user_name=session['user'], news_data=news_data)
        else:
            return redirect('/')
    else:
        return redirect('/login')

# ユーザー保存記事の詳細ページ
@app.route('/user_news/<news_title_id>', methods=['GET', 'POST'])
def user_news(news_title_id):
    if 'user' in session:
        if request.method == "GET":
            news_data = controller.get_user_news_id(news_title_id)
            return render_template('user_news.html', news_data=news_data)
        else:
            controller.delete_user_news(id=news_title_id)
            return redirect('/set_news')
    else:
        return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)