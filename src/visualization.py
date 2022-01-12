#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:20:02 2022

@author: wanwoeichyi
"""

import streamlit as st
from PIL import Image
import pandas as pd

#from nltk.corpus import stopwords
#from wordcloud import WordCloud, STOPWORDS

def app():
    cleaned_data = pd.read_csv("https://raw.githubusercontent.com/broccobroccolis/skinoclock/main/Cleaned_skindataall.csv")
    df = cleaned_data.copy()
    
    vis_type = st.multiselect("Select the type of visualizations you would like to explore: ", ("Users' Features Distribution","Ingredients Word Cloud"))
    for x in range(0,len(vis_type)):
        if x ==0:
            featuresDistribution(df)
        else:
            ingredientsWordCloud()
            
def featuresDistribution(df):
    st.subheader("Users' Features Distribution")
    features = st.multiselect("Select the features to see the users' distribution': ",("Skin Tone","Skin Type","Eye Color","Hair Color"))
    
    for x in range(0, len(features)):
        if features[x] == "Skin Tone":
            st.caption("Skin Tone: ")
            st.image(Image.open('img/skintone_dis.png'),width=450)
        elif features[x] == "Skin Type":
            st.caption("Skin Type: ")
            st.image(Image.open('img/skintype_dis.png'),width=450)
        elif features[x] == "Eye Color":
            st.caption("Eye Color: ")
            st.image(Image.open('img/eyecolor_dis.png'),width=450)
        elif features[x] == "Hair Color":
            st.caption("Hair Color: ")
            st.image(Image.open('img/haircolor_dis.png'),width=450)
            
        if x == len(features)-1:
                st.success("Above is/are the users' distribution visualization(s) of your selected feature(s).")
        
    
def ingredientsWordCloud():
    #stopwords = set(STOPWORDS)
    #stopwords.update(['read', 'more', 'product'])
    st.subheader("Ingredients Word Cloud")
    category = st.multiselect("Select the product category to view their ingredients list Word Cloud: ",("Cleanser","Toner","Treatment","Moisturizer","Face Mask"))
    
    for x in range(0,len(category)):
        #category_df = df[df.Category == category[x]]
        #category_df2 = " ".join(ing for ing in category_df.Ingredients)
        #generateWordCloud(category_df2)
        
        if category[x] == 'Cleanser':
            st.caption("Cleanser:")
            st.image(Image.open('img/cleanser_wordcloud.png'),width=450)
        elif category[x] == 'Toner':
            st.caption("Toner:")
            st.image(Image.open('img/toner_wordcloud.png'),width=450)
        elif category[x] == 'Treatment':
            st.caption("Treatment:")
            st.image(Image.open('img/treatment_wordcloud.png'),width=450)
        elif category[x] == 'Moisturizer':
            st.caption("Moisturizer:")
            st.image(Image.open('img/moisturizer_wordcloud.png'),width=450)
        elif category[x] == 'Face Mask':
            st.caption("Face Mask:")
            st.image(Image.open('img/facemask_wordcloud.png'),width=450)
        
        if x == len(category)-1:
                st.success("Above is/are the Word Cloud visualization(s) of the ingredients distribution of your selected product category(s).")
        

    
