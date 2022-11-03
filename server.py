
from unicodedata import name
from flask import Flask , redirect,url_for

app = Flask(__name__)

@app.route('/admin')
def admin():
    return "occhev entra admin uu"
@app.route('/guest/<name>')
def guest(name):
    if name!="admin":
        return "kottha ga occhav entra %s"% name
    
    return redirect(url_for('admin'))
@app.route('/user/<name>')
def check(name):
    if name=='admin':
        return redirect (url_for('admin'))
    else:
        return redirect(url_for('guest',name=name))
if __name__=="__main__":
    app.debug=True
    app.run(port=5000)
