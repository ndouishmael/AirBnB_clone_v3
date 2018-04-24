#!/usr/bin/python3
'''
   contain teardown method
'''
from flask import Flask
from models import storage
from api.v1.views import app_views
import os


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(exception):
    '''
        Teardown method for storage session
    '''
    storage.close()

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
