import streamlit as st

home_page = st.Page("sections/homepage.py", title = "Home", icon = "🏠")
analysis_page = st.Page("sections/analysis.py", title = "Analysis", icon = "🔎")
add_expense_page = st.Page("sections/add_expense.py", title = "Add Expense", icon = "➕")

pages = st.navigation(
    
    {
        # page grouping
        "General": [ home_page ],
        "Ananlysis & Report": [ analysis_page],
        "Manage Expense": [add_expense_page ] 
    }

)

pages.run()