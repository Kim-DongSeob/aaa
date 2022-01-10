import json
from flask import Flask, render_template, jsonify, request, redirect, session
from pymongo import MongoClient

app = Flask(__name__)

# client = MongoClient('mongodb://test:test@localhost', 27017)
client = MongoClient('localhost', 27017)
db = client.chapter01


@app.route('/')
def home():
    return render_template('mainPage.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=8080, debug=True)
