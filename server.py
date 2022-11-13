
from cProfile import run
from unicodedata import name
from flask import Flask , redirect , url_for , request

app = Flask(__name__) 

@app.route('/admin')
def admin():
    return "occhev entra admin uu"

@app.route('/guest/<guestname>')
def guest(guestname):
    if guestname!="admin":
        return "kottha ga occhav entra %s"% guestname
    
    return redirect(url_for('admin'))

@app.route('/user/<name>')
def check(name):
    if name == 'admin':
        return redirect (url_for('admin'))
    else:
        return redirect(url_for('guest',guestname=name))
    
@app.route('/welcome/<welcomename>')
def welcome(welcomename):
    return "welcome ra %s" %welcomename

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['uname']
        return redirect(url_for('welcome',welcomename=user)) 
    else: 
        user = request.args.get('uname')
        return redirect(url_for('welcome',welcomename=user))
    
if __name__=="__main__":
    app.debug=True
    app.run(port=5000) 
   
