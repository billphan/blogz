from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import desc

app = Flask(__name__)
app.config['DEBUG'] = True
# connection string info - ://user:password@server:portNumber/databaseName
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'xfd{H\xe5<\xf9\x6a2\xa0\x9fR"\xa1\xa8'

# class for blog database
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1200))
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created = db.Column(db.DateTime)

    def __init__(self, title, body):
        self.title = title
        self.body = body
        self.owner = owner
        self.created = datetime.utcnow()

# class for users database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(120))
    blog = db.relationship("Blog", backref="owner")

    def __init__(self, username, password):
        self.username = username
        self.password = password

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route("/signup", methods=['POST', 'GET'])
def signup():

    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]

    username_error = ""
    password_error = ""
    verify_error = ""

    if username == "": # Validate Username
        username_error = "Please enter a valid username."
    elif len(username) <= 3 or len(username) > 20:
        username_error = "Username must be between 3 and 20 characters long."
        username = ""
    elif " " in username:
        username_error = "Your username cannot contain any spaces."
        username = ""

    if password == "": # Validate Password
        password_error = "Please enter a valid password."
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters long."
    elif " " in password:
        password_error = "Your password cannot contain any spaces."

    if verify == "" or verify != password: # Verify Password
        verify_error = "Passwords do not match. Please try again."
        verify = ""

    if not username_error and not password_error and not verify_error:
        new_user = User(username, password)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = username
        return redirect("/post")
    else:
        return render_template(
            'signup.html',
            username = username,
            username_error = username_error,
            password_error = password_error,
            verify_error = verify_error,)
    return render_template('signup.html')

@app.route("/login", methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        username_error = ""
        password_error = ""

        if user and user.password == password:
            session['username'] = username
            return redirect('/post')
        if not user:
            username = ""
            username_error = "Incorrect Username"
        if password != user.password:
            password = ""
            password_error = "Incorrect Password"
        else:
            return render_template("login.html",
                username = username,
                password = password,
                username_error = username_error,
                password_error = password_error
        )
    return render_template("login.html")

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

@app.route('/logout')
def logout():
    del session['username']
    return redirect('/blog')

if __name__ == '__main__':
    app.run()
