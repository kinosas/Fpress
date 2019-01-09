from app import db

class Admin(db.Model):
    __tablename__ = 'admins'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(36),nullable=False)
    password = db.Column(db.String(36),nullable=False)

    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %s>'%(self.username)

class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    link = db.Column(db.String(64),unique=True)
    browsed = db.Column(db.Integer,nullable=True)
    private = db.Column(db.Boolean,nullable=True)
    title = db.Column(db.String(20),nullable=True)
    author = db.Column(db.Integer,db.ForeignKey('admins.id'))
    abstract = db.Column(db.String(200),nullable=False)
    content = db.Column(db.String(5000),nullable=False)

    def __init__(self,link,private,title,author,abstract,content):
        self.link = link
        self.browsed = 0
        self.private = private
        self.title = title
        self.author = author
        self.abstract = abstract
        self.content = content

    def __repr__(self):
        return '<Artical abstract %s>'%self.abstract
