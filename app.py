from flask import Flask, render_template, request
from person_fetch import Search
import json
import sqlite3

# initialize and create database.
DB_NAAME = "PEPS.db"
def get_database_cnnection():
    con = sqlite3.connect(DB_NAAME)

# initialize app
app = Flask(__name__)
# get_database_cnnection()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def results():
    search = request.form.get('search')
    res = Search(search.replace(" ", "+"), False).get_info()

    return render_template('results.html', data=res, phrase=search)

@app.route('/stored-peps')
def peps():
    return render_template('peps.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)
