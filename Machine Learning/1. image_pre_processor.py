#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image, ImageEnhance
from pathlib import Path
import matplotlib.pyplot as plt
import uuid
import random
import os


# In[2]:


def resize(image, size):
    return image.resize(size)

def rotate(image, degrees):
    return image.rotate(degrees)

def color(image, factor):
    enhancer = ImageEnhance.Color(image)
    return enhancer.enhance(factor)

def contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)

def brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)

def sharpen(image, factor):
    enhancer = ImageEnhance.Sharpness(image)
    return enhancer.enhance(factor)

def save(image, path):
    return image.save(path, "PNG")


# In[3]:


def synthesize_images(inputPath, outputPath, folders, rotations, multiplier, ColorMin, ColorMax, ContrastMin, ContrastMax, 
                     BrightnessMin, BrightnessMax, SharpenMin, SharpenMax):
    for f in folders:
        input_image_list = Path(inputPath + f + '/').glob('*')
        
        outputFolderPath = outputPath + f + '/'
        if not os.path.exists(outputFolderPath):
            os.makedirs(outputFolderPath)
                    
        for path in input_image_list:
            i = Image.open(path)
            
            for r in rotations:
                for m in range(multiplier):
                    color_factor = random.uniform(ColorMin, ColorMax)
                    contrast_factor = random.uniform(ContrastMin, ContrastMax)
                    brightness_factor = random.uniform(BrightnessMin, BrightnessMax)
                    sharpen_factor = random.uniform(SharpenMin, SharpenMax)
                    
                    i = resize(i, new_size)
                    i = rotate(i, r)
                    i = color(i, color_factor)
                    i = contrast(i, contrast_factor)
                    i = brightness(i, contrast_factor)
                    i = sharpen(i, sharpen_factor)
                    
                    save(i, outputFolderPath + str(uuid.uuid4()) + '.png')
                    print('.', end='')


# In[4]:


def create_train_validate_list(folders, outputPath):
    allImages = []    
    for f in folders:
        for p in Path(outputPath + f + '/').glob('*.png'):
            allImages.append(str(p))    
    random.shuffle(allImages)
    
    valLen = int(len(allImages)/4)
    trainLen = len(allImages) - valLen
    trainImg = allImages[:trainLen]
    valImg  = allImages[1-valLen-1:]
    
    f = open(outputPath + "train_lst.lst", "w+")
    x = 0
    for i in trainImg:
        x = x + 1
        if 'notpenguin' in i:
            f.write("%i\t0\t%s\n" % (x, i))
        else:
            f.write("%i\t1\t%s\n" % (x, i))
    f.close()
    
    f = open(outputPath + "validation_lst.lst", "w+")
    x = 0
    for i in valImg:
        x = x + 1
        if 'notpenguin' in i:
            f.write("%i\t0\t%s\n" % (x, i))
        else:
            f.write("%i\t1\t%s\n" % (x, i))
    f.close()


# In[5]:


def main():
    
    print("'\n',Downloading images complete.",'\n')
    
    print("Images Transformation Started.",'\n')
    
    synthesize_images(inputPath, outputPath, folders, rotations, multiplier, ColorMin, ColorMax, ContrastMin, ContrastMax, 
                     BrightnessMin, BrightnessMax, SharpenMin, SharpenMax)
                       
    print("Images Successfully Transformed.",'\n')
    
    print("Training Validation List Creation Started.",'\n')
    
    # Make a list of training and validation image file locations from o/p folder.
    create_train_validate_list(folders, outputPath)
    
    print("Training Validation List complete.",'\n')


# In[6]:


if __name__ == '__main__':
    
    # Define input and output folder paths. Along with path, folder names are also defined.    
    inputPath = './input_images/'
    outputPath = './output_images/'
    folders = ['penguin', 'notpenguin']
    
    # Define range of values for transformation variables.
    new_size=(224,224)
    rotations = [0,90,180,270]
    ColorMin, ColorMax = (0.8, 1.2)
    ContrastMin, ContrastMax = (0.8, 1.2)
    BrightnessMin, BrightnessMax = (0.8, 1.2)
    SharpenMin, SharpenMax = (0.8, 1.2)
    multiplier = 5
    
    print("Starting to download images.",'\n')
    get_ipython().system('aws s3 cp s3://abcdefghijklmn/raw-images/ ./input_images/ --recursive')
            
    main()
    
    print("Starting to upload images.",'\n')    
    get_ipython().system('aws s3 cp ./output_images s3://abcdefghijklmn/processed-images/output_images/ --recursive')
    
    print("Upload Complete.",'\n')


# In[ ]:




