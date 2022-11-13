from flask import Flask,render_template , request

app = Flask(__name__)

@app.route('/')

def login():
    return render_template('just.html')

if __name__ == '__main__':
    app.run(debug="True")