#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 20:08:55 2022

@author: wanwoeichyi
"""

from PIL import Image
import streamlit as st
from src import homepage, about, rec, info, visualization

from multipage import MultiPage

# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Skin O'Clock")

# Add all your applications (pages) here
app.add_page("Homepage", homepage.app)
app.add_page("Recommendations", rec.app)
app.add_page("Visualizations", visualization.app)
app.add_page("Extra Info", info.app)
app.add_page("About", about.app)

# The main app
app.run()
