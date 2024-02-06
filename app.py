#!/usr/bin/env python3
from flask import Flask, render_template
import psycopg2
from config import db_config


app = Flask(__name__)

dbname = db_config['dbname']
user = db_config['user']
password = db_config['password']
host = db_config['host']
port = db_config['port']

def get_db_connection():
        conn = psycopg2.connect(**db_config)
        return conn

@app.route("/")
def hello():
    return render_template('home.html')



@app.route('/index')
def index():
    conn = get_db_connection()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()
