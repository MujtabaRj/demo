import streamlit as st
import numpy as np
from PIL import Image

img = Image.open('izuku.jpg')
st.image(img)
x = np.arange(-10,10)
st.title("Graph of the Equation")
s = st.slider(label = "eq",min_value=1,max_value=10)
p = st.slider(label = "pw",min_value=1,max_value=10)
inp = st.number_input("Enter the equation :")
if (st.button("PLOT")):
    st.text(s*x**p)
    st.line_chart(s*x**p)