from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    return render_template('base.html', title='Домашняя страница')


@app.route('/training/<prof>')
def tran(prof):
    return render_template('train.html', title='Тренировка', prof=prof)


@app.route('/list_prof/<list>')
def l_pr(list):
    prfs = ['инженер-исследователь', 'пилот', 'строитель', 'экобиолог', 'врач', 'климатолог', 'метеоролог', 'астролог']
    return render_template('lst.html', title='Профессии', prfs=prfs, par=list)


@app.route('/answer')
@app.route('/auto_answer')
def ans():
    d = {'title': 'Анкета', 'surname': 'PushKing', 'name': 'AlexUnder', 'education': 'Высшее',
         'profession': 'космодесантник', 'sex': 'male',
         'motivation': 'Я люблю красный! Готов к встрече с враждебными марсианами.', 'ready': True}
    return render_template('auto_answer.html', title=d['title'], dictn=d)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
