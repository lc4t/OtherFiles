from flask import Flask
from flask import render_template
from flask import request
from pymongo import MongoClient
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',title='hello')




@app.route('/search/<q>')
def search(q=None):
    pages = []
    client = MongoClient()
    db = client.items.YbookItem
    _ = db.find({'title': {'$regex': q, '$options':'i'}}, {'_id': 0, 'content': 0, 'url': 0})
    for i in _:
        pages.insert(0, i)

    return render_template('index.html', title=q, pages=pages)


@app.route('/see/<title>')
def see(title=None):

    client = MongoClient()
    db = client.items.YbookItem
    pages = []
    _ = db.find({'title': title}, {'_id': 0, 'update': 0})
    for i in _:
        # i['content'] = str(i['content'])
        # i['content'] = i['content'].replace('\\n', '&lt;br/&gt;').replace('\\r', '&lt;br/&gt;')
        pages.append(i)
    # print(pages)

    return render_template('see.html', title=title, pages=pages)



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
