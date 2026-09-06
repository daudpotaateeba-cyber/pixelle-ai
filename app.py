import streamlit as st

st.set_page_config(
    page_title="Pixelle",
    page_icon="✦",
    layout="centered"
)

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
        padding-top: 4rem;
        padding-bottom: 4rem;
    }

    /* Sparkles */
    .sparkle {
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
        letter-spacing: 8px;
        color: #a88bc9;
    }

    /* Title */
    h1 {
        text-align: center;
        font-size: 3.2rem !important;
        font-weight: 750;
        letter-spacing: -1.5px;
        margin-bottom: 0.5rem;
        color: #8b6bb3;
    }

    /* Subtitle */
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #6f6872;
        margin-bottom: 0.3rem;
    }

    /* Description */
    .description {
        text-align: center;
        font-size: 0.95rem;
        color: #9a929c;
        margin-bottom: 2.5rem;
    }

    /* Button */
    .stButton {
        text-align: center;
    }

    .stButton > button {
        border-radius: 999px;
        padding: 0.75rem 2.2rem;
        font-size: 1rem;
        font-weight: 650;
        color: white;
        border: none;
        background: #8b6bb3;
        box-shadow: 0 6px 20px rgba(120, 90, 160, 0.20);
        transition: 0.2s ease;
    }

    /* Button hover */
    .stButton > button:hover {
        transform: translateY(-2px);
        background: #76559e;
        box-shadow: 0 9px 25px rgba(120, 90, 160, 0.25);
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


# Sparkles
st.markdown(
    '<div class="sparkle">✦ ˚ ✧ ˚ ✦</div>',
    unsafe_allow_html=True
)


# Main title
st.title("Welcome to Pixelle ♡")


# Subtitle
st.markdown(
    '<div class="subtitle">'
    'Let’s see what’s hiding in your image.'
    '</div>',
    unsafe_allow_html=True
)


# Description
st.markdown(
    '<div class="description">'
    'Your little AI image detective ✨'
    '</div>',
    unsafe_allow_html=True
)


# Start button
if st.button("Get Started  →"):
    st.switch_page("pages/1_📷_Upload.py")


# Footer
st.markdown(
    '<div class="footer">'
    'powered by AI · made with ♡'
    '</div>',
    unsafe_allow_html=True
)