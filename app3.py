import streamlit as st
import pandas as pd
import numpy as np
import time

# session
# callback

st.header('Session state')

st.session_state

session = st.session_state

if 'a_counter' not in session : 
    session['a_counter'] = 0

if 'boolean' not in session : 
    session['boolean'] = False

st.write(session)

# button
r = st.button('Button', key='but1')

if r : 
    "before button press", session

    session.a_counter += 1
    session.boolean = not session.boolean

    'after button press', session

#=======================================================
# kg <-> lbs
#=======================================================
st.subheader('Kg <-> lbs')

def lbs_to_kg() :
    session.kg = session.lbs / 2.2046

def kg_to_lbs() :
    session.lbs = session.kg * 2.2046

def clear() : 
    session.kg = session.lbs = 0

col1, buf, col2 = st.columns([2,1,2])

with col1 : 
    pounds = st.number_input("Pounds:", key='lbs', on_change=lbs_to_kg)

with col2 : 
    kilogram = st.number_input("Kg:", key='kg', on_change=kg_to_lbs)

st.button('Clear', on_click=clear)

