import streamlit as st
from app import generate_response

# Page config
st.set_page_config(
    page_title="ఉత్సవ మిత్ర - Festival Friend",
    page_icon="🎉",
    layout="centered",
)

# Custom CSS for Indian Hindu theme colors & styles
st.markdown(
    """
    <style>
    /* Background gradient inspired by traditional festive colors */
    .stApp {
        background: linear-gradient(135deg, #FCEABB, #F8B500);
        color: #3E2723;
        font-family: 'Noto Serif', serif;
    }

    /* Title styles */
    .title {
        font-size: 4rem !important;
        color: #D84315;
        font-weight: 700;
        text-shadow: 1px 1px 2px #BF360C;
    }

    /* Subtitle styles */
    .subtitle {
        font-size: 1.5rem !important;
        color: #6D4C41;
        margin-bottom: 1.5rem;
        font-style: italic;
    }

    /* Input box style */
    .stTextInput>div>div>input {
        border-radius: 10px;
        border: 2px solid #D84315;
        padding: 10px 15px;
        font-size: 1.1rem;
        color: #3E2723;
        background-color: #FFF3E0;
    }

    /* Button colors */
    div.stButton > button:first-child {
        background-color: #D84315;
        color: white;
        font-weight: 600;
        border-radius: 12px;
        padding: 0.5rem 1.5rem;
        transition: background-color 0.3s ease;
    }

    div.stButton > button:first-child:hover {
        background-color: #BF360C;
        color: #FFFDE7;
    }

    /* Response box style */
    .streamlit-expanderHeader {
        font-weight: 700;
        color: #6D4C41 !important;
    }

    p, .css-1d391kg, .css-1oe63nd {
        font-size: 1.15rem;
        color: #4E342E;
        line-height:1.5;
    }

    /* Footer line style */
    hr {
        border-top: 2px solid #D84315;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title and subtitle with styled markdown
st.markdown('<h1 class="title">ఉత్సవ మిత్ర 🎉</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">మీ పండుగల స్నేహితుడు | Your Festival Friend</p>', unsafe_allow_html=True)
st.markdown(
    "<p>భారతదేశంలోని పండుగల గురించి ఏమైనా అడగండి — ప్రత్యేకంగా తెలంగాణలో జరుపుకునేవి!<br>"
    "<small style='color:#6D4C41;'>Ask anything about Indian festivals, especially those celebrated in Telangana!</small></p>", 
    unsafe_allow_html=True
)

# Language selector (English / Telugu)
lang = st.radio(
    "భాష ఎంచుకోండి / Choose your language:",
    options=["English", "తెలుగు"],
    index=1,
    horizontal=True,
    label_visibility="visible"
)

# Input prompt with dynamic label based on language selection
input_label = "మీ ప్రశ్న ఇక్కడ రాయండి... / Write your question here..." if lang == "English" else "మీ ప్రశ్న ఇక్కడ రాయండి..."
user_input = st.text_input(input_label)

if user_input:
    with st.spinner("చూస్తోంది... / Thinking..."):
        reply = generate_response(user_input)
    st.markdown("### ఉత్సవ మిత్ర:")
    st.markdown(f"<p style='background-color:#FFEB3B; border-radius:10px; padding:15px; color:#3E2723;'>{reply}</p>", unsafe_allow_html=True)

# Footer area with separator and credit
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#6D4C41;'>Made with ❤️ for internship project | Data: Telangana Festivals</p>",
    unsafe_allow_html=True
)
