from flask import render_template
from app import app
from app.articles import advertising_article, transportation_article

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/advertising')
def advertising():
    article = advertising_article
    return render_template('article.html', article=article)

@app.route('/transportation')
def transportation():
    article = transportation_article
    return render_template('article.html', article=article)
