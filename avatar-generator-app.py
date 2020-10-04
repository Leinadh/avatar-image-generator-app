import streamlit as st
from PIL import Image
from streamlit_cropper import st_cropper
from time import sleep

st.title('Avatar Image Generator')
st.subheader("Here you can create a virtual avatar based on your appearance. Just upload a picture of your face below, crop it, and you're done!")
st.write('')

st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader(
    'Please upload a selfie.', type=['jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.write('')
    st.write("Let's crop it!")
    cropped_img = st_cropper(image, aspect_ratio=(1, 1), box_color='#FF0000')

    st.write('')
    button_start = st.button('Generate image')
    st.write('')

    if button_start:
        with st.spinner(text='Generating avatar...'):
            sleep(5)
            img_cartoon = cropped_img  # img_cartoon = model.predict(cropped_img)
        st.image(img_cartoon, caption='Your avatar.',
                 use_column_width=True)
        st.balloons()

st.write('This is a demo of [our project](https://madewithml.com/projects/1233/generating-avatars-from-real-life-pictures/) created for the Made With ML Data Science Incubator.')
