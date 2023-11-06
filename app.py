from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
import cv2
import scipy
import numpy as np
import imageio.v2 as iio
from PIL import Image, ImageTk
import scipy.fftpack
import math
import pandas as pd
import seaborn as sns
import asyncio

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')

save_folder = os.path.join('static', 'saveimages')

save_folder_histogram = os.path.join('static', 'histogram')

def create_histogram(img):
    assert len(img.shape) == 2 # check grayscale image
    histogram = [0] * 256 # list of intensity frequencies, 256 zero values
    for row in range(img.shape[0]): # traverse by row (y-axis)
        for col in range(img.shape[1]): # traverse by column (x-axis)
            histogram[img[row, col]] += 1
    return histogram
def visualize_histogram(histogram, output='static\\histogram\\histogram.png'):
    hist_data = pd.DataFrame({'intensity': list(range(256)), 'frequency': histogram})
    sns_hist = sns.barplot(x='intensity', y='frequency', data=hist_data, color='blue')
    sns_hist.set(xticks=[]) # hide x ticks
    
    fig = sns_hist.get_figure()
    fig.savefig(output)
    return output

app.config['UPLOAD'] = upload_folder
app.config['SAVE'] = save_folder
app.config['HISTOGRAM'] = save_folder_histogram
@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

@app.route('/histogram', methods=['GET', 'POST'])
def histogram():
    if request.method == 'POST':
        file = request.files['img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD'], filename))
        img = os.path.join(app.config['UPLOAD'], filename)
        path = os.getcwd() +"\\"+ img
        img_1 = cv2.imread(path)
        img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2RGB)
        img_gray = cv2.cvtColor(img_1, cv2.COLOR_RGB2GRAY)
        grayscale_img = Image.fromarray(img_gray)
        grayscale_img.save(os.path.join(app.config['SAVE'], 'grayscale_'+filename))
        new_img_2 = cv2.equalizeHist(img_gray)

        histogram = create_histogram(img_gray)
        hist_img_path = visualize_histogram(histogram, output=os.path.join(app.config['HISTOGRAM'], 'histogram_' + filename))

        histogram_after_process = create_histogram(new_img_2)
        hist_img_path = visualize_histogram(histogram_after_process,output=os.path.join(app.config['HISTOGRAM'], 'histogram_after_' + filename))
        iml = np.asarray(img_gray)

        bl = iml.flatten()

        hist, bins = np.histogram(iml, 256, [0,255])

        cdf = hist.cumsum()

        cdf_m = np.ma.masked_equal(cdf, 0)

        num_cdf_m = (cdf_m-cdf_m.min())*255
        den_cdf_m = (cdf_m.max() - cdf_m.min())
        cdf_m = num_cdf_m/den_cdf_m

        cdf = np.ma.filled(cdf_m,0).astype('uint8')

        im2 = cdf[bl]
        
        im3 = np.reshape(im2, iml.shape)
        new_img = Image.fromarray(im3)
        

        original_pic = os.path.join(app.config['SAVE'], 'grayscale_'+filename)
        new_filename ='after_histogram_' + filename 
        new_img.save(os.path.join(app.config['SAVE'],new_filename))
        img_show = os.path.join(app.config['SAVE'], new_filename)
        histogram_before_show = os.path.join(app.config['HISTOGRAM'], 'histogram_' + filename)
        histogram_after_show = os.path.join(app.config['HISTOGRAM'], 'histogram_after_' + filename)
        return render_template('histogram_image_render.html',original_pic=original_pic ,img_show=img_show, histogram_after_show=histogram_after_show, histogram_before_show=histogram_before_show)
    return render_template('histogram_image_render.html')
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost',5000,app)