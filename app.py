import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=585afa0a90e01f4d1993529964edf181"
    city = 'Nairobi'


    r = requests.get(url.format(city)).json()
    print(r)
    return render_template('weather.html')
