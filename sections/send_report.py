from io import StringIO
import streamlit as st

# modules for validating email
from validate_email import validate_email_or_fail
from validate_email.exceptions import EmailValidationError

from custom_packages.email_operations import send_email

st.markdown("# Mail Report :envelope:")
st.markdown("***")

with st.form(key = "_add_exp_form"):
    st.markdown("### Send Report Form :speech_balloon:")
    recepient_email = st.text_input(label = "Recepient Email Address", placeholder = "jhondoe@example.com")
    email_subject = st.text_input(label = "Enter Subject", placeholder = "Expense Statistics with Attached Report ")
    email_body = st.text_area(label = "Email Body(Max 500 Characters)", placeholder = "Hello Sir/Ma'am...", max_chars = 500) 
    email_attachment = st.file_uploader(label = "Add Report File as Attachment", type = ["pdf", "png", "jpg"] )

    sender_email = st.secrets.outlook_credentials.outlook_mail_id
    sender_password = st.secrets.outlook_credentials.outlook_password

    if email_attachment is not None:
        attachment_bytes = email_attachment.getvalue()
        attachment_file_name = email_attachment.name


    if st.form_submit_button("Send", type = 'primary' ):
        # st.write(type(email_attachment))
        # st.write(email_attachment)

        try:
            # checks for validity of email adress first
            validate_email_or_fail(email_address = recepient_email, dns_timeout = 20)

            # the mail is sent only if the email validation passes
            send_email(
                sender_email,
                sender_password,
                recepient_email,
                email_subject,
                email_body,
                # email_attachment,
                attachment_bytes,
                attachment_file_name
            )
        except EmailValidationError as email_err:
            st.warning("Invalid Email Address", icon = "🚫")
            # st.write(email_err)
        except Exception as exception:
            st.warning("Unable to Send Email, An Error Occoured", icon = "🚫")
            # st.write(exception)
