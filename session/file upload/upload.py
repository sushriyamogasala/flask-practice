from flask import Flask , redirect,url_for,render_template,request,session,make_response
from werkzeug.utils import secure_filename
#from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

app = Flask(__name__)


@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/uploader',methods= ['post','get'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return 'File uploaded successfully'
    
if __name__ == '__main__':
    app.run(debug=True) 
