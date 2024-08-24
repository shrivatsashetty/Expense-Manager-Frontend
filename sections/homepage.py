import streamlit as st

st.markdown("# Hello There :wave:")
st.markdown("# Welcome to Expense Manger :dollar:")


cover_image_url = """
https://media.istockphoto.com/id/1383866726/photo/annual-budget-and-\
financial-planning-concept-with-manager-or-executive-cfo-crafting-or.jpg\
?s=2048x2048&w=is&k=20&c=iyhk1WbUWUo6921DgUs7NqVaC__qS8fgzZeJkqp6bnE=
"""

cover_image_path = "assets/expense_manager_cover.jpeg"

st.image(
    image = cover_image_path,
    caption = "Expense Manger",
    )

st.markdown("***")
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