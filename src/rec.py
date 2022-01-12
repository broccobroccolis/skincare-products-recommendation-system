#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 22:22:52 2022

@author: wanwoeichyi
"""

import streamlit as st
import pandas as pd
import numpy as np
from surprise import accuracy, Dataset, Reader, NormalPredictor, BaselineOnly, KNNBasic, KNNWithMeans, KNNBaseline, KNNWithZScore, SVD, SVDpp, NMF, SlopeOne, CoClustering
from surprise.model_selection import train_test_split as tts
from collections import defaultdict
from PIL import Image

def app():
    st.subheader("""Welcome to your skincare products recommendation engine!""")
    st.caption("Now be patient... We need a little bit of time to give you our best...")
    
    cleaned_data = pd.read_csv("https://raw.githubusercontent.com/broccobroccolis/skinoclock/main/Cleaned_skindataall.csv")
    df = cleaned_data.copy()
    
    category = st.selectbox("Select the product category you're looking for: ",("Cleanser","Toner","Treatment","Moisturizer","Face Mask"))
    
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
    
    all_pred = get_all_predictions(predictions)

    #to get top N recommendations
    n = 308
    for uid, user_ratings in all_pred.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        all_pred[uid] = user_ratings[:n]
    tmp = pd.DataFrame.from_dict(all_pred)
    tmp_transpose = tmp.transpose()
        
    user_id_input = int(st.text_input("Please enter your user ID at Sephora: ", 67))
    final_recommendations = get_predictions(user_id_input,category,tmp_transpose,df)
    st.write(final_recommendations.head())
#    for x in range(0,4):
#        st.write("No.", x+1 , final_recommendations['Product'][x].name, " from ",final_recommendations['Brand'][x].name)
#        st.caption("Price: ", final_recommendations['Price'][x])
#        st.caption("Size in ml: ", final_recommendations['Size'][x])
#        st.caption("Ingredients: ", final_recommendations['Ingredients'][x])
#        st.caption("URL: ", final_recommendations['Product_Url'][x])
    
    st.write("")
    popularity_based_recommendation(df)
    
    
def get_all_predictions(predictions):
    
    # First map the predictions to each user.
    top_n = defaultdict(list)    
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # Then sort the predictions for each user
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)

    return top_n


#get predictions for a user
def get_predictions(user_id,category,tmp_transpose,df):
    n=308
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
    
    final_recommendations = final_recommendations[final_recommendations.Category.str.contains(category)]
    return final_recommendations


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

