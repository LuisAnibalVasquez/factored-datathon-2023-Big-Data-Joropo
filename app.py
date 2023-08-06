import requests
import streamlit as st
from tensorflow import keras
import tensorflow as tf


# model = keras.models.load_model("models")

st.set_page_config(page_title="Big Data & Joropo App", page_icon="🌠", layout="wide")

st.markdown("<h1 style='text-align: center;'>Big Data & Joropo App 🌠</h1>", unsafe_allow_html=True)
st.markdown("This app is part of the data solution developed for the Factored Datathon 2023.")
st.markdown("In this, you can use the REST API developed as part of the challenge.")
st.markdown("The app consume 2 APIs:")
st.markdown("The first one is for the sentiment analysis of a given amazon boook review.")
st.markdown("The second one return book recommedation for a given user.")

with st.container():
    col1, col2, = st.columns(2)
    with col1:
        review = st.text_input('Review')    
    with col2:
        reviewerID = st.text_input('Reviewer ID')                         

def main():

    with st.form('sentiment_form'):
        submitReview = st.form_submit_button("Get sentiment")  
        if submitReview:
            if review == "":
                st.warning('Reviews is mandatory', icon="⚠️")
            else:
                path = "https://joropo-factored.onrender.com/sentimet/" + review
                data = requests.post(path).json()
                if data[0] > 0:
                    s = "With a " +  str(data[1]) + " of confidence the review is POSITIVE"             
                else:
                    s = "With a " +  str(data[1]) + " of confidence the review is NEGATIVE"             
                st.subheader(s)
                st.write(data)

    with st.form('recommender_form'):        
        submitRecommender = st.form_submit_button("Get recommendation")                            
        if submitRecommender:
            if reviewerID == "":
                st.warning('Reviewer ID is mandatory', icon="⚠️")
            else:
                path = "https://joropo-factored.onrender.com/recommend/" + reviewerID
                data = requests.post(path).json()       
                st.subheader("Recommended products for the user " + reviewerID)
                st.write(data)


if __name__ == '__main__':
    main()