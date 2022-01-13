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
        if vis_type[x] == "Users' Features Distribution":
            featuresDistribution(df)
        elif vis_type[x] == "Ingredients Word Cloud":
            ingredientsWordCloud(df)
            
def featuresDistribution(data):
    st.subheader("Users' Features Distribution")
    features = st.multiselect("Select the features to see the users' distribution': ",("Skin Tone","Skin Type","Eye Color","Hair Color"))
    
    for x in range(0, len(features)):
        if features[x] == "Skin Tone":
            st.caption("Skin Tone: ")
            stats = data.groupby('Skin_Tone')['Username'].count().sort_values(ascending=False)
        elif features[x] == "Skin Type":
            st.caption("Skin Type: ")
            stats = data.groupby('Skin_Type')['Username'].count().sort_values(ascending=False)
        elif features[x] == "Eye Color":
            st.caption("Eye Color: ")
            stats = data.groupby('Eye_Color')['Username'].count().sort_values(ascending=False)
        elif features[x] == "Hair Color":
            st.caption("Hair Color: ")
            stats = data.groupby('Hair_Color')['Username'].count().sort_values(ascending=False)
        
        
        fig, ax = plt.subplots(figsize=(12, 6))
        fig = stats.plot.bar()
        ax.set_xticklabels(ax.get_xticklabels(), rotation=360, ha='right')

        st.pyplot(fig=fig.figure, figsize=30)
        
        if x == len(features)-1:
                st.success("Above is/are the users' distribution visualization(s) of your selected feature(s).")

def ingredientsWordCloud(df):
    st.subheader("Ingredients Word Cloud")
    category = st.multiselect("Select the product category to view their ingredients list Word Cloud: ",("Cleanser","Toner","Treatment","Moisturizer","Face Mask"))
        
    for x in range(0,len(category)):
        category_df = df[df.Category == category[x]]
        category_df2 = " ".join(ing for ing in category_df.Ingredients)
        
        if category[x] == 'Cleanser':
            st.caption("Cleanser:")
            generateWordCloud(category_df2)
        elif category[x] == 'Toner':
            st.caption("Toner:")
            generateWordCloud(category_df2)
        elif category[x] == 'Treatment':
            st.caption("Treatment:")
            generateWordCloud(category_df2)
        elif category[x] == 'Moisturizer':
            st.caption("Moisturizer:")
            generateWordCloud(category_df2)
        elif category[x] == 'Face Mask':
            st.caption("Face Mask:")
            generateWordCloud(category_df2)
        
        if x == len(category)-1:
                st.success("Above is/are the Word Cloud visualization(s) of the ingredients distribution of your selected product category(s).")
        
def generateWordCloud(data):
    stopwords = set(STOPWORDS)
    stopwords.update(['read', 'more', 'product'])
    wordcloud = WordCloud(stopwords=stopwords, background_color="white").generate(data)
    
    plt.figure(figsize = (10,2))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)
