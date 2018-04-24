#!/usr/bin/python3
'''
   contain teardown method
'''
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

app = Flask(__name__)
app.register_blueprint(app)


@app.teardown_appcontext
def teardown():
    '''
        Teardown method for storage session
    '''
    storage.close()


if __name__ == "__main__":
    app.run(os.getenv('HBNB_API_HOST'), os.getenv('HBNB_API_PORT'))
