from flask import Flask, url_for, request
from random import choice

app = Flask(__name__)


@app.route('/')
def mission():
    return """Миссия Колонизация Марса"""


@app.route('/index')
def mission2():
    return """И на Марсе будут яблони цвести!"""


@app.route('/promotion')
def advertisement_phrase():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <p>Человечество вырастает из детства.<br>
                    Человечеству мала одна планета.<br>
                    Мы сделаем обитаемыми безжизненные пока планеты.
                    И начнем с Марса!<br>
                    Присоединяйся!</p>
                  </body>
                </html>"""


@app.route('/image_mars')
def image():
    return """<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                      </head>
                      <body>
                        <h1>Ждин нас Марс!</h1>
                        <img src="/static/img/mars.jpg" width="500" height="500" alt="Не нашел">
                        <p>Вот она какая, красная планета</p>
                      </body>
                    </html>"""


@app.route('/promotion_image')
def bootstrap():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" >
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    
                    <img src="/static/img/mars.jpg" width="500" height="500" alt="Не нашел">
                    
                    <div class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    
                    <div class="alert alert-primary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    
                    <div class="alert alert-warning" role="alert">
                      И начнём с Марса!
                    </div>
                    
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                    
                  </body>
                </html>"""


@app.route('/form_sample', methods=['POST', 'GET'])
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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1>Анкет претендента</h1>
                            <h3>На участие в миссии</h3>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="name1" class="form-control" id="name2" aria-describedby="emailHelp" placeholder="Введите Фамилию" name="second_name">
                                    <input type="name2" class="form-control" id="name1" placeholder="Введите имя" name="first_name">
                                    <br>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="class">
                                            <option value="first">Начальное</option>
                                            <option value="second">Основное общее</option>
                                            <option value="third">Среднее общее</option>
                                            <option value="fourth">Среднее профессиональное</option>
                                            <option value="fiveth">Высшее оконченное</option>
                                            <option value="sixth">Высшее квалификационное</option>
                                        </select>
                                     </div>
                                     <div class="form-group">
                                        <label for="form-profession">Какие у Вас есть профессии?</label>
                                        <div>
                                            <input type="checkbox" id="scales" name="scales">
                                            <label for="scales">Инженер-исследователь</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" id="horns" name="horns">
                                            <label for="horns">Инженер-строитель</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" id="scales" name="scales">
                                            <label for="scales">Пилот</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" id="horns" name="horns">
                                            <label for="horns">Метеоролог</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" id="scales" name="scales">
                                            <label for="scales">Инженер по жизнеобеспечению</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" id="horns" name="horns">
                                            <label for="horns">Инженер по радиационной защите</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" id="scales" name="scales">
                                            <label for="scales">Врач</label>
                                        </div>
                                        <div>
                                            <input type="checkbox" id="horns" name="horns">
                                            <label for="horns">Экзобиолог</label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                     <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на Марсе?</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def planet_info(planet_name):
    planets = {'Меркурий': ["Крохотулечка-планета",
                            "Первой Солнышком согрета",
                            "И проворна — год на ней",
                            "Восемьдесят восемь дней."],
               'Венера:': ["Только Солнце и Луна",
                           "В небе ярче, чем она.",
                           "Да и горячей планеты",
                           "В Солнечной системе нету."],
               'Марс': ["Планета огненного смерча",
                        "Жара повсюду и кругом",
                        "И космонавты как младенцы",
                        "Застыли тут с открытым ртом."],
               'Юпитер': ["Великан-тяжеловес",
                          "Мечет молнии с небес",
                          "Полосат он, словно кошка",
                          "Жаль худеет понемножку."],
               'Сатурн': ["Пышный газовый гигант",
                          "Брат Юпитера и франт",
                          "Любит он, чтоб рядом были",
                          "Кольца изо льда и пыли."],
               'Уран': ["Я — планета Уран",
                        "Берегите глаза!",
                        "Планета — вспышка!",
                        "Планета — гроза!",
                        "И только свободу",
                        "Люблю и лелею.",
                        "Я — планета Водолея."],
               'Нептун:': ["На планете синей-синей",
                           "Дует ветер очень сильный.",
                           "Год на ней велик весьма —",
                           "Длится 40 лет зима."],
               'Земля': ["На планете чудеса:",
                         "Океаны и леса",
                         "Кислород есть в атмосфере",
                         "Дышат люди им и звери."]}
    colors = ['success', 'secondary', 'warning', 'danger', 'primary', 'info', 'light', 'dark']
    text = "".join(
        [f"""<div class="alert alert-{choice(colors)}" role="alert">{el}</div>""" for el in planets[planet_name]])
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Варианты выбора</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style.css"/>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                  </body>
                  {text}
                </html>"""


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Варианты выбора</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="static/css/style.css"/>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <h4><div class="alert alert-success" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора</div>
                    составляет {rating}!
                    <div class="alert alert-warning" role="alert">Желаем удачи!</div><h4>
                  </body>
                  </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def photo():
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
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                          
                            <h1>Загрузка фотографии</h1>
                            <h3>для участия в миссии</h3>
                            <div>
                                <form class="photo_form" method="post">
                                     <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" id="photo" name="file" onchange="preview()">
                                        <br/><br/>
                                        <img id="frame" src="" class="img-fluid" />
                                        <br/><br/>
                                    </div>
                                    <script src="{url_for('static', filename='js/app.js')}"></script>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        return "Форма отправлена"


@app.route('/carousel')
def carousel_photo():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Пейзажи Марса</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1>Пейзажи Марса</h1>
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                      <ol class="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                      </ol>
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img class="d-block w-100" src="{url_for('static', filename='img/mars1.jpg')}" alt="First slide">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename='img/mars2.jpg')}" alt="Second slide">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename='img/mars3.jpg')}" alt="Third slide">
                        </div>
                      </div>
                      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                      </a>
                      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                      </a>
                    </div>
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
