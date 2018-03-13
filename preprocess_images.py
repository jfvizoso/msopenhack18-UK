import os
import sys
from PIL import Image
import math
import numpy as np

def normalize(arr):    
    arr = arr.astype('float')    # Do not touch the alpha channel    
    for i in range(3):        
        minval = arr[...,i].min()        
        maxval = arr[...,i].max()        
    if minval != maxval:            
        arr[...,i] -= minval            
        arr[...,i] *= (255.0/(maxval-minval))    
    return arr

def get_image(path, img_width, img_height):
    img = Image.open(path)
    width = img.size[0]
    height = img.size[1]
    max_dim = max(width, height)
    padded_img = Image.new("RGB", (max_dim, max_dim))
    padded_img.paste(img, ((max_dim-width)//2, (max_dim-height)//2))

    resized_img = padded_img.resize((img_width, img_height))
    img = normalize(np.array(resized_img))
    return img

def preprocess_images(path, img_width=128, img_height=128):
    image_count = -1
    category_id = -1

    for category in os.scandir(path):
        if category.is_dir():
            for image in os.scandir(category.path):
                if (os.path.isfile(image.path)):
                    image_count += 1

    images = np.empty((image_count+1, img_width, img_height, 3))
    image_categories = np.empty((image_count+1))

    image_count = -1
    for category in os.scandir(path):
        if category.is_dir():
            category_id += 1
            # images[category_id] = np.array([])
            for image in os.scandir(category.path):
                if (os.path.isfile(image.path)):
                    image_count += 1
                    im = get_image(image.path, img_width, img_height)
                    images[image_count, :, :, :] = im 
                    image_categories[image_count] = category_id

    np.save('images.npy', images) 
    np.save('image_categories.npy', image_categories)     


def main(argv):
    preprocess_images(argv[1])
    

if __name__ == "__main__":
    if len(sys.argv) >1:
        main(sys.argv)
    else:
        print ("Usage: python preprocess_images.py PATH")
        print ("PATH: path to the folder containing the images.")
