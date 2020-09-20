import streamlit as st
from PIL import Image 
from streamlit_cropper import st_cropper
#import SessionState

st.title('Avatar Image Generator')
st.subheader('This is a face to cartoon generator created for the Made With ML Data Science Incubator.')
st.text('') 

st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader('Please upload a selfie.', type=['jpg', 'jpeg'])


realtime_update = st.checkbox(label="Update in Real Time", value=True)
#box_color = st.beta_color_picker(label="Box Color", value='#0000FF')
aspect_choice = st.radio(label="Aspect Ratio", options=["1:1", "Free"])
aspect_dict = {"1:1": (1,1),
                "Free": None}
aspect_ratio = aspect_dict[aspect_choice]



if uploaded_file is not None:
    image = Image.open(uploaded_file)
    #st.image(image, caption='Uploaded Image.', use_column_width=True)

    if not realtime_update:
        st.write("Double click to save crop")
    # Get a cropped image from the frontend
    cropped_img = st_cropper(image, realtime_update=realtime_update,
                                aspect_ratio=aspect_ratio)


    st.write('')
    st.write('Generarating Avatar...')
    st.write('')

    #session_state = SessionState.get(name = "", button_start = False)
    button_start = st.button('Generate image')

    if button_start:
        #img_cartoon = model.predict(cropped_img)   
        img_cartoon = cropped_img
        st.image(img_cartoon, caption='Generated Image.', use_column_width=True)