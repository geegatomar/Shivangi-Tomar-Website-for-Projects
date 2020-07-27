from flask import Flask, render_template, redirect, url_for, request, send_file
from generate_random_image import Generate
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def projects():
    return render_template('about.html')

@app.route('/cat_dog_classifier')
def catsdogs():
    return render_template('cat_dog_classifier.html')

@app.route('/captcha_breaker_basic')
def captchabasic():
    return render_template('captcha_breaker_basic.html')

@app.route('/get_image')
def getimg():
    image_file = Generate.image()
    #return image
    return send_file(image_file, mimetype='image')


if __name__ == "__main__":
    app.run(debug=True)
