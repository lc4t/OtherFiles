from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',name='flag{2_young_2_naive}')


@app.route('/<name>/')
def ids(name = None):
    if (name == None):
        return index()
    return render_template('index.html',name=name)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if (request.form['username'] and request.form['password']):
            return '1'

    return render_template('index.html', name=request.args.get('username', ''))


if __name__ == '__main__':
    app.debug = True
    app.run()