import streamlit as st
import plotly.express as px

import pandas as pd
import numpy as np

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

st.markdown("***")
st.markdown("## Monthly-Wise Expenditure")
# creating a dictionary for montly expenditure
monthly_expenditure_data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Total_Expenditure': [22000, 18000, 20000, 15000, 24000, 23000]  # all Values are less than INR 25000
}

# Converting the dictionary to a pandas DataFrame
monthly_expenditure_df = pd.DataFrame(monthly_expenditure_data)

fig = px.bar(
    monthly_expenditure_df, 
    x = 'Month', 
    y = 'Total_Expenditure', 
    title = 'Total Monthly Expenditure So Far',
    color = 'Month',
    )

st.plotly_chart(fig, use_container_width=True)

# crating data to monitor daily spending trends
st.markdown("***")
st.markdown("## Daily Spending Trends")
# Assuming 30 days for both June and July
# Creating a range of days from 1 to 30 for both June and July
days_in_june = np.arange(1, 31)
days_in_july = np.arange(1, 28)

# Generate random spending data for each day ensuring the total does not exceed INR 25000 per month
np.random.seed(0)  # For reproducibility
june_expenditure = np.random.randint(500, 1500, size=len(days_in_june))
july_expenditure = np.random.randint(500, 1500, size=len(days_in_july))

# Ensure the total expenditure for each month doesn't exceed INR 25000
june_expenditure = june_expenditure * (25000 / june_expenditure.sum())
july_expenditure = july_expenditure * (25000 / july_expenditure.sum())

# Creating DataFrame for June
df_june = pd.DataFrame({
    'Date': days_in_june,
    'Expenditure': june_expenditure,
    'Month': 'June'
})

# Creating DataFrame for July
df_july = pd.DataFrame({
    'Date': days_in_july,
    'Expenditure': july_expenditure,
    'Month': 'July'
})

# Combine both DataFrames
df_spending_trends = pd.concat([df_june, df_july])

fig = px.line(df_spending_trends, x='Date', y='Expenditure', color='Month', 
              title='Daily Spending Trends for Past and Current Month')

st.plotly_chart(fig, use_container_width=True)