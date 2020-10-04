import streamlit as st
from PIL import Image 
from streamlit_cropper import st_cropper
#import SessionState

st.title('Avatar Image Generator')
st.subheader("Here you can create a virtual avatar based on your appearance. Just upload a picture of your face below, crop it, and you're done!") 


st.set_option('deprecation.showfileUploaderEncoding', False)
uploaded_file = st.file_uploader('Please upload a selfie.', type=['jpg', 'jpeg'])


# st.text('') 
# realtime_update = st.checkbox(label="Update in real time", value=True)
#box_color = st.beta_color_picker(label="Box Color", value='#0000FF')
# aspect_choice = st.radio(label="Aspect Ratio", options=["1:1", "Free"])
# aspect_dict = {"1:1": (1,1),
#                 "Free": None}
# aspect_ratio = aspect_dict[aspect_choice]


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    #st.image(image, caption='Uploaded Image.', use_column_width=True)

    # if not realtime_update:
    #     st.write("Double click to save crop")
    # Get a cropped image from the frontend
    st.write("Let's crop it!")
    cropped_img = st_cropper(image, aspect_ratio=(1,1))


    

    #session_state = SessionState.get(name = "", button_start = False)
    st.write('')
    button_start = st.button('Generate image')
    st.write('')

    
    st.write('Generarating Avatar...')
    if button_start:
        #img_cartoon = model.predict(cropped_img)   
        img_cartoon = cropped_img
        st.image(img_cartoon, caption='Generated Image.', use_column_width=True)


st.write('')
st.write('')
st.write('This is a face to cartoon generator created for the Made With ML Data Science Incubator.')