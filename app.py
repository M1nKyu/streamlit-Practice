import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(500,2) / [50,50] + [37.76, -122.4], columns = ['lat', 'lon'])
st.map(df)

x = st.slider('Select a value') # 슬라이더 추가
st.write(x, 'sqaured is', x * x) # 웹페이지를 텍스트처럼 사용할 수 있음
