from flask import Flask,render_template,request,send_from_directory,flash,url_for,redirect
import cv2
import numpy as np
import imutils
import easyocr




COUNT = 0
app = Flask(__name__)


app.secret_key = 'dont tell anyone'
@app.route('/')
def index():
   return render_template('layout.html')


@app.route("/home",methods=['POST'])
def home():
    global COUNT
    
    img = request.files['image']

    img.save('images/{}.jpg'.format(COUNT))
    img_arr = cv2.imread('images/{}.jpg'.format(COUNT))

    
    
    gray = cv2.cvtColor(img_arr, cv2.COLOR_BGR2GRAY)

    bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(bfilter, 30, 200)

    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
        

    mask = np.zeros(gray.shape, np.uint8)
    #new_img = request.files['image']

    #new_img.save('new_images/{}.jpg'.format(COUNT))

    #new_image = cv2.imread('new_images/{}.jpg'.format(COUNT))
    #new_image = np.array(new_image)
    #new_image = new_image.astype("float32") / 255.0
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(img_arr, img_arr, mask=mask)

    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2 + 1, y1:y2 + 1]

    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)
    #res = request.files['image']

    text = result[0][-2]
    font = cv2.FONT_HERSHEY_SIMPLEX
    res = cv2.putText(img_arr, text=text, org=(approx[0][0][0], approx[1][0][1] + 60), fontFace=font, fontScale=1,
                      color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    res = cv2.rectangle(img_arr, tuple(approx[0][0]), tuple(approx[2][0]), (0, 255, 0), 3)

    flash(text)

    #res.save('images/{}.jpg'.format(COUNT))
    #res = cv2.imread('images/{}.jpg'.format(COUNT))
    COUNT += 1


    return render_template("car.html")
    

@app.route('/load_img')
def load_img():
    global COUNT 

    return send_from_directory('images',"{}.jpg".format(COUNT-1))



if __name__=="__main__":
   app.run(debug=True)