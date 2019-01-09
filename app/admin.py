from flask import Blueprint,render_template, request, redirect, session, url_for
from app import db
from .models import Admin,Article
from app import form

admin = Blueprint('admin',__name__)

def is_admin():
    if 'username' in session and session['username'] == 'ybc':
        return True
    else:
        return False

@admin.route('/')
def login():
    loginform = form.LoginForm()
    return render_template('/admin/login.html',loginform=loginform)

@admin.route('/verify/',methods=['POST','GET'])
def verify():
    try:
        _id = request.form['id']
        _password = request.form['password']
        _admin = Admin.query.filter_by(id=_id).first()
        if _admin and _admin.password == _password:
            session['id'] = _admin.id
            session['username'] = _admin.username
            return redirect('/admin/center/')
        else:
            return redirect('/admin/')
    except Exception as e:
        return e

@admin.route('/center/')
def center():
    if is_admin():
        username = session['username']
        articles = Article.query.all()
        return render_template('/admin/center.html',username=username,articles=articles)
    else:
        return redirect('/admin/')

@admin.route('/logout/')
def logout():
    session.pop('id', None)
    session.pop('username', None)
    return redirect('/admin/')

@admin.route('/new/')
def new():
    if is_admin():
        return render_template('/admin/new.html')
    else:
        return redirect('/admin/')

@admin.route('/add/',methods=['POST','GET'])
def add():
    if is_admin():
        try:
            _id = request.form['id']
            _link = request.form['link']
            _private = request.form['private'] == 'True'
            _title = request.form['title']
            _author = request.form['author']
            _abstract = request.form['abstract']
            _content = request.form['content']
            new_article = Article(
                id=_id,
                link=_link,
                private=_private,
                title = _title,
                author = _author,
                abstract = _abstract,
                content = _content
            )
            db.session.add(new_article)
            db.session.commit()
            return redirect('/admin/center/')
        except Exception as e:
            return e
    else:
        return redirect('/admin/')

@admin.errorhandler(404)
def page_not_found():
    return render_template('404.html'),404