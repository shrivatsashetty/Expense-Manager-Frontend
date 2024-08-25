import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import streamlit as st

def send_email(sender_email, sender_password, recepient_email, email_subject, email_body, attached_file_bytes, attached_file_name) -> None:

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recepient_email
    message['Subject'] = email_subject

    #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(email_body, 'plain'))

    payload = MIMEBase("application", "octet-stream")
    # since the attachment is already coming in the form of bytes,
    # we do not need to further convert the file to Bytes.io
    payload.set_payload(attached_file_bytes) 

    encoders.encode_base64(payload) #encode the attachment

    #add payload header with filename
    payload.add_header("Content-Disposition", f"attachment; filename= {attached_file_name}")
    message.attach(payload)

    #Create SMTP session for sending the mail
    # we make use of the Outlook email
    with smtplib.SMTP('smtp.office365.com', 587) as session:
        session = smtplib.SMTP('smtp.office365.com', 587) #use gmail with port
        session.ehlo()
        session.starttls() #enable security
        session.login(sender_email, sender_password) # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_email, recepient_email, text)

    # display a sucess message if the message is sent
    st.success("Report Sent!!!", icon = "📤")