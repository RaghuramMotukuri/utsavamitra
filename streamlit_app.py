# streamlit_app.py
import streamlit as st
from app import generate_response

# Page config
st.set_page_config(
    page_title="ఉత్సవ మిత్ర - Festival Friend",
    page_icon="🎉"
)

# Title
st.title("ఉత్సవ మిత్ర 🎉")
st.subheader("మీ పండుగల స్నేహితుడు | Your Festival Friend")
st.write("భారతదేశంలోని పండుగల గురించి ఏమైనా అడగండి — ప్రత్యేకంగా తెలంగాణలో జరుపుకునేవి!")

# Input
user_input = st.text_input("మీ ప్రశ్న ఇక్కడ రాయండి... / Write your question here...")

if user_input:
    with st.spinner("Thinking..."):
        reply = generate_response(user_input)
    st.write("### ఉత్సవ మిత్ర:")
    st.write(reply)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for internship project | Data: Telangana Festivals")