
import streamlit as st
import math

def sugar_arb(sb, w):
    prem = abs((sb*22.0462)-w)
    prem = round(prem, 5)
    return prem

sb = st.number_input("NYBOT Sugar", min_value=0, max_value=None)
w = st.number_input("White Sugar", min_value=0, max_value=None)   

st.button("Calculate Premium", key=None, help=None, on_click=None, args=None, kwargs=None)
    
