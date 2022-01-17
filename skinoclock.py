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
import hydralit_components as hc

# Create an instance of the app 
#app = MultiPage()

st.set_page_config(layout='wide',initial_sidebar_state='collapsed',)

# Add all your applications (pages) here
#app.add_page("Homepage", homepage.app)
#app.add_page("Recommendations", rec.app)
#app.add_page("Visualizations", visualization.app)
#app.add_page("Extra Info", info.app)
#app.add_page("About", about.app)

# The main app
#app.run()

MENU = {
    "Home" : homepage,
    "Recommendations" : rec,
    "Visualization" : visualization,
    "Extra Info" : info,
    "About" : about,
    
}

def main():

    # specify the primary menu definition
    menu_data = [
        {'icon': "far fa-chart-bar", 'label':"Recommendations"},#no tooltip message
        {'icon': "fas fa-desktop",'label':"Visualization"},
        {'icon': "fas fa-info-circle", 'label':"Info"}, 
        {'icon': "far fa-copy", 'label':"About"},
    
    ]


    over_theme = {'txc_inactive': '#FFFFFF','menu_background':'#DDB6B3'}
    menu_id = hc.nav_bar(
        menu_definition=menu_data,
        override_theme=over_theme,
        home_name='Home',
        hide_streamlit_markers=False, #will show the st hamburger as well as the navbar now!
        sticky_nav=True, #at the top or not
        sticky_mode='pinned', #jumpy or not-jumpy, but sticky or pinned
    )
    
    if menu_id == "Home":
        homepage.app()
    if menu_id == "Recommendations":
        rec.app()
    if menu_id == "Visualization":
        visualization.app()
    if menu_id == "Info":
        info.app()
    if menu_id == "About":
        about.app()


if __name__ == '__main__':
    main()
