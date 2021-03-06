import os
from dotenv import load_dotenv
from flask import Flask
from flask import render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
import requests

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(200))
    due = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        todos = Todo.query.all()
        return render_template('index.html', todos=todos)

@app.route('/test')
def test():
    values = {
        "val1": 100, "val2" :200, "val3" :300, "val4" :400 
        }
    return render_template('temp/test.html', values=values)  #jsonify(values) 

@app.route('/movie')
def movie():
    url = f'https://www.omdbapi.com/?s=man&apikey={os.getenv("API_KEY")}'
    res = requests.get(url).json()
    datas = res['Search'][:15]
    movie_data = []
    for dict_data in datas:
        data = {
            'title' : dict_data['Title'],
            'poster' : dict_data['Poster'],
            'year' : dict_data['Year'],
            }
        movie_data.append(data)
    return render_template('temp/movie.html', movie_data=movie_data, datas=datas)
        

@app.route('/zipcode/<code>')
def zipcode(code):
    
    url = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={code}'
    res = requests.get(url).json()
    json_data = {
        "pref" : res['results'][0]['address1'],
        "city" : res['results'][0]['address2'],
        "area" : res['results'][0]['address3'],
        "prefcode" : res['results'][0]['prefcode'],
        }
    return render_template('/temp/zipcode.html', json_data=json_data, res=res)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        due = request.form.get('due')

        due = datetime.strptime(due, '%Y-%m-%d')
        todo = Todo(title=title, content=content, due=due)
        
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create.html')

@app.route('/detail/<int:id>')
def read(id):
    todo = Todo.query.get(id)
    return render_template('detail.html', todo=todo)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    todo = Todo.query.get(id)
    if request.method == 'GET':
        return render_template('edit.html', todo=todo)
    else:
        todo.title = request.form.get('title')
        todo.detail = request.form.get('detail')
        todo.due = datetime.strptime(request.form.get('due'), '%Y-%m-%d')

        db.session.commit()
        return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    todo = Todo.query.get(id)

    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

#export FLASK_ENV=development =>Debug mode: on
#??????????????????app.run(debug=True)