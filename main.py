import flask

import time
import os

from flask import request, jsonify
from flask import render_template
from flask import app

import traceback
from wardrobe import Wardrobe

running_tasks = []

OK = "200"
BAD_REQUEST = "400"
SERVER_ERROR = "500"

wardrobe = Wardrobe()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_clothing_item():
    if request.method == 'POST':
        form = request.data
        wardrobe.add_item()


