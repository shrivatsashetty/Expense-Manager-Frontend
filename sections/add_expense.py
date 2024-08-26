import streamlit as st
import datetime
import requests

import numpy as np
import pandas as pd

post_url = "http://localhost:8080/transactions/add"

post_many_url = "http://localhost:8080/transactions/addmany"

st.markdown("# Add Expenses :heavy_plus_sign:")
st.markdown("***")

# 
def log_form_data(form_data):
    st.write(form_data)


with st.form(key = "_add_exp_form"):
    st.markdown("### Enter Transaction Details :credit_card:")

    # enter transaction amount
    transaction_amount = st.number_input(label = "Enter Amount",min_value = 1, placeholder = "Enter Transaction Amount")

    # text note along the transaction
    text_note = st.text_input(label = "Add Note", )

    expense_category_options_mapping = {
        "Miscellaneous": "Miscellaneous 💲",
        "Rent": "Rent 💵",
        "Tax": "Tax 🧾",
        "Investment": "Investment 💰",
        "Food": "Food 🥞",
        "Travel": "Travel 🚗",
        "Tax": "Tax 🧾",
    }

    # expenditure category(Rent, Food, Travel etc)
    expense_category = st.selectbox(label = "Expense Category", 
                                    options = list(expense_category_options_mapping.values())
                                    )
    
    # date of transaction, defaults to today's date
    transaction_date = st.date_input(label = "Enter Transaction Date", 
                                     value = datetime.date.today(),
                                     key = "_transaction_date_selector",
                                     help = "Select Transaction Date",
                                     format = "YYYY/MM/DD",
                                     )

    transaction_data: dict = {
        "transactionAmount": transaction_amount,
        "textNote": text_note,
        "expenseCategory": str(expense_category).split(" ")[0], # discard the emoji, take only the text
        "transactionDate": transaction_date.day,  # type: ignore
        "transactionMonth": transaction_date.strftime('%B'), # type: ignore
        "transactionYear": transaction_date.year, # type: ignore
    }

    if 'transaction_data' not in st.session_state:
        st.session_state['transaction_data'] = None
    
    st.session_state['transaction_data'] = transaction_data

    if st.form_submit_button("Add", type = 'primary', 
                            #  on_click = log_form_data, 
                            #  args = (st.session_state['transaction_data'],) 
                             ):
        
        log_form_data(transaction_data)

        try:
            post_response = requests.post(post_url, json = transaction_data)

            if post_response.status_code == 200:
                st.success(f'Expense Added Sucessfully on {transaction_date}', icon="✅")
            else:
                st.warning("Failed to update transaction", icon = "⚠️")
        except ConnectionError as conn_err:
            st.warning("Server Not Found", icon = "⚠️")
        except Exception as e:
            st.warning("Some Error Occured", icon = "🚫")
            # st.write(e)


# option for adding batch transaction

st.markdown("***")

with st.form(key = "_batch_transaction_insertion_form"):

    st.markdown("### Add Batch Transactions :repeat: ")
    
    # File uploader for selecting the CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    batch_transaction_df = None

    # If a file is uploaded, process and display it
    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        batch_transaction_df = pd.read_csv(uploaded_file)

    else:
        st.write("Please upload a CSV file to see the content.")
    
    if st.form_submit_button("Submit"):
         
        if batch_transaction_df is not None:
            
            # convert the batch transaction data to a Pyhton dictionary to make it as a payload
            batch_transaction_dict = batch_transaction_df.to_dict(orient = 'records')
            
            # st.write(batch_transaction_dict)

            try:
                post_response = requests.post(post_many_url, json = batch_transaction_dict)

                if post_response.status_code == 200:
                    st.success(f'Expense Added Sucessfully on {transaction_date}', icon="✅")
                else:
                    post_response.status_code
                    st.warning("Failed to update transaction", icon = "⚠️")
            except ConnectionError as conn_err:
                st.warning("Server Not Found", icon = "⚠️")
            except Exception as e:
                st.warning("Some Error Occured", icon = "🚫")
                st.write(e)

        else:
            st.warning("No Data to Send, Choose a file", icon = "🚫")
