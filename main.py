from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


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


    def __init__(self, btitle, bpost):
        self.btitle = btitle
        self.bpost = bpost


tasks = []

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html',title="Build-A-Blog!", tasks=tasks)

def new_post():
    return render_template('new_post.html',title="Build-A-Blog!")

def post():

    if request.method == 'POST':
        title = request.form['title']
        entry = request.form['entry']
        blog_post = Blog(title, entry)
        db.session.add(blog_post)
        db.session.commit()

    if request.method == 'GET':
        post_id = request.args.get('post_id')
        this_post = Blog.get(post_id)

    return render_template('post.html',title=title)



if __name__ == '__main__':
    app.run()
