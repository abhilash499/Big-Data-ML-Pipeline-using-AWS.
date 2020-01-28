#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, request, redirect
import os
from PIL import Image
from werkzeug.utils import secure_filename
import base64
import requests
import json


# In[2]:


app = Flask(__name__)


# In[3]:


target = os.path.join(os.getcwd(), "static", "images")
if not os.path.isdir(target):
    os.mkdir(target)


# In[ ]:


@app.route('/', methods=['GET','POST'])
def my_application():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        
        file = request.files['file']
        filename = secure_filename(file.filename)

        file.save(os.path.join(target, filename))

        im_temp = Image.open(os.path.join(target, filename))
        newsize = (224, 224)
        im_process = im_temp.resize(newsize)
        im_process.save(os.path.join(target, filename))
        display(im_process)
       
        image_source = os.path.join(target, filename)
        print(image_source)
        
        with open(os.path.join(target, filename), 'rb') as image_file:
            encoded_string = base64.b64encode(image_file.read())
            encoded_string_utf8 = encoded_string.decode('utf-8')
        
        data = encoded_string_utf8       
        response = requests.post(url = 'https://cqzjto89w6.execute-api.us-east-1.amazonaws.com/image-classifier-api', data = data)
        
        print('response received from API')
        
        if response.status_code == 200:
            result = json.loads(response.content.decode('utf-8'))
        else:
            result = response
            
        return render_template('result.html', image_source = image_source, result=result)


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




