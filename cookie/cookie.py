from flask import Flask , render_template , redirect , make_response , url_for , request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('setcookie.html')

@app.route('/setcookie',methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form.get('uname')
        #pwd = request.form.get('pwd')
        resp = make_response(render_template('getcookie.html'))
        resp.set_cookie('uid',user)
        #resp.set_cookie('pwd',pwd)
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('uid')
    #name1 = request.cookies.get('pwd')
    return '<h1> Welcome to cookies '+ name + '</h1>'

if __name__ =='__main__':
    app.run(debug=True)
