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

    option = st.selectbox('Type de batterie ?',
    ("JH4-4P",
      "JH4-3P",
       "JH4-2P",
        "JH4-1P",
         "JP3-2P",
          "JP3-3P"))

    option = st.selectbox('Type de container ?',
    ("20 pieds",
      "40 pieds",
       "45 pieds"))

    st.file_uploader('Choisissez un fichier de T°C extérieure')
    st.file_uploader('Choisissez un fichier de sollicitation')

    st.markdown('Construction du profil de puissance si pas de fichier de sollicitations')
    st.text_input('C-Rate')
    st.text_input('Temps inter cycle')


if __name__ == "__main__":
    runstreamlit()
        
