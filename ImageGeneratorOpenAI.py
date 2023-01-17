# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:29:37 2023

@author: HP
"""

import openai
import urllib.request
from PIL import Image
import streamlit as st
import os
from dotenv import load_dotenv

def configure():
  load_dotenv()

configure()


openai.api_key = os.getenv('api_key')

def generate_image(image_description):

  img_response = openai.Image.create(
    prompt = image_description,
    n=1,
    size="512x512")
  

  img_url = img_response['data'][0]['url']

  urllib.request.urlretrieve(img_url, 'img.png')

  img = Image.open("img.png")
  
  return img



# page title
st.title('DALL.E - Image Generation - OpenAI')

# text input box for image recognition
img_description = st.text_input('Image Desription')

if st.button('Generate Image'):
    
    generated_img = generate_image(img_description)
    st.image(generated_img)