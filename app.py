from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST', 'GET'])
def encode():
    if request.method == 'POST':
        text = request.form.get('text1')
        uploadfile = request.form.get('uploadfile')
        uploadimage = request.form.get('uploadimage')
        
    return render_template('signinpage.html')


@app.route('/', methods = ['POST', 'GET'])
def decode():
    if request.method == 'POST':
        inputimage = request.form.get('inputimage')

        
    return render_template('signinpage.html')