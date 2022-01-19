
import streamlit as st
import math

def sugar_arb(sb, w):
    prem = abs((sb*22.0462)-w)
    prem = round(prem, 5)
    return prem

w = st.number_input("LDN PRICE", min_value=None max_value=None, step = 0.1)
sb = st.number_input("NY PRICE", min_value=0.00, max_value=None)
st.metric("ARB PREMIUM", sugar_arb(sb, w), delta=None, delta_color="normal")

