import streamlit

streamlit.set_page_config(layout='wide')

col1, col2 = streamlit.columns(2)

with col1:
    streamlit.image('images/photo.jpg', width=300)

with col2:
    streamlit.title('Łukasz Gurgul')
    content = '''
    Hi! I am Łukasz Gurgul
    '''
    streamlit.write(content)