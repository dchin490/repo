
import streamlit as st
import math

def sugar_arb(sb, w):
    prem = abs((sb*22.0462)-w)
    prem = round(prem, 5)
    return prem

sb = st.number_input("NYBOT Sugar", min_value=0, max_value=None, step =.01)
w = st.number_input("White Sugar", min_value=0, max_value=None, step = .1)   
st.metric("Arb Premium", sugar_arb(sb, w), delta=None, delta_color="normal")

