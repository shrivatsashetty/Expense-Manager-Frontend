import streamlit as st

user_management_page = st.Page("sections/user_management.py", title = "Manage User", icon = "👤")
home_page = st.Page("sections/homepage.py", title = "Home", icon = "🏠")
analysis_page = st.Page("sections/analysis.py", title = "Analysis", icon = "🔎")
add_expense_page = st.Page("sections/add_expense.py", title = "Add Expense", icon = "➕")
send_report = st.Page("sections/send_report.py", title = "Send Report", icon = "✉️")

pages = st.navigation(
    {
        # page grouping
        "General": [ 
            home_page, 
            user_management_page,
            ],
        "Ananlysis & Report": [ 
            analysis_page, 
            send_report
            ],
        "Manage Expense": [
            add_expense_page 
            ] 
    }
)

pages.run()