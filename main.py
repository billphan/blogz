from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from hashutils import make_pw_hash, check_pw_hash

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'as8d7f98a!@qw546era#$#@$'
db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.Text)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pub_date = db.Column(db.DateTime)

    def __init__(self, title, body, owner, pub_date=None):
        self.title = title
        self.body = body
        self.owner = owner
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True)
    pw_hash = db.Column(db.String(120))
    blogs = db.relationship('Blog', backref='owner')

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pw_hash(password)

@app.before_request
def require_login():
    allowed_routes = ['login', 'signup', 'blog', 'index', 'static']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)













@app.route('/login', methods=['POST','GET'])
def login():
    username_error = ""
    password_error = ""

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_pw_hash(password, user.pw_hash):
            if password != user.password:
                return render_template('login.html', password_error="Your username or password was incorrect.")
            elif password == user.password:
                session['username'] = username
                return redirect('/newpost')
        return render_template('login.html', username_error="Your username or password was incorrect.")

    return render_template("login.html")











@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        verify = request.form["verify"]
        exist_error = User.query.filter_by(username=username).first()

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
        else: # Validate existing username.
            if exist_error:
                username_error = "Username already taken. Please try another."
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
            return redirect("/newpost")
        else:
            return render_template('signup.html',
                username = username,
                password = password,
                verify = verify,
                username_error = username_error,
                password_error = password_error,
                verify_error = verify_error
        )

    return render_template('signup.html')

@app.route('/blog', methods=['POST', 'GET'])
def blog():
    blog_id = request.args.get('id')
    user_id = request.args.get('userid')
    posts = Blog.query.all()

    if blog_id:
        post = Blog.query.filter_by(id=blog_id).first()
        return render_template("post.html", title=post.title, body=post.body, user=post.owner.username, pub_date=post.pub_date, user_id=post.owner_id)
    if user_id:
        entries = Blog.query.filter_by(owner_id=user_id).all()
        return render_template('user.html', entries=entries)

    return render_template('blog.html', posts=posts)

@app.route('/newpost')
def post():
    return render_template('newpost.html', title="New Post")

@app.route('/newpost', methods=['POST', 'GET'])
def newpost():
    title = request.form['title']
    body = request.form["body"]
    owner = User.query.filter_by(username=session['username']).first()
    title_error = ""
    body_error = ""

    if title == "":
        title_error = "Title required."
    if body == "":
        body_error = "Content required."

    if not title_error and not body_error:
        new_post = Blog(title, body, owner)
        db.session.add(new_post)
        db.session.commit()
        page_id = new_post.id
        return redirect("/blog?id={0}".format(page_id))
    else:
        return render_template("newpost.html",
            title = title,
            body = body,
            title_error = title_error,
            body_error = body_error
        )

@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')

if __name__ == '__main__':
    app.run()
