import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import os


st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## IMAGE BACKGROUND REMOVER")
MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im

def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("BG Removed Image :wrench:")
    col2.image(fixed)

    return fixed

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        # Include fix_image in the cache
        fixed_image = fix_image(upload=my_upload)

        # Convert the fixed image for downloading
        fixed_image_data = convert_image(fixed_image)

        st.sidebar.markdown("\n")
        st.download_button("Download image", fixed_image_data, "fixed.jpeg", "image/png")
        nk21_button = st.button("NK21❤️")

        if nk21_button:
                st.balloons()
st.sidebar.markdown(
    """
    **Developer:** NK21
    https://t.me/technicalsagar7
    """
)
