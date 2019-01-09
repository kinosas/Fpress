from app import app
from .admin import admin
from .visitor import visitor

app.register_blueprint(visitor, url_prefix='/')
app.register_blueprint(admin,url_prefix='/admin')