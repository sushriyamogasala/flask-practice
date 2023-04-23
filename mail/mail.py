from flask import Flask,redirect,url_for,render_template,session,make_response,g
from flask_mail import Mail,Message

app = Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'sushriya1009@gmail.com'
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/')
def index():
    msg = Message('Hello',sender='sushriya1009@gmail.com',recipients=['m.ramakrishna1512@gmail.com'])
    msg.body = "Hello RK! This msg is sent from Flask-Mail"
    mail.send(app)
    return "Message sent"

if __name__=='__main__':
    app.run(debug=True)
