import streamlit as st
from PIL import Image 

st.title('Avatar Image Generator')
st.subheader('This is a face to cartoon generator created for the Made With ML Data Science Incubator.')
st.text('') 

st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader('Please upload a selfie.', type=['jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write('')
    st.write('Generarating Avatar...')
    st.write('')
    st.image(image, caption='Generated Image.', use_column_width=True)
