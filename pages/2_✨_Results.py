import streamlit as st

st.set_page_config(
    page_title="Pixelle | Results",
    page_icon="✦",
    layout="centered"
)

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

    /* Image */
    [data-testid="stImage"] {
        border-radius: 18px;
        overflow: hidden;
        margin-top: 1.5rem;
    }

    /* -------------------------
       PIXELLE BUTTON
       ------------------------- */

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

    /* Force ALL button text to white */
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

    /* Section headings */
    h2, h3 {
        color: #76559e !important;
    }

    /* -------------------------
       LILAC INFO / WARNING BOX
       ------------------------- */

    [data-testid="stAlert"] {
        background: #f3ebff !important;
        border: 1px solid #d9c8ec !important;
        border-radius: 18px !important;
        color: #76559e !important;
    }

    [data-testid="stAlert"] p {
        color: #76559e !important;
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

st.title("Pixelle found... ♡")

st.write("Here's what I detected in your image.")


# -----------------------------
# RESULTS
# -----------------------------

if "result" in st.session_state:

    result = st.session_state["result"]

    st.image(
        result.plot(),
        caption="Pixelle's detection ✦"
    )

    st.subheader("Detected objects ♡")

    if len(result.boxes) == 0:

        st.info(
            "Hmm... Pixelle couldn't recognize any objects "
            "in this image. ♡"
        )

    else:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])
            name = result.names[class_id]

            st.write(
                f"**{name.title()}** — "
                f"{confidence:.0%} confidence"
            )

else:

    st.warning(
        "Please upload an image first. ♡"
    )


# -----------------------------
# ANALYZE ANOTHER IMAGE
# -----------------------------

st.divider()

if st.button("← Analyze another image"):

    st.switch_page(
        "pages/1_📷_Upload.py"
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
