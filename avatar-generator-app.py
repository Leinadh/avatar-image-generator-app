import streamlit as st
from PIL import Image
from streamlit_cropper import st_cropper
from time import sleep
from avatar_generator_model import Avatar_Generator_Model 

st.title('Avatar Image Generator')
st.subheader("Here you can create a virtual avatar based on your appearance. Just upload a picture of your face below, crop it, and you're done!")
st.write('')

st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader(
    'Please upload a selfie.', type=['jpg', 'jpeg'])
st.write('')

model = Avatar_Generator_Model()
model.load_weights()

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.write("Let's crop it!")
    st.write('')
    cropped_img = st_cropper(image, aspect_ratio=(1, 1), box_color='#FF0000')

    st.write('')
    button_generate = st.button('Generate image', key=3)
    st.write('')

    if button_generate:
        with st.spinner(text='Generating avatar...'):
            img_cartoon = model.generate(cropped_img)  # img_cartoon = model.predict(cropped_img)
            sleep(5)
        st.image(img_cartoon, caption='Your avatar.',
                 use_column_width=True)
        st.balloons()

st.write('This is a demo of [our project](https://madewithml.com/projects/1233/generating-avatars-from-real-life-pictures/) created for the Made With ML Data Science Incubator.')
