#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 20:08:55 2022

@author: wanwoeichyi
"""

import streamlit as st
import pandas as pd
import numpy as np
from surprise import accuracy, Dataset, Reader, NormalPredictor, BaselineOnly, KNNBasic, KNNWithMeans, KNNBaseline, KNNWithZScore, SVD, SVDpp, NMF, SlopeOne, CoClustering
from surprise.model_selection import train_test_split as tts
from collections import defaultdict
from PIL import Image

st.title("Skin O'Clock")
st.header("""Skincare Products Recommendation Engine""")
st.write("WIH3001 Data Science Project")
st.write("Prepared by Wan Woei Chyi (17205866/1)")

image = Image.open('skincare.jpeg')

st.image(image)

cleaned_data = pd.read_csv("https://raw.githubusercontent.com/broccobroccolis/skinoclock/main/Cleaned_skindataall.csv")
df = cleaned_data.copy()

category = st.sidebar.selectbox("Select product category: ",("Cleanser","Toner","Treatment","Moisturizer","Face Mask"))

#skin_tone = st.sidebar.selectbox("Select skin tone: ", ("Light","Fair","Porcelain","Medium","Tan","Olive","Dark","Deep","Ebony"))
#skin_type = st.sidebar.selectbox("Select skin type: ", ("Dry","Normal","Combination","Oily"), index=2)
#eye_color = st.sidebar.selectbox("Select eye color: ", ("Black","Brown","Hazel","Blue","Gray","Green"), index=5)
#hair_color = st.sidebar.selectbox("Select hair color: ", ("Black","Blonde","Brunette","Gray","Auburn","Red"),index=2)

#Modelling recommenders
data = df[['User_id', 'Product_id', 'Rating_Stars']]
reader = Reader(line_format='user item rating', sep=',')
data = Dataset.load_from_df(data, reader=reader)
trainset, testset = tts(data, test_size=0.2, random_state=30)

#Building recommendations
full_trainset = data.build_full_trainset()   #Build on entire data set
algo = SVDpp(n_epochs = 10, lr_all = 0.005, reg_all = 0.4)
algo.fit(full_trainset)
antitestset = full_trainset.build_anti_testset()
predictions = algo.test(antitestset)

#get all predictions sorted
def get_all_predictions(predictions):
    
    # First map the predictions to each user.
    top_n = defaultdict(list)    
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)

    return top_n

all_pred = get_all_predictions(predictions)

#to get top N recommendations
n = 308
for uid, user_ratings in all_pred.items():
    user_ratings.sort(key=lambda x: x[1], reverse=True)
    all_pred[uid] = user_ratings[:n]
tmp = pd.DataFrame.from_dict(all_pred)
tmp_transpose = tmp.transpose()


#get predictions for a user
def get_predictions(user_id,category):
    try:
        results = tmp_transpose.loc[user_id]
    
        recommended_product_ids=[]
        for x in range(0, n):
            recommended_product_ids.append(results[x][0])
        
        df_products = df[['Category','Product', 'Brand','Price','Size','Product_id', 'Ingredients', 'Product_Url']]
        df_products.drop_duplicates(inplace=True)
    
    except KeyError:
        st.warning("Sorry, we can't generate relevant recommendations because your User ID isn't in our database.")
        return None
    except UnboundLocalError:
        st.warning("Sorry, we can't generate relevant recommendations because your User ID isn't in our database.")
        return None

    recommended_product_ids_df = pd.DataFrame(recommended_product_ids, columns=['Product_id'])
    final_recommendations = recommended_product_ids_df.merge(df_products,on='Product_id')
    
    st.success('Your recommendations have been successfully generated!')
    st.subheader('The top 5 products recommendation for you are: ')
    return final_recommendations[final_recommendations.Category.str.contains(category)].head(5)

user_id_input = int(st.sidebar.text_input("Please enter your user ID at Sephora", 67))
st.write(get_predictions(user_id_input,category))


def recommend_products_by_user_features(skintone, skintype, eyecolor, haircolor, category, percentile=0.85):
    ddf = df[(df['Skin_Tone'] == skintone) & (df['Hair_Color'] == haircolor) & (df['Skin_Type'] == skintype) & (df['Eye_Color'] == eyecolor)]

    recommendations = ddf[(ddf['Rating_Stars'].notnull())][
        ['Category', 'Rating_Stars', 'Product_Url', 'Brand', 'Product']]
    recommendations = recommendations.sort_values('Rating_Stars', ascending=False).head(10)
    recommendations = recommendations[recommendations.Category == category]

    st.write('Based on your features, customers with similar features have bought:')
    st.write(recommendations)

#recommend_products_by_user_features(skin_tone, skin_type, eye_color, hair_color, category)

with st.container():
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Products", "315")
    col2.metric("Total Users", "5334")
    col3.metric("Total Reviews", "5784")

def popularity_based_recommendation(data):
    df_pb_rec = data.copy()
    df_pb_rec["product_and_brand"] = df_pb_rec["Product"] + " from " + df_pb_rec["Brand"]
    top_products_of_all_time = pd.DataFrame(df_pb_rec.groupby('product_and_brand')['Rating_Stars'].mean()
                                            .sort_values(ascending=False))
    st.subheader('The top and worst 10 products recommendation of all time: ')
    
    with st.expander("Click to see more"):
        st.write('The top 10 products recommendation of all time: ')
        st.write(top_products_of_all_time.head(10))

        worst_products_of_all_time = top_products_of_all_time.copy()
        st.write('The worst 10 products recommendation of all time: ')
        st.write(worst_products_of_all_time.iloc[::-1].head(10))

popularity_based_recommendation(df)
