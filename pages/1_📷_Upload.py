import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import pillow_avif
from pillow_heif import register_heif_opener

register_heif_opener()

st.set_page_config(
    page_title="Pixelle | Upload",
    page_icon="✦",
    layout="centered"
)

# Load YOLO
model = YOLO("yolo11n.pt")


# -----------------------------
# PIXELLE STYLE
# -----------------------------

st.markdown("""
<style>

    /* Background */
    .stApp {
        background: linear-gradient(
            135deg,
            #fbf8ff 0%,
            #f1eaff 100%
        );
    }

    /* Main content */
    .main .block-container {
        max-width: 800px;
        padding-top: 3.5rem;
        padding-bottom: 4rem;
    }

    /* Sparkles */
    .sparkle {
        text-align: center;
        font-size: 1.4rem;
        letter-spacing: 7px;
        color: #a88bc9;
        margin-bottom: 0.5rem;
    }

    /* Title */
    h1 {
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 750;
        letter-spacing: -1px;
        color: #8b6bb3;
        margin-bottom: 0.5rem;
    }

    /* Normal text */
    p {
        text-align: center;
        color: #6f6872;
    }

    /* Upload box */
    [data-testid="stFileUploader"] {
        background: rgba(255, 255, 255, 0.65);
        border: 2px dashed #c9b1e5;
        border-radius: 22px;
        padding: 1rem;
        margin-top: 1.5rem;
    }

    /* -------------------------
       PIXELLE BUTTON
       ------------------------- */

    .stButton {
        text-align: center;
    }

    .stButton > button {
        background-color: #8b6bb3 !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 999px !important;
        padding: 0.75rem 2.2rem !important;
        font-size: 1rem !important;
        font-weight: 650 !important;
        box-shadow: 0 6px 20px rgba(120, 90, 160, 0.20) !important;
        transition: 0.2s ease !important;
    }

    /* Force button text to white */
    .stButton > button *,
    .stButton > button p,
    .stButton > button span,
    .stButton > button div {
        color: #ffffff !important;
    }

    /* Button hover */
    .stButton > button:hover {
        background-color: #76559e !important;
        color: #ffffff !important;
        transform: translateY(-2px);
        box-shadow: 0 9px 25px rgba(120, 90, 160, 0.25) !important;
    }

    .stButton > button:hover *,
    .stButton > button:hover p,
    .stButton > button:hover span,
    .stButton > button:hover div {
        color: #ffffff !important;
    }

    /* Image */
    [data-testid="stImage"] {
        border-radius: 18px;
        overflow: hidden;
        margin-top: 1rem;
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #aaa2aa;
        font-size: 0.8rem;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# PAGE CONTENT
# -----------------------------

st.markdown(
    '<div class="sparkle">✦ ˚ ✧ ˚ ✦</div>',
    unsafe_allow_html=True
)

st.title("Let's find out ✦")

st.write(
    "Upload an image and let Pixelle take a look. ♡"
)


# -----------------------------
# UPLOAD IMAGE
# -----------------------------

uploaded_file = st.file_uploader(
    "Choose an image",
    type=[
        "jpg",
        "jpeg",
        "png",
        "webp",
        "bmp",
        "gif",
        "tif",
        "tiff",
        "avif",
        "heic",
        "heif"
    ]
)


# -----------------------------
# IMAGE + DETECTION
# -----------------------------

if uploaded_file:

    try:

        image = Image.open(uploaded_file)
        image = image.convert("RGB")

        st.image(
            image,
            caption="Your image ♡"
        )

        if st.button("Detect Objects ✦"):

            with st.spinner(
                "Pixelle is taking a look... ✦"
            ):

                image_array = np.array(image)

                results = model(image_array)

                result = results[0]

            st.session_state["image"] = image
            st.session_state["result"] = result

            st.switch_page(
                "pages/2_✨_Results.py"
            )

    except Exception:

        st.error(
            "Oops! Pixelle couldn't read this image. "
            "Please try another image file. ♡"
        )


# -----------------------------
# FOOTER
# -----------------------------

st.markdown(
    '<div class="footer">'
    'Pixelle · your little AI image detective ✦'
    '</div>',
    unsafe_allow_html=True
)
