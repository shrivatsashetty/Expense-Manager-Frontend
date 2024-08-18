import streamlit as st
import plotly.express as px

import pandas as pd

st.title(":clipboard: REPORT DASHBOARD")

st.markdown("***") # this adds a horizontal ruler
st.markdown("## Key-Metrics :key:")

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
        delta = "5.4%", # indicates rate of increase or deacrease
        delta_color = "normal", # indicates color coding for delta value
        help = "Total Income for the Current Month"
    )

with col13:
    st.metric(
        label = ":red[Total Expenditure]",
        value = 16000,
        delta = "6.2%",
        delta_color = "inverse",
        help = "Total Expenditure so far for the Current Month"
    )

st.markdown("***")
st.markdown("## Category Wise Expenditure")

# Creating a dictionary for category-wise expenditure
cat_wise_exp_data = {
    'Category': ['Rent', 'Tax', 'Food', 'Travel', 'Investments'],
    'Amount': [5000, 3000, 4000, 2000, 2000]  # Distributed the total INR 16000
}

# Converting the dictionary to a pandas DataFrame
cat_wise_exp_df = pd.DataFrame(cat_wise_exp_data)

# Displaying the DataFrame
fig = px.pie(cat_wise_exp_df, values = 'Amount', names = 'Category', hole=.2, )
st.plotly_chart(fig, use_container_width=True)
