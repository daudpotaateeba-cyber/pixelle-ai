import streamlit as st
from collections import Counter

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

    .stApp {
        background: linear-gradient(
            135deg,
            #fbf8ff 0%,
            #f1eaff 100%
        );
    }

    .main .block-container {
        max-width: 850px;
        padding-top: 3.5rem;
        padding-bottom: 4rem;
    }

    .sparkle {
        text-align: center;
        font-size: 1.4rem;
        letter-spacing: 7px;
        color: #a88bc9;
        margin-bottom: 0.5rem;
    }

    h1 {
        text-align: center;
        font-size: 2.8rem !important;
        font-weight: 750;
        letter-spacing: -1px;
        color: #8b6bb3;
        margin-bottom: 0.5rem;
    }

    p {
        color: #6f6872;
    }

    .summary-box {
        background: rgba(255,255,255,0.75);
        border: 1px solid #ddcfee;
        border-radius: 22px;
        padding: 1.3rem 1.5rem;
        margin: 1.5rem 0;
        box-shadow: 0 6px 20px rgba(120,90,160,0.10);
    }

    .summary-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #8b6bb3;
        margin-bottom: 0.6rem;
    }

    .object-line {
        font-size: 1rem;
        color: #6f6872;
        margin: 0.25rem 0;
    }

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
        box-shadow: 0 6px 20px rgba(120,90,160,0.20) !important;
    }

    .stButton > button *,
    .stButton > button p,
    .stButton > button span,
    .stButton > button div {
        color: #ffffff !important;
    }

    .stButton > button:hover {
        background-color: #76559e !important;
        transform: translateY(-2px);
    }

    [data-testid="stAlert"] {
        background: #f3ebff !important;
        border: 1px solid #d9c8ec !important;
        border-radius: 18px !important;
        color: #76559e !important;
    }

    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #aaa2aa;
        font-size: 0.8rem;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# HEADER
# -----------------------------

st.markdown(
    '<div class="sparkle">✦ ˚ ✧ ˚ ✦</div>',
    unsafe_allow_html=True
)

st.title("Pixelle found these ✦")


# -----------------------------
# CHECK RESULTS
# -----------------------------

if "result" not in st.session_state:
    st.warning("No detection results found yet. ♡")

    if st.button("Upload an image"):
        st.switch_page("pages/1_📷_Upload.py")

else:

    result = st.session_state["result"]

    # -----------------------------
    # SHOW DETECTED IMAGE
    # -----------------------------

    plotted_image = result.plot()

    st.image(
        plotted_image,
        caption="Pixelle's detections ✦"
    )

    # -----------------------------
    # COUNT OBJECTS
    # -----------------------------

    class_ids = result.boxes.cls.tolist()

    detected_names = [
        result.names[int(class_id)]
        for class_id in class_ids
    ]

    object_counts = Counter(detected_names)

    total_objects = len(detected_names)

    # -----------------------------
    # SUMMARY
    # -----------------------------

    if total_objects > 0:

        st.markdown(
            f"""
            <div class="summary-box">
                <div class="summary-title">
                    Pixelle found {total_objects} object{"s" if total_objects != 1 else ""} ✦
                </div>
            """,
            unsafe_allow_html=True
        )

        for object_name, count in object_counts.items():
            st.markdown(
                f"""
                <div class="object-line">
                    • {object_name.title()} × {count}
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )

    else:

        st.info(
            "Pixelle couldn't confidently detect any objects in this image. ♡"
        )

    # -----------------------------
    # CONFIDENCE DETAILS
    # -----------------------------

    st.markdown("### Detection details")

    if total_objects > 0:

        confidences = result.boxes.conf.tolist()

        for object_name, confidence in zip(
            detected_names,
            confidences
        ):
            st.write(
                f"✦ {object_name.title()} — {confidence * 100:.1f}% confidence"
            )

    # -----------------------------
    # TRY AGAIN BUTTON
    # -----------------------------

    if st.button("Analyze another image ✦"):
        st.switch_page("pages/1_📷_Upload.py")


# -----------------------------
# FOOTER
# -----------------------------

st.markdown(
    '<div class="footer">'
    'Pixelle · your little AI image detective ✦'
    '</div>',
    unsafe_allow_html=True
)
