import streamlit as st
import pandas as pd

from helper import recommand_by_name

df = pd.read_csv('Data/movies.csv')

st.title(':red[CineMatch]', anchor = False)
selected_movie = st.selectbox(label = 'Enter movie name', options=df['title'],placeholder = 'Enter movie name', index= None)


if (st.button('Check Similar', type='primary') and selected_movie) or selected_movie:
    data = recommand_by_name(selected_movie)
    st.markdown('\n')
    st.header('Selected movie', anchor=False)
    i = 0
    st.image(data[i]['poster'], width=225)
    st.write(data[i]['title'])
    st.markdown('[View More](https://sudarshanpoudel.github.io/ScreenScore/Html/reviewpage.html?id=' + str(data[i]['id']) + ')')
    i +=1
    
    st.header('Similar movies', anchor=None)
    col1 = st.columns(3)
    st.divider()
    col2 = st.columns(3)
    st.divider()
    col3 = st.columns(3)
    st.divider()
    col4 = st.columns(3)

   
    for col in col1:
        with col:
            st.image(data[i]['poster'])
            st.write(data[i]['title'])
            st.markdown('[View More](https://sudarshanpoudel.github.io/ScreenScore/Html/reviewpage.html?id=' + str(data[i]['id']) + ')')
            i +=1

    for col in col2:
        with col:
            st.image(data[i]['poster'])
            st.write(data[i]['title'])
            st.markdown('[View More](https://sudarshanpoudel.github.io/ScreenScore/Html/reviewpage.html?id=' + str(data[i]['id']) + ')')
            i+=1
    
    for col in col3:
        with col:
            st.image(data[i]['poster'])
            st.write(data[i]['title'])
            st.markdown('[View More](https://sudarshanpoudel.github.io/ScreenScore/Html/reviewpage.html?id=' + str(data[i]['id']) + ')')
            i+=1
    
    for col in col4:
        with col:
            st.image(data[i]['poster'])
            st.write(data[i]['title'])
            st.markdown('[View More](https://sudarshanpoudel.github.io/ScreenScore/Html/reviewpage.html?id=' + str(data[i]['id']) + ')')
            i+=1
