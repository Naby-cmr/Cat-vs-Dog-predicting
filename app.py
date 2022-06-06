import streamlit as st 
import numpy as np
from PIL import Image
from classify import predict


st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    uploaded_file = Image.open(uploaded_file)
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)
    uploaded_file = np.array(uploaded_file)
    st.write("")
    

submit = st.button("👉🏼 Predict")



def generate_result(prediction):
    # st.write("""## 🎯 RESULT""")
	if prediction[0] < 0.6:
		st.write("""## Model predicts it as an image of a CAT 🐱 !!!""")
	else:
		st.write("""## Model predicts it as an image of a DOG 🐶 !!!""")


if submit:
	predicts = predict(uploaded_file)
	generate_result(predicts)

