import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # matplot 라이브러리가 없어서 오류가 발생할 것임, 설치필요
import graphviz as graphviz

rand = np.random.normal(1, 2, size = 20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)


st.graphviz_chart(
  digraph {
    Big_shark -> Tuna
    Tuna -> Mackerel
    Mackerel -> small_fishes
  }
)


df = pd.DataFrame(np.random.randn(500,2) / [50,50] + [37.76, -122.4], columns = ['lat', 'lon'])
st.map(df)

x = st.slider('Select a value') # 슬라이더 추가
st.write(x, 'sqaured is', x * x) # 웹페이지를 텍스트처럼 사용할 수 있음

