from django.shortcuts import render
from keras.layers import Input
import io
import cv2
import numpy
import imutils
import tensorflow as tf
import numpy as np
from keras.applications.vgg16 import preprocess_input
from PIL import Image
from keras_preprocessing.image import load_img


def is_grey_scale(img_path):
    img = Image.open(img_path).convert('RGB')
    w,h = img.size
    for i in range(w):
        for j in range(h):
            r,g,b = img.getpixel((i,j))
            if r != g != b:
                return False
    return True

def convert_img_to_batch_opencv(my_img):
    img = cv2.imread(my_img)
    if img is None:
        print("Error: Image not loaded")
        return None
    img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # threshold the image, then perform a series of erosions +
    # dilations to remove any small regions of noise
    thresh = cv2.threshold(gray, 45, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=2)
    # find contours in thresholded image, then grab the largest one
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    c = max(cnts, key=cv2.contourArea)
    # find the extreme points
    extLeft = tuple(c[c[:, :, 0].argmin()][0])
    extRight = tuple(c[c[:, :, 0].argmax()][0])
    extTop = tuple(c[c[:, :, 1].argmin()][0])
    extBot = tuple(c[c[:, :, 1].argmax()][0])
    # add contour on the image
    img_cnt = cv2.drawContours(img.copy(), [c], -1, (0, 255, 255), 4)
    # add extreme points
    img_pnt = cv2.circle(img_cnt.copy(), extLeft, 8, (0, 0, 255), -1)
    img_pnt = cv2.circle(img_pnt, extRight, 8, (0, 255, 0), -1)
    img_pnt = cv2.circle(img_pnt, extTop, 8, (255, 0, 0), -1)
    img_pnt = cv2.circle(img_pnt, extBot, 8, (255, 255, 0), -1)
    # crop
    ADD_PIXELS = 0
    new_img = img[extTop[1] - ADD_PIXELS:extBot[1] + ADD_PIXELS, extLeft[0] - ADD_PIXELS:extRight[0] + ADD_PIXELS].copy()
    img = cv2.resize(new_img, dsize=(224, 224), interpolation=cv2.INTER_CUBIC)
    img = preprocess_input(img)
    img = np.array([img])
    return img


def predict_tumor(img):
    model = tf.keras.models.load_model('scane/models/2019-06-07_VGG_model.h5')
    img_arr = convert_img_to_batch_opencv(img)
    if img_arr is None:
        print("Error: Image not loaded")
        return None
    predictions = model.predict(img_arr)
    predictions = [1 if x > 0.67 else 0 for x in predictions]
    if predictions[0] == 1:
        return 1
    else:
        return 0

def compare_2_model(res1, res2):
    CATEGORIES = ["glioma_tumor", "meningioma_tumor", "no_tumor", "pituitary_tumor"]
    if (res2 == 2 and res1 == 1):
        return "There is a suspicion that you have a tumor and you must go to the doctor "
    elif (res2 == 0 and res1 == 0):
        return "There is a suspicion that you have a {} tumor and you must go to the doctor ".format(CATEGORIES[res2])
    elif (res2 == 1 and res1 == 0):
        return "There is a suspicion that you have a {} tumor and you must go to the doctor ".format(CATEGORIES[res2])
    elif (res2 == 2 and res1 == 0):
        return "healthy"
    elif (res2 == 3 and res1 == 0):
        return "There is a suspicion that you have a {} tumor and you must go to the doctor ".format(CATEGORIES[res2])
    else:
        return "you have a {} tumor and you must go to the doctor ".format(CATEGORIES[res2])

def Radiology_Diagnostics(request):
 
    if request.method == "POST" and request.FILES['myfile']:
      try:
        my_f = request.FILES["myfile"].read()
        image = Image.open(io.BytesIO(my_f))
        opencvImage_model_1 = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
        res1 = predict_tumor(opencvImage_model_1)
        opencvImage_model_2 = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2GRAY)
        # Check the size of the input image
        size = opencvImage_model_2.size
        if size[0] < 150 or size[1] < 150:
          # Resize the image to the largest possible size that is still at least 150x150
          new_size = (min(size[0], 150), min(size[1], 150))
          opencvImage_model_2 = cv2.resize(opencvImage_model_2, new_size)
        X = opencvImage_model_2.reshape((150, 150, 1))
        X = X / 255.0
        x = np.array([X])
        mymodel = tf.keras.models.load_model('scene/models/mod2.h5')
        predictions = mymodel.predictclasses(X)
        res2 = predictions[0]
        fin_res = compare_2_model(res2, res1)
        print(fin_res)
        context = { "fin_re": fin_res , "test":"test" }
        return render(request, 'scane/show_res.html' , context)
      except:
        print("error occurs ya jo")
   
    return render(request, 'scane/Radiology_Diagnostics.html')


load_img = "C:/Users/future/Desktop/test/Y1.jpg"

res1 = predict_tumor(load_img)

mymodel = tf.keras.models.load_model('scane/models/mod2.h5')
X = cv2.imread(load_img, 0)
X = cv2.resize(X, (150, 150))
X = X.reshape((150, 150, 1))
X = X/255.0
X = np.array([X])
predictions = mymodel.predict_step(X)
res2 = np.argmax(predictions)

def compare_2_model(res1, res2):
    CATEGORIES = ["glioma_tumor", "meningioma_tumor", "no_tumor", "pituitary_tumor"]
    if (res2 == 2 and res1 == 1):
        return "There is a suspicion that you have a tumor and you must go to the doctor "
    elif (res2 == 0 and res1 == 0):
        return "There is a suspicion that you have a {} tumor and you must go to the doctor ".format(CATEGORIES[res2])
    elif (res2 == 1 and res1 == 0):
        return "There is a suspicion that you have a {} tumor and you must go to the doctor ".format(CATEGORIES[res2])
    elif (res2 == 2 and res1 == 0):
        return "healthy"
    elif (res2 == 3 and res1 == 0):
        return "There is a suspicion that you have a {} tumor and you must go to the doctor ".format(CATEGORIES[res2])
    else:
        return "you have a {} tumor and you must go to the doctor ".format(CATEGORIES[res2])

print(compare_2_model(res2, res1))




def show_res(request):
    print(compare_2_model(res2, res1))

    return render(request, 'scane/show_res.html')
