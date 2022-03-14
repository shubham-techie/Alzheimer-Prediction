import pylab as p
from flask import Blueprint,render_template,request
from flask_login import login_required, current_user
from . import db
from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import cv2

main=Blueprint('main',__name__)

model=load_model('D:\Shubham\Alzhiemer-Prediction\project\model.h5')
CATEGORIES = ["MildDemented", "ModerateDemented","NonDemented","VeryMildDemented"]

def predict_label(image_name):
    image_path='D:/Shubham/Alzhiemer-Prediction/project/static/alzheimer-images/' +image_name

    image = cv2.imread(image_path, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.array(image)
    image = image.astype('float32')
    image /= 255
    image = np.stack((image,) * 3, axis=-1)
    image = image.reshape(-1, 224, 224, 3)

    result=model.predict(image)
    return result

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/prediction')
# @login_required
def prediction():
    return render_template('prediction.html', name='current_user.name')

@main.route('/prediction', methods=['POST'])
def predict():
    img=request.files['image']
    imgpath='./project/static/alzheimer-images/'+img.filename
    img.save(imgpath)

    p=predict_label(img.filename)
    classes=np.argmax(p)
    print("Disease name ", CATEGORIES[classes])

    return render_template('prediction.html', result=CATEGORIES[classes], image='alzheimer-images/'+img.filename)

