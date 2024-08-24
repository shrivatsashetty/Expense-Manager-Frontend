import streamlit as st
import datetime
import requests

post_url = "http://localhost:8080/transactions/add"

st.markdown("# Add Expenses :heavy_plus_sign:")
st.markdown("***")

# 
def log_form_data(form_data):
    st.write(form_data)

with st.form(key = "_add_exp_form"):
    st.markdown("### Add Expense :moneybag:")

    # enter transaction amount
    transaction_amount = st.number_input(label = "Enter Amount",min_value = 1, placeholder = "Enter Transaction Amount")

    # text note along the transaction
    text_note = st.text_input(label = "Add Note", )

    # expenditure category(Rent, Food, Travel etc)
    expense_category = st.selectbox(label = "Expense Category", 
                                    options = ["Rent 💵", "Tax 💶", "Food 🥞", "Travel 🚌", "Investment 🏦"]
                                    )
    # date of transaction, defaults to today's date
    transaction_date = st.date_input(label = "Enter Transaction Date", 
                                     value = datetime.date.today(),
                                     key = "_transaction_date_selector",
                                     help = "Select Transaction Date",
                                     format = "DD/MM/YYYY",
                                     )

    transaction_data: dict = {
        "transactionAmount": transaction_amount,
        "textNote": text_note,
        "expenseCategory": expense_category,
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

        
        post_response = requests.post(post_url, json = transaction_data)

        if post_response.status_code == 200:
            st.success(f'Expense Added Sucessfully on {transaction_date}', icon="✅")
        else:
            st.warning("Failed to update transaction", icon = "⚠️")
        

        # e = RuntimeError("Unable to Display Report")
        # st.exception(e)

