from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz

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
def hello_world():
    values = {"val1": 100, "val2" :200, "val3" :300, "val4" :400 }
    return render_template('index.html', values=values)

@app.route('/create', methods=['GET', 'POST'])
def create():
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug=True)

#export FLASK_ENV=development =>Debug mode: on
#↑↑と同義：app.run(debug=True)