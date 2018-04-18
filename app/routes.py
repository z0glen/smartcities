from flask import render_template
from app import app
from app.articles import advertising_article, transportation_article, about_article, case_studies_article, boston_smart_city_article

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

@app.route('/about')
def about():
    article = about_article
    return render_template('article.html', article=article)

@app.route('/case_studies')
def case_studies():
    article = case_studies_article
    return render_template('article.html', article=article)

@app.route('/boston_smart_city')
def boston_smart_city():
    article = boston_smart_city_article
    return render_template('article.html', article=article)
