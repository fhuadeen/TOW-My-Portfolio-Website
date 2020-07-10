# import flask library
from flask import Flask
from flask import render_template # use for returning templates rather than just a string
# from data import Articles
from flask import flash # for flash messaging
from flask import redirect # to handle redirection
from flask import url_for, session, logging
#from flask_mysqldb import MySQL
#from wtforms import Form, StringField, TextAreaField, PasswordField, validators # for creating forms
#from passlib.hash import sha256_crypt # to encrypt password

app = Flask(__name__)

# Articles = Articles() # bring in articles function from data.py

app.debug = True # so we don't have to be reloading server every time we make a change


# to create a route to avoid 'not found' in browser
@app.route('/')
def index():
    return render_template('home.html') # route to home page

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html') # route to portfolio page

@app.route('/articles')
def articles():
    return redirect('https://medium.com/@fhuadeen') # route to articles page

@app.route('/resume')
def resume():
    return redirect('https://docs.google.com/document/d/1TIAc04c7enmQ39nAv9KypNIMfSfzNhEh7uiyiSjQyUI/edit?usp=sharing') # route to articles page

# run the application
if __name__ == '__main__':
    app.run()
