import streamlit as st
import pandas as pd
import numpy as np
st.title('JAM')
col1, col2 = st.columns(2)
with col1:
    fname = st.text_input('First Name')
with col2:
    lname = st.text_input('Last Name')
if st.button("Submit"):
    st.markdown(f'***your first name is*** :blue-background[{fname}]',)
    st.markdown(f'***your last name is*** :blue-background[{lname}]',)