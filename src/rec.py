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
    
    cleaned_data = pd.read_csv("https://raw.githubusercontent.com/broccobroccolis/skinoclock/main/Cleaned_skindataall.csv")
    df = cleaned_data.copy()
    
    category = st.selectbox("Select the product category you're looking for: ",("Cleanser","Toner","Treatment","Moisturizer","Face Mask"))
    
    try : 
        user_id_input = int(st.text_input("Please enter your user ID at Sephora: "))
    except ValueError:
        pass
    

    if st.button('Get recommendations'):
        try:
            st.caption("Now be patient... We need a little bit of time to give you our best...")
            get_recommendation(user_id_input,category)
            #final_recommendations = get_predictions(user_id_input,category,tmp_transpose,df)
            #st.write(final_recommendations.head())
    
        except AttributeError:
            pass
    else:
        pass
    
    st.write("")
    popularity_based_recommendation(df)
    
def get_recommendation(user_id_input,category):
    cleaned_data = pd.read_csv("https://raw.githubusercontent.com/broccobroccolis/skinoclock/main/Cleaned_skindataall.csv")
    df = cleaned_data.copy()
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
    
    final_recommendations = get_predictions(user_id_input,category,tmp_transpose,df)
    st.write(final_recommendations.head())

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
    except AttributeError:
        st.warning("Sorry, we can't generate relevant recommendations because your User ID isn't in our database.")
        return None
    recommended_product_ids_df = pd.DataFrame(recommended_product_ids, columns=['Product_id'])
    final_recommendations = recommended_product_ids_df.merge(df_products,on='Product_id')
    
    st.success('Your recommendations have been successfully generated!')
    st.subheader('The top 5 products recommendation for you are: ')
    
    final_recommendations = final_recommendations[final_recommendations.Category.str.contains(category)]

    final_recommendations.rename(columns = {'Price':'Price (USD)'}, inplace = True)
    final_recommendations.rename(columns = {'Size':'Size (ml)'}, inplace = True)
    final_recommendations = final_recommendations.reset_index(drop=True)

    return final_recommendations


def popularity_based_recommendation(data):
    df_pb_rec = data.copy()
    df_pb_rec["product_and_brand"] = df_pb_rec["Product"] + " from " + df_pb_rec["Brand"]
    top_products_of_all_time = pd.DataFrame(df_pb_rec.groupby('product_and_brand')['Rating_Stars'].mean()
                                            .sort_values(ascending=False))
    
    pb_rec = top_products_of_all_time.merge(df_pb_rec,on='product_and_brand')
    pb_rec.drop_duplicates(subset=['Product_id'],inplace=True)

    final_pb_rec = pb_rec[['Product_id','Category','Product', 'Brand','Rating_Stars_x','Price','Size','Ingredients','Product_Url']]
    final_pb_rec.rename(columns = {'Rating_Stars_x':'Average Rating Stars'}, inplace = True)
    final_pb_rec.rename(columns = {'Price':'Price (USD)'}, inplace = True)
    final_pb_rec.rename(columns = {'Size':'Size (ml)'}, inplace = True)

    final_pb_rec.sort_values(by=['Average Rating Stars'], inplace=True, ascending=False)
    final_pb_rec = final_pb_rec.reset_index(drop=True)

    st.subheader('The top and worst N products recommended by users of all time: ')
    
    with st.expander("Click to see more"):
        N = st.slider("Enter number N: ", min_value=1, max_value=int(len(pb_rec)/2), value=5)
        st.write('The top ', N, ' products recommended by users of all time: ')
        st.write(final_pb_rec.head(N))

        st.write('The worst ', N, ' products recommended by users of all time: ')
        st.write(final_pb_rec.iloc[::-1].head(N))
