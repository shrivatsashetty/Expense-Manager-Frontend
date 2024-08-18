import streamlit as st

st.markdown("# Add Expenses :heavy_plus_sign:")
st.markdown("***")

with st.form(key = "_add_exp_form"):
    st.markdown("### Add Expense :moneybag:")
    amount = st.number_input(label = "Enter Amount",min_value = 1, placeholder = "Enter Transaction Amount")
    note = st.text_input(label = "Add Note", )
    expense_category = st.selectbox(label = "Expense Category", options = ["Rent 💵", "Tax 💶", "Food 🥞", "Travel 🚌", "Investment 🏦"])


    if st.form_submit_button("Add", type = 'primary' ):
        st.success('Expense Added Sucessfully', icon="✅")

