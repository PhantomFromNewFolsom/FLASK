from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('base.html', title='Домашняя страница')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
