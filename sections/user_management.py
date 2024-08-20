import streamlit as st
import requests

st.markdown("# User Mangement :bust_in_silhouette:") 

with st.form(key = "_login_or_signup_form", clear_on_submit = True):
    add_or_remove_user = st.selectbox(label = "Add or Remove User", options = ["➕ Add User", "🚫 Remove User"])

    if add_or_remove_user == '➕ Add User' :

        # profile_pic = st.file_uploader(
        #     key = "_profile_pic_uploader",
        #     label = "Select Profile Photo",
        #     type = ['png', 'jpg'],
        #     help = "Upload User Profile Picture",
        # )

        username = st.text_input(
            label = "Enter Username",
            placeholder = "ex: user123",
        )

        password = st.text_input(
            label = "Enter Password",
            type = "password",  
        )

        retyped_password = st.text_input(
            label = "Retype Password",
            type = "password", 
        )

    if add_or_remove_user == '🚫 Remove User' :
        pass 

    if st.form_submit_button("Submit", type = 'primary' ):
        if password == retyped_password:
            user = {
                "username": username,
                "password": password
            }
            # response = requests.post("http://localhost:8508", json = user)
            st.success('User Added Sucessfully', icon="✅")
        else:
            st.warning("Passwords did not match", icon = "⚠️")
            
