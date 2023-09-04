import os
from flask import Flask, request, render_template

app = Flask(__name__)

upload_folder = "uploads"
app.config['upload_folder'] = upload_folder

@app.route('/upload', methods=['GET'])
def get_upload():
    return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def post_upload():
    if "image" not in request.files:
        return "No file path"
    
    file = request.files['image']

    if file.filename == "":
        return "No selected file"
    
    if file:
        filename = os.path.join(app.config['upload_folder'], file.filename)
        file.save(filename)
        return f"File uploaded successfully <a href='/upload/{file.filename}'> View Image </a>"
    


@app.route('/', methods = ['GET'])
def get_home():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(
        debug = True,
        host = "0.0.0.0"
    )