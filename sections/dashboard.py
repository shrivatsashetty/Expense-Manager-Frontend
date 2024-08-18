import streamlit as st

import pandas as pd

st.title(":clipboard: DASHBOARD")

st.markdown("***")
st.markdown("### Key-Metrics :key:")

col11, col12, col13 = st.columns(3, gap ='small', vertical_alignment = 'bottom')

with col11:
    st.metric(
        label = ":blue[Username]" , 
        value = 'Aman' ,
        help = "The name of the Dataset that was assesed" , 
    )

with col12:
    st.metric(
        label = ":green[Total Income]",
        value = 25000,
        delta = "5%",
        delta_color = "normal",
        help = "Total Income for the Current Month"
    )

with col13:
    st.metric(
        label = ":red[Total Expenditure]",
        value = 16000,
        delta = "6%",
        delta_color = "inverse",
        help = "Total Expenditure so far for the Current Month"
    )

