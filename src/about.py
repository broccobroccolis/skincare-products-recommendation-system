#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 22:04:49 2022

@author: wanwoeichyi
"""

import streamlit as st
from PIL import Image


def app():
    st.subheader("""About Skin O'Clock""")
    st.write("Skin O'Clock is a web-based application which can help the target audience get recommendations on skincare products for their desired category.")
    st.write("Skin O'Clock targets to serve users who are members of Sephora, a globally known cosmetics e-Commerce platform, as our application is built using customers' and products' data of Sephora.")
    
    st.write("")
    st.subheader("Dataset Information")
    st.write("Dataset used include can be accessed via https://raw.githubusercontent.com/broccobroccolis/skinoclock/main/skindataall_1412.csv.")
    
    st.write("")
    st.subheader("Source Code")
    st.write("Complete source codes and dataset can be obtained at https://github.com/broccobroccolis/skinoclock.")
    
    st.write("")
    st.subheader("Further Enquiries")
    st.write("To know more information, to comment on the project or just to connect, feel free to reach me via my email at woeichyi_wan@outlook.com.")
    
    
    
    
 