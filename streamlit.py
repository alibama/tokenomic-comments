import math
import streamlit as st
import numpy as np
import json
import altair as alt
from urllib.request import urlopen
#from xml.etree.ElementTree import parse
import urllib
import urllib.parse as urlparse
import requests
import pandas as pd
#import pandas_profiling
#@st.cache


import codecs
#from pandas_profiling import ProfileReport 

# Components Pkgs
import streamlit.components.v1 as components
#from streamlit_pandas_profiling import st_profile_report

# Custom Component Fxn
import sweetviz as sv 

st.header('tokenomics comments ')
st.subheader('Exploratory Data Analysis with Streamlit')

st.markdown('In this app we are using content pulled from the [tokenomic comments](https://tokenomics.aragond.tech) with a small Python script')

@st.cache(suppress_st_warning=True)

df = pd.read_json('https://tokenomics.aragond.tech/topics.json?_format=json')
print(df)
