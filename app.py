# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:58:30 2026

@author: ayagh
"""
import streamlit as st
import pickle # بنستخدم pickle بدل tensorflow عشان دي ملفات .pkl

# 1. تحميل الموديل والمترجم
def load_files():
    with open('final_rf_model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('final_vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_files()

# 2. واجهة الموقع
st.title("Fake Job Detection") # بما إن المشروع عن الوظائف المزيفة
user_input = st.text_area("Enter the job description here:")

if st.button("Check"):
    if user_input:
        # تحويل الكلام لأرقام باستخدام المترجم
        data = vectorizer.transform([user_input])
        # التوقع باستخدام الموديل
        prediction = model.predict(data)
        
        if prediction[0] == 1:
            st.error("Warning: This might be a Fake job!")
        else:
            st.success("This looks like a Real job.")