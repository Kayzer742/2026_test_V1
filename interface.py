# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 09:47:44 2023

@author: AntoineBois
"""

import streamlit as st
import hmac
import streamlit as st

def runstreamlit () :
    
    st.title("Interface 1.0")
    
    option = st.selectbox('Localisation ? ',
    ('EU',
      'US'))

    st.file_uploader('Data loads')

if __name__ == "__main__":
    runstreamlit()
        
