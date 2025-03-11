from random import choice
import json

from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Id астронавта', validators=[DataRequired()])
    password = PasswordField('Пароль астронавта', validators=[DataRequired()])
    cap_name = StringField('Id капитана', validators=[DataRequired()])
    cap_password = PasswordField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/success')
def suc():
    return render_template('suc.html', title='Успех')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('double_defend.html', title='Авторизация', form=form)


@app.route('/distribution')
def dist():
    lst = ['Александр Пушкин', 'Михаил Лермонтов', 'Дуглас Адамс', 'Михаил Булгаков', 'О. Генри']
    return render_template('distribution.html', title='Авторизация', lst=lst)


@app.route('/table/<sex>/<int:old>')
def table(sex, old):
    return render_template('table.html', title='Авторизация', sex=sex, old=old)


@app.route('/load_photo', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('photocard.html', title='Картинка')
    elif request.method == 'POST':
        f = request.files['file']
        print(f)
        f.save('./static/save_img/p.png')
        return render_template('photocard.html', title='Картинка')


@app.route('/carousel')
def carousel():
    return render_template('carousel.html', title='Карусель')


n = 0
images = ['dino.png', 'female_ast.png', 'predatelstvo.jpg', 'male_ch.jpg']


@app.route('/gallery', methods=['POST', 'GET'])
def gallery():
    global n, images
    if request.method == 'GET':
        return render_template('gallery.html', title='Галерея',
                               images=images)
    elif request.method == 'POST':
        n += 1
        f = request.files['file']
        f.save(f'./static/save_img/p{n}.png')
        images.append(f'p{n}.png')
        return render_template('gallery.html', title='Картинка',
                               images=images, ln=len(images))


@app.route('/member')
def member():
    with open('templates/members.json', encoding='utf-8') as members:
        data = json.load(members)
    sp = []
    for key, value in data.items():
        sp.append(value)
    return render_template('member.html', title='Member', member=choice(sp))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
