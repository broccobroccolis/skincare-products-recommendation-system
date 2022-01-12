#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 21:50:37 2022

@author: wanwoeichyi
"""
import streamlit as st
from PIL import Image


def app():
    st.header("""Skincare Products Recommendation Engine""")
    st.markdown("WIH3001 Data Science Project")
    st.markdown("Prepared by Wan Woei Chyi (17205866/1)")
    image = Image.open('/Users/wanwoeichyi/Desktop/WIH3001 DS fyp/img/skincare.jpeg')
    st.image(image)
    
    st.sidebar.caption("Navigate through the pages to explore more!")
    st.write("")
    st.write("")
    with st.container():
        col1, col2, col3 = st.columns([1,1,1])
        col1.metric("Total Products", "315")
        col2.metric("Total Users", "5334")
        col3.metric("Total Reviews", "5784")