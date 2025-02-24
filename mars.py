from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def home():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promote():
    return '''<p>Человечество вырастает из детства.</br>
Человечеству мала одна планета.</br>
Мы сделаем обитаемыми безжизненные пока планеты.</br>
И начнем с Марса!</br>
Присоединяйся!</p>'''


@app.route('/image_mars')
def photo_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.png')}" alt="здесь должна была быть
                     картинка, но не нашлась">
                    <p>Здесь могла быть ваша реклама, но пока у нас нет</br> 
                    спонсоров, так что купите пожалуйста рекламу(</br></p>
                    <div class="alert alert-danger" role="alert">
                      P. S. Андрей Юрьевич, зачтите задачу пожалуйста, там не указано, какая конкретно должна быть
                    подпись
                    </div>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promo_photo():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                        <title>Привет, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/mars.png')}" alt="здесь должна была быть
                         картинка, но не нашлась">
                        <div class="alert alert-dark" role="alert">
                          Человечество вырастает из детства.
                        подпись
                        </div>
                        <div class="alert alert-success" role="alert">
                          Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                          И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Присоединяйся!
                        </div>
                      </body>
                    </html>"""


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', 
                                                                                  filename='css/mystyle.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h2 align="center">Анкета претендента на участие в миссии</h2>
                            <div>
                                <form class="login_form" method="post">
                                    <input class="form-control" id="surname"
                                    placeholder="Введите фамилию" name="surname">
                                    <input class="form-control" id="name"
                                    placeholder="Введите имя" name="name">
                                    <label></label>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" 
                                    placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-control" id="educationSelect" name="education">
                                          <option>Отсутствует</option>
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                    <label>Какие у Вас есть профессии?</label>
                                    <br>
                                    <label>
                                        <input type="checkbox" name="profession1" value="engineer">
                                        Инженер
                                      </label>
                                      <br>
                                      <label>
                                        <input type="checkbox" name="profession2" value="pilot">
                                        Пилот
                                      </label>
                                      <br>
                                      <label>
                                        <input type="checkbox" name="profession3" value="ecobiolog">
                                        Экобиолог
                                        </label>
                                    <br>
                                    <label>
                                        <input type="checkbox" name="profession4" value="builder">
                                        Строитель
                                        </label>
                                    <br>
                                    <label>
                                        <input type="checkbox" name="profession5" value="doctor">
                                        Врач
                                        </label>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male"
                                           value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female"
                                           value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">
                                        Готовы остаться на марсе</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print('Профессии:')
        for i in range(1, 6):
            prof = request.form.get(f'profession{i}')
            if prof is not None:
                print('   ' + request.form.get(f'profession{i}'))
        print(request.form['about'])
        print(request.form.get('accept'))
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def chosen_planet(planet_name):
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link rel="stylesheet" href="{url_for('static', filename='css/style.css')}">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet_name}</h1>
                        <h3>Эта планета близка к Земле</h3>
                        <div class="alert alert-dark" role="alert">
                          Там много полезных ресурсов
                        </div>
                        <div class="alert alert-success" role="alert">
                          На ней есть вода и атмосфера
                        </div>
                        <div class="alert alert-secondary" role="alert">
                          У неё есть некоторое магнитное поле
                        </div>
                        <div class="alert alert-warning" role="alert">
                          Она очень красива
                        </div>
                        <div class="alert alert-danger" role="alert">
                          Присоединяйся, мы колонизируем {planet_name}!
                        </div>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)
