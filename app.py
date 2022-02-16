from flask import Flask, flash, redirect, render_template, request
from stegano import encode, decode

UPLOAD_FOLDER = '../static/images'
ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/',methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/encodeForm', methods = ['POST', 'GET'])
def encodeForm():
    if request.method == 'POST':
        print('Ha andar aa gya hu')

        text_data = request.form.get('text1')
        print(text_data)
        # uploadfile = request.form.get('uploadfile')
        uploaded_image = request.files['uploaded_image']

        print(str(uploaded_image))
        
        if uploaded_image.filename == '':
            print('File not selected')
            flash('No file selected!')
            return redirect(request.url)
        
        uimg = "static/images/upload.png"
        uploaded_image.save(uimg)
        encoded_image = encode(uimg, text_data)
        if encoded_image:
            print('Image encoded!')
        else:
            print('huttt')
        encoded_img = "static/images/encoded.png"
        encoded_image.save(encoded_img)
        
        return render_template('index.html')
    return render_template('index.html')


@app.route('/decodeForm', methods = ['POST', 'GET'])
def decodeForm():
    if request.method == 'POST':
        if 'inputimage' not in request.files:
            flash('No image uploaded!')
            return redirect(request.url)

        input_image = request.files['inputimage']

        if input_image.filename == '':
            flash('No file selected!')
            return redirect(request.url)

        decoded_data = decode(input_image)
        
    return render_template('index.html')