#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 22:04:49 2022

@author: wanwoeichyi
"""

import streamlit as st
from PIL import Image
import webbrowser


def app():
    st.subheader("""About Skin O'Clock ✨  """)
    st.write("Skin O'Clock is a web-based application which can help the target audience get recommendations on skincare products for their desired category.")
    st.write("Skin O'Clock targets to serve users who are members of Sephora, a globally known cosmetics e-Commerce platform, as our application is built using customers' and products' data of Sephora.")
    
    st.write("")
    st.subheader("Dataset Information 📊  ")
    st.write("Dataset used can be accessed at https://raw.githubusercontent.com/broccobroccolis/skinoclock/main/skindataall_1412.csv.")
    
    st.write("")
    st.subheader("Source Code 💻  ")
    st.write("Complete source codes and dataset can be accessed at https://github.com/broccobroccolis/skinoclock.")
    
    st.write("")
    st.subheader("Documentation 📑  ")
    st.write("Detailed documentation can be accessed at https://drive.google.com/file/d/1Yf-NLtNYLzpYcKlOa748dsLsypyjFyD4/view?usp=sharing.")
    
    st.write("")
    st.subheader("About Author ✍🏻  ")
    with st.container():
        col1, col2 = st.columns([1,4])
        image = Image.open('img/DSC_8752.jpg')
        col1.image(image, width=200)
        
        col2.write("Hello there! I am Wan Woei Chyi, a 3rd year Data Science student from University of Malaya, and definitely a skincare enthusiast! ")
        col2.write("This is the data product of my WIH3001 Data Science Project, Skin O'Clock, a skincare products recommendation system.")
        col2.write("Hope you have fun!")
        col2.write("Feel free to connect with me on LinkedIn via https://www.linkedin.com/in/woeichyi-wan. Cheers! 🙌")
    
    st.write("")
    st.subheader("Further Enquiries 📩  ")
    st.write("To know more information, to comment on the project or just to connect, feel free to reach me via my email at woeichyi_wan@outlook.com.")
    
    
    
    
 
