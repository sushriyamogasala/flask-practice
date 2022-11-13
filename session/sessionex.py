from flask import Flask , session , render_template , request , url_for,make_response , redirect
import os
app = Flask(__name__)


app.secret_key = 'secret ga unchali anta?/*&^%'

@app.route('/')
def index():
    if 'username' in session:
        username = session['username'] 
        return "Logged in as "+ username +'<br>'+ "<b><a href = '/logout' >Click here to get out </a> </b> "
    return "You aren't logged in <br> <a href = '/login' >Click here to come inside</a>"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['uname']
        return redirect(url_for('index'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)



        