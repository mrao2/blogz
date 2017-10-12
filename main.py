from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from dateTime import datetime


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:mohith@localhost:3306/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)
class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    btitle = db.Column(db.String(80), nullable=False)
    bpost = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __init__(self, btitle, bpost, pub_date):
        self.btitle = btitle
        self.bpost = bpost
        self.pub_date = pub_date

tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():

    if request.method == 'POST':
        task = request.form['task']
        tasks.append(task)

    return render_template('index.html',title="Build-A-Blog!", tasks=tasks)

if __name__ == '__main__':
    app.run()
