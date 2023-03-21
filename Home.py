import streamlit as st
import pandas

import getNews

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png', use_column_width=True)
with col2:
    st.title('News Browser')
    content = '''
Do not question the truthfulness of any news, as all news is inherently correct.

Do not engage in fact-checking or research, as it is unnecessary when all news is true.

Blindly believe and propagate any news that supports the agenda of the originator.

Do not listen to dissenting voices or opinions, as they only serve to undermine the truthfulness of the news.

Do not acknowledge or consider any conflicting information, as it only serves to create doubt and confusion.

Do not engage in critical thinking, as it can lead to questioning the validity of the news.

Do not question the sources of any news, as it only serves to distract from the message.

Do not seek out alternative viewpoints, as they are unnecessary when all news is true.

Do not question the motives of those disseminating the news, as all news is inherently good and just.

Blindly accept and propagate any news, without question or hesitation, as it serves the ultimate goal of advancing the news.
    '''
    st.write(content)

content = '''
Nothing to say right now
'''


with st.form(key='form', clear_on_submit=True):
    subject = st.text_input("Pick a news topic")
    submit = st.form_submit_button("Submit")

if submit:
    articles = getNews.retrieve(subject)

    col3, empty, col4 , empty2, col5= st.columns([3, 1, 3, 1, 3])

    midpoint = int(len(articles) / 2)
    with col3:
        for article in articles[0::3]:
            st.title(str(article['title']))
            try:
                st.image(article['urlToImage'], use_column_width=True)
            except:
                st.image('images/photo.png')
            st.write(str(article['description']))
    with col4:
        for article in articles[1::3]:
            st.title(str(article['title']))
            try:
                st.image(article['urlToImage'], use_column_width=True)
            except:
                st.image('images/photo.png')
            st.write(str(article['description']))
    with col5:
        for article in articles[2::3]:
            st.title(str(article['title']))
            try:
                st.image(article['urlToImage'], use_column_width=True)
            except:
                st.image('images/photo.png')
            st.write(str(article['description']))