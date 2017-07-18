
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:buildablog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'xfd{H\xe5<\xf9\x6a2\xa0\x9fR"\xa1\xa8'

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1200))
    created = db.Column(db.DateTime)

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.created = datetime.utcnow()

    def is_valid(self):
        if self.title and self.body and self.created:
            return True
        else:
            return False

@app.route('/')
def index():
    return redirect('/blog')

@app.route('/blog')
def blog_index():
    blog_id = request.args.get('id')
    blogs = Blog.query.all()

    if blog_id:
        post = Blog.query.get(blog_id)
        blog_title = post.title
        blog_body = post.body
        return render_template('entry.html', title="Blog Entry #" + blog_id, blog_title=blog_title, blog_body=blog_body)

    sort = request.args.get('sort')

    if (sort=="newest"):
        blogs = Blog.query.order_by(Blog.created.desc()).all()
    elif (sort=="oldest"):
        blogs = Blog.query.order_by(Blog.created.asc()).all()
    else:
        blogs = Blog.query.all()
    return render_template('blog.html', title="Build A Blog", blogs=blogs)

@app.route('/post')
def new_post():
    return render_template('post.html', title="Add New Blog Entry")

@app.route('/post', methods=['POST'])
def verify_post():
    blog_title = request.form['title']
    blog_body = request.form['body']
    title_error = ''
    body_error = ''

    if blog_title == "":
        title_error = "Title required."
    if blog_body == "":
        body_error = "Content required."

    if not title_error and not body_error:
        new_blog = Blog(blog_title, blog_body)
        db.session.add(new_blog)
        db.session.commit()
        blog = new_blog.id
        return redirect('/blog?id={0}'.format(blog))
    else:
        return render_template('post.html', title="Add New Blog Entry", blog_title = blog_title, blog_body = blog_body, title_error = title_error, body_error = body_error)

if __name__ == '__main__':
    app.run()
