#!/usr/bin/env python3
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/')
def display_tables():
    keyword = request.args.get('keyword', '')
    inspector = db.inspect(db.engine)
    tables = inspector.get_table_names()
    filtered_tables = [table for table in tables if keyword.lower() in table.lower()]
    return render_template('home.html', tables=filtered_tables, keyword=keyword)

if __name__ == '__main__':
    app.run(debug=True)
