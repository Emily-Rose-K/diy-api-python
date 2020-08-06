from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/flask_dogs'
app.config['FLASK_ENV'] = 'development'
app.config['FLASK_APP'] = 'app.py'

from dog_crud import *

@app.route('/')
def home():
    return jsonify({'message' : 'Home Page'})

@app.route('/dogs', methods=['GET', 'POST'])
def all_dogs():
    if request.method == 'GET':
        return get_all_dogs()
    if request.method == 'POST':
        create_dog(request.form['name'], request.form['breed'], request.form['age'])
        return redirect('/dogs')

@app.route('/dog/<id>', methods=['GET', 'PUT', 'DELETE'])
def dog_detail():
    if request.method == 'GET':
        return get_dog(id)
    if request.method == 'PUT':
        return update_dog(id)
    if request.method == 'DELETE':
        return destroy_dog(id)