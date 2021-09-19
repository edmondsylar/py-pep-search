from flask import Flask, render_template, request
from person_fetch import Search
import json


# initialize app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def results():
    search = request.form.get('search')
    res = Search(search.replace(" ", "+"), False).get_info()

    return render_template('results.html', data=res, phrase=search)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
