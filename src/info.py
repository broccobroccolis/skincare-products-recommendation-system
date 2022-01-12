#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:45:43 2022

@author: wanwoeichyi
"""

import streamlit as st
from PIL import Image

def app():
    st.subheader("""Why is good skincare important?""")
    
    st.write("✨It helps your skin stay in good condition.")
    st.caption("You’re shedding skin cells throughout the day, so it’s important to keep your skin glowing and in good condition. An effective routine can help prevent acne, treat wrinkles, and help keep your skin looking its best.")

    st.write("✨Your skin will look more youthful.")
    st.caption("As you age, your skin’s cells turn over more slowly, make it look duller and less radiant. Using a quality skin care line can help remove dead skin cells so your body will replace them with newer, more youthful cells.")

    st.write("✨ Prevention is easier than correction.")
    st.caption("Preventing skin problems is easier -– and less costly – than trying to fix them in the future.")
    
    st.write("✨ Your self-confidence will get a boost.")
    st.caption("When your skin looks better, you’ll feel better about yourself and have more self-confidence.")
    
    
    st.subheader("What are some good skin care components?")
    
    st.write("🧴 Cleanser")
    st.caption("Face washes are designed to remove impurities, germs, dirt and makeup that can irritate the skin. Regular cleansing is essential to keeping your skin looking radiant and healthy.")
    st.write("✨ Toner")
    st.caption("Toner is used after washing your face, and it helps smooth and calm skin while restoring nutrients.")
    st.write("🔮 Treatment")
    st.caption("Because a treatment/serum is lighter and delivers active ingredients to the skin quickly, it goes on first, after you've cleansed your skin. Think of it as the secret weapon for treating skin issues like discoloration, dullness, fine lines, or acne — and a moisturizer as the key to hydrating your skin.")
    st.write("💧 Moisturizer")
    st.caption("Moisturizer can help keep your skin hydrated and refreshed. As we age, the oil glands that keep skin healthy begin to lose their power, making it to where they create fewer oils. Moisturizing daily causes the glands to not have to work as hard to keep your skin healthy throughout your life.")
    st.write("🪞 Face Mask")
    st.caption("Face masks dive down deeper into the pores than regular daily cleansers. They can help draw out dirt, oil and impurities from below the skin's surface, giving you a more thorough cleansing session. Masks are great for body and mind as well as skin.")
    
    image = Image.open('img/model.jpeg')
    st.image(image)
        
    st.write("")
    st.caption("References:")
    st.caption("https://www.skincenterofsouthmiami.com/2018/06/the-importance-of-facials-and-skin-care/\
              https://www.completefamilydermatology.com/blogs/why-moisturizing-is-so-important/\
              https://www.healthline.com/health/benefits-of-face-serum")
