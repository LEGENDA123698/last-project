""" Програма використовує flask та запускає веб-сервер.
При запиті на цей сервер він повертає вміст файлу index.html
Файл обробляється як шаблон. Він не знаходиться! """
from flask import Flask, render_template

def index():
    """ функція обробляє шаблон index.html і повертає документ, що вийшов."""
    return render_template('index.html')

app = Flask(__name__) 

# створюємо правило для URL '/': 
app.add_url_rule('/', 'index', index)

# Запускаємо веб-сервер:
app.run()
