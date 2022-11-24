import streamlit
import pandas

streamlit.set_page_config(layout='wide')

col1, col2 = streamlit.columns([0.8, 2])

with col1:
    streamlit.image('images/photo.jpg', width=300,)

with col2:
    streamlit.title('Łukasz Gurgul')
    content = '''
    Hi! I am Łukasz Gurgul
    '''
    streamlit.write(content)

text = '''
Below you can find some of the apps I have built in Python. Feel free to contact me!
'''

streamlit.write(text)

df = pandas.read_csv('data.csv', sep=';')

col3, empty_column, col4 = streamlit.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        streamlit.header(row['title'])
        streamlit.write(row['description'])
        imagepath = 'images/' + row['image']
        streamlit.image(imagepath)
        streamlit.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        streamlit.header(row['title'])
        streamlit.write(row['description'])
        imagepath = 'images/' + row['image']
        streamlit.image(imagepath)
        streamlit.write(f'[Source Code]({row["url"]})')