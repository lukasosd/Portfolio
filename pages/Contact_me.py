import streamlit
from send_email import send_email


streamlit.header('Contact Me')

with streamlit.form(key='email_form'):
    user_email = streamlit.text_input('Your email address: ')
    raw_message = streamlit.text_area('Your message: ')
    message = f'Subject: Contact from Portfolio\n{raw_message} \nFrom: {user_email}'
    button = streamlit.form_submit_button('Submit')
    if button:
        send_email(message)
        streamlit.info('Your email has been sent successfully!')