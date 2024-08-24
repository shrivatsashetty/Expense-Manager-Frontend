import streamlit as st
import plotly.express as px
import requests

import pandas as pd
import numpy as np

get_url = "http://localhost:8080/transactions"

st.title(":clipboard: REPORT DASHBOARD")

try:
    
    get_response = requests.get(get_url)

    if get_response.status_code == 200:

        transactions_data = get_response.json()
        st.markdown("### Transactions Data:")
        st.write(get_response.json())

        transactions_df = pd.DataFrame(transactions_data)
        st.dataframe(transactions_df)

        st.markdown("***") # this adds a horizontal ruler
        st.markdown("## Key-Metrics :key:")

        col11, col12, col13 = st.columns(3, gap ='small', vertical_alignment = 'bottom')

        with col11:
            st.metric(
                label = ":blue[Total Transactions]" , 
                value = len(transactions_df['transactionAmount']) ,
                help = "Username" , 
            )

        with col12:
            st.metric(
                label = ":green[Avg Spending Per Day]",
                value = int(transactions_df['transactionAmount'].mean()),
                delta = "5.4%", # indicates rate of increase or deacrease
                delta_color = "normal", # indicates color coding for delta value
                help = "Total Income for the Current Month"
            )

        with col13:
            st.metric(
                label = ":red[Max Single Transaction]",
                value = transactions_df['transactionAmount'].max(),
                delta = "6.2%",
                delta_color = "inverse",
                help = "Total Expenditure so far for the Current Month"
            )

        st.markdown("***")
        st.markdown("## Category Wise Expenditure")

        # Displaying the DataFrame
        fig = px.pie(transactions_df, values = 'transactionAmount', names = 'expenseCategory', hole=.2, )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("***")
        st.markdown("## Month-Wise Expenditure")

        st.dataframe(transactions_df)

        fig = px.bar(
            transactions_df, 
            x = 'transactionMonth', 
            y = 'transactionAmount', 
            title = 'Total Monthly Expenditure So Far',
            color = 'expenseCategory',
            )

        st.plotly_chart(fig, use_container_width=True)

        # crating data to monitor daily spending trends
        st.markdown("***")
        st.markdown("## Daily Spending Trends")
 
        fig = px.line(transactions_df, x='transactionDate', y='transactionAmount', color='transactionMonth', 
                    title='Daily Spending Trends for Past and Current Month')

        st.plotly_chart(fig, use_container_width=True)

except Exception as err:
    st.markdown("### Data Not Found")
    st.write(err)
