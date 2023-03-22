import streamlit as st
import streamlit.components.v1 as components
import json
import getNews

with open('data/newsApiKeyFile.json') as f:
    content = json.load(f)
    apiKey = content['key']

st.set_page_config(layout="wide")

col1, col2 = st.columns([1, 4])
with col1:
    st.image('images/photo.png', use_column_width=True)
    st.image('images/musk.jpg', use_column_width=True)
    st.markdown('<p style="text-align: center;">News API Documentation</p>', unsafe_allow_html=True)


with col2:
    st.title('News Browser')
    with open('data/manifesto.txt') as file:
        st.write(file.read())
    components.iframe('https://newsapi.org/docs',
                      height=600,
                      scrolling=True)

with st.form(key='form', clear_on_submit=True):
    subject = st.text_input("Pick a news topic")
    begin_date = st.date_input(key="start", label="Start Date").isoformat()
    end_date = st.date_input(key="end", label="End Date").isoformat()
    languages = ['en','ar','de','es','fr','he','it','nl','no','pt','ru','sv','ud','zh']
    language = st.selectbox(label="Language", options=languages)
    submit = st.form_submit_button("Submit")

if submit:
    articles = getNews.retrieve(apiKey,
                                topic=subject,
                                language=language,
                                start_date=begin_date,
                                end_date=end_date)

    col3, empty, col4 , empty2, col5= st.columns([3, 1, 3, 1, 3])
    with col3:
        for article in articles[0::3]:
            st.title(str(article['title']))
            try:
                st.image(article['urlToImage'], use_column_width=True)
            except:
                st.image('images/photo.png')
            st.write(str(article['description']))
            st.write(str(article['url']))
    with col4:
        for article in articles[1::3]:
            st.title(str(article['title']))
            try:
                st.image(article['urlToImage'], use_column_width=True)
            except:
                st.image('images/photo.png')
            st.write(str(article['description']))
            st.write(str(article['url']))
    with col5:
        for article in articles[2::3]:
            st.title(str(article['title']))
            try:
                st.image(article['urlToImage'], use_column_width=True)
            except:
                st.image('images/photo.png')
            st.write(str(article['description']))
            st.write(str(article['url']))