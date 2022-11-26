import streamlit

streamlit.header('Contact Me')

with streamlit.form(key='email_form'):
    user_email = streamlit.text_input('Your email address: ')
    message = streamlit.text_area('Your message: ')
    button = streamlit.form_submit_button('Submit')
    if button:
        pass