from flask import Flask, request, render_template
from tools import read_json, len_list, get_posts

from flask_restx import Api

from config import Config
from views.main import main_ns


app = Flask(__name__)


@app.route('/')
def main():
    list_1 = read_json("data/data.json")
    number = len_list("data/data.json")

    return render_template('main.html', list_1=list_1, number=number)


@app.route('/articles/<int:articleid>')
def post(articleid):
    list_1 = read_json("data/data.json")
    return render_template('articles.html', postid=articleid, list_1=list_1)


@app.route('/search')
def search():
    search_1 = request.args.get('s')
    list_3 = read_json("data/data.json")
    posts = get_posts(list_3, search_1)
    return render_template('search.html', posts=posts, numbers=len(posts), search_1=search_1)


if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)