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

        text_data = request.form.get('text1', None)
        uploaded_file = request.files['uploaded_file']
        uploaded_image = request.files['uploaded_image']

        if not text_data:
            if uploaded_file.filename == '':
                flash('Enter Text or upload a Text file!')
                return redirect(request.url)
            text_data = uploaded_file.read().decode("utf-8").replace('\n', '')

        if uploaded_image.filename == '':
            flash('No file selected!')
            return redirect(request.url)
        
        if not uploaded_image and allowed_file(uploaded_image.filename):
            flash('File format not supported!')
            return redirect(request.url)
            
        encoded_image = encode(uploaded_image, text_data)
        if encoded_image:
            print('Image encoded!')
        else:
            print('Error')

        encoded_img = "static/images/encoded.png"
        encoded_image.save(encoded_img)

        return render_template('index.html', flag=1)
        
    return render_template('index.html', flag=0)


@app.route('/decodeForm', methods = ['POST', 'GET'])
def decodeForm():
    if request.method == 'POST':
        input_image = request.files['input_image']

        if input_image.filename == '':
            flash('No file selected!')
            return redirect(request.url)

        if not input_image and allowed_file(input_image.filename):
            flash('File format not supported!')
            return redirect(request.url)

        decoded_data = decode(input_image)
        if decoded_data:
            print('Image decoded :)')
        return render_template('index.html', text=decoded_data)    
    return render_template('index.html')