from flask import Flask, render_template , request , url_for , redirect

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('student.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template('result.html',result=result)
    else:
        result = request.args.get
        return render_template('result.html',result=result)
if __name__ == '__main__':
    app.run(debug="True")  
    