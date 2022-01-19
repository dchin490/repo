import streamlit as st
import math

#arb premium calc
def sugar_arb(sb, w):
    prem = abs((sb*22.0462)-w)
    prem = round(prem, 5)
    return prem

#assign user input prices to sugar legs 
w = st.number_input("White Sugar (W:IFLX)", min_value=0.0, max_value=None, step = 0.1)
sb = st.number_input("Sugar No. 11 (SB:IFUS)", min_value=0.00, max_value=None, step = 0.01)

#display arb premium 
st.metric("ARB Premium", sugar_arb(sb, w), delta=None, delta_color="normal")
