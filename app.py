from flask import Flask, render_template
import os
import psycopg2
app = Flask(__name__)

DB_HOST = os.environ['DB_HOST']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']
DB_NAME = os.environ['DB_NAME']


conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port="5432"
)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/index')
def index():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM manuscript")
    data = cursor.fetchall()
    cursor.close()

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run()
