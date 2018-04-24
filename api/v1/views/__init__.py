#!/usr/bin/python3
'''
    init file for
'''
from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint('/api/v1')
