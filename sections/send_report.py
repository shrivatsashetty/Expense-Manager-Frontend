import streamlit as st

st.markdown("# Send Report :envelope:")
st.markdown("***")

with st.form(key = "_add_exp_form"):
    st.markdown("### Send Report :speech_balloon:")
    email = st.text_input(label = "Email Address", placeholder = "Enter E-Mail Address of the Recepient")
    subject = st.text_input(label = "Enter Subject", placeholder = "Enter Subject for the E-Mail")
    st.file_uploader(label = "Upload the Report File", type = ["pdf", "png", "jpg"])


    if st.form_submit_button("Send", type = 'primary' ):
        st.error('Unable to Send, Invalid Email', icon="⛔")
        st.toast("Fialed to Send, Try Again", icon="⚠️")