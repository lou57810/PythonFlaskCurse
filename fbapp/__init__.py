import os
from flask import Flask

from .views import app
from . import models

models.db.init_app(app)


@app.cli.command()
def init_db():
    print("lancement app!")
    # db_local = db
    # db_local.init_app(app)
    print('init_db is running!')
    models.init_db()
