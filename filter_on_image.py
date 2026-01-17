import streamlit as st

from PIL import Image, ImageFilter
st.title("Image Filter Playground")


file = st.file_uploader("Select Image" , type=["jpg","png", "jpeg"])


if file:
    option = st.selectbox("Select Filter",["Original","GreyScale","blur"])

    img= Image.open(file)
    if option=="GreyScale":
        img= img.convert("L")
    if option =="Blur" :
        img = img.filter (ImageFilter.BLUR) 
    st.image(img)      

