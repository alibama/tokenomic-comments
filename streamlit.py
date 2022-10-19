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
df = pd.read_json('https://tokenomics.aragond.tech/topics.json?_format=json')

def main():
	if st.button("Generate Sweetviz Report"):
		report = sv.analyze(df)
		report.show_html()
		st_display_sweetviz("SWEETVIZ_REPORT.html")

def st_display_sweetviz(report_html,width=1000,height=500):
	report_file = codecs.open(report_html,'r')
	page = report_file.read()
	components.html(page,width=width,height=height,scrolling=True)
#dfdata = dfdata[dfdata['cited'] >= citations] 
#dfdata['doi'] = dfdata['doi'].astype(str)  #pandas was calling this a mixed type column and it borked sweetviz
#dfdata['aff'] = dfdata['aff'].astype(str)  #pandas was calling this a mixed type column and it borked sweetviz
#dfdata
df.to_csv('opendata.csv', index=False)
st.write(df)
        

if __name__ == '__main__':
	main()
