from flask import Blueprint,render_template, request, redirect
from app import db
from .models import Article

visitor = Blueprint('visitor',__name__)

@visitor.route('/')
def index():
    articles = Article.query.all()  
    return render_template('visitor/index.html',articles=articles)

@visitor.route('/article/<id>')
def article(id):
    # 根据这id来进行分类，这里的逻辑还没理清楚
    return "查询结果"

@visitor.errorhandler(404)
def page_not_found():
    return render_template('404.html'),404