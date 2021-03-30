from flask import Flask, render_template,request,session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail                 
from datetime import datetime
from logging.config import dictConfig
from werkzeug import secure_filename
import json
import os
import math

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
    
})


with open('config.json', 'r') as c:
    params = json.load(c)["params"]

local_server = True
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = params['upload_location']
app.secret_key = 'super-secret-key'
app.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD = params['gmail-password']
)
mail = Mail(app)

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)

class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    phone_no = db.Column(db.String(15), nullable=False)
    msg = db.Column(db.String(25), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    
 
class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    slug = db.Column(db.String(20), nullable=False)
    img_file = db.Column(db.String(12), nullable=False)
    tag_line = db.Column(db.String(25), nullable=False)




@app.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last = math.floor(len(posts)/int(params['no_of_posts']))
    # [0:params['no_of_posts']]
    # posts = posts[]
    page = request.args.get('page')
    if (not str(page).isnumeric()):
        page = 1
    page=int(page)
    # post page slicing
    posts = posts[(page-1)*int(params['no_of_posts']): (page-1)*int(params['no_of_posts']) + int(params['no_of_posts'])]
    
    # pagination logic
    # first page 
    if (page==1):
        prev = "#"
        next = "/?page=" + str(page+1)
    # last page
        print(request.method)
    elif (page==last):
        prev = "/?page=" + str(page-1)    
        next="#"
    # middle 
    else:
        prev = "/?page=" + str(page-1)
        next = "/?page=" + str(page+1)
    

    return render_template('index.html', params=params, posts=posts, prev=prev, next=next)

@app.route("/about")
def about():
    return render_template('about.html', params=params)


@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('nm')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name=name, email=email, phone_no=phone, msg=message)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name, 
                         sender=email,
                         recipients=[params['gmail-user']],
                         body = message + "\n" + phone)
        flash("Thanks fo submitting your details.", "success")
        
    return render_template('contact.html', params=params)



@app.route("/post/<string:post_slug>", methods=['GET'])
def post_route(post_slug):
    post = Posts.query.filter_by(slug=post_slug).first()
    return render_template('post.html', params=params, post=post)

@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    app.logger.info('%s logged in successfully')
    if "user" in session and session['user'] == params['admin_user']:
        posts = Posts.query.all()
        return render_template("dashboard.html", params=params, posts=posts)

    if request.method=="POST":
        username = request.form.get("uname")
        userpass = request.form.get("pass")
        if username == params['admin_user'] and userpass == params['admin_password']:
          
            # set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template("dashboard.html", params=params, posts=posts)

    else:
        print("request method post")
        return render_template("login.html", params=params)

       
@app.route("/edit/<string:sno>", methods = ['GET', 'POST'])
def edit(sno):
    if ('user' in session and session['user'] == params['admin_user']):
        # print("hello",request.method)
        if request.method=="POST":
            # print("hiii")
            title = request.form.get('title')
            content = request.form.get('content')
            date = datetime.now()
            slug = request.form.get('slug')
            img_file = request.form.get('img_file')
            tline = request.form.get('tline')
           
            # print("yes")

            if sno=='0':
                # print("no")
                post = Posts(title=title, content=content, date=date, slug=slug, img_file=img_file, tag_line=tline)
                db.session.add(post)
                db.session.commit()
            else:
                post = Posts.query.filter_by(sno=sno).first()
                post.title = title
                post.content = content
                post.date = date
                post.slug = slug
                post.img_file = img_file
                post.tag_line = title
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html', params=params, post=post, sno=sno)

@app.route("/delete/<string:sno>", methods=['GET', 'POST'])
def delete(sno):
    if 'user' in session and session['user']==params['admin_user']:
        post = Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')



@app.route("/uploader", methods = ['GET', 'POST'])
def uploader():
    if ('user' in session and session['user'] == params['admin_user']):
        print("hii")
        if request.method=='POST':
            print("hello")
            f=request.files['file1']
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

            return "Uploaded Successfully"

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')



if __name__ == '__main__':
    app.run(debug=True)     
