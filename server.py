
from flask import Flask

app = Flask(__name__)

@app.route('/admin')
def hw(name):
    return "juyiiiiiiiiiiii  %s"%name

if __name__=="__main__":
    app.debug=True
    app.run(port=5000)
