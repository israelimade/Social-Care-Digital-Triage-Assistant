import streamlit as st
from core.rules import red_flags, suggest_signposts
from core.schemas import Intake

st.set_page_config(page_title="Social Care Digital Triage Assistant")

st.title("Social Care Digital Triage Assistant (Prototype)")
st.write("This is an information and signposting tool. It does not make eligibility decisions.")

with st.form("triage"):
    age_band = st.selectbox("Age range (optional)", ["Prefer not to say","18–34","35–49","50–64","65–74","75+"])
    falls = st.radio("Any falls in the last 6 months?", ["No", "Yes, no injury", "Yes, with injury"])
    bathing = st.selectbox("Bathing difficulty", ["None", "Some", "Unable without help"])
    stairs = st.selectbox("Stairs at home", ["No stairs", "One step", "Multiple steps"])
    carer_strain = st.selectbox("Carer strain", ["No carer", "Manageable", "Significant strain"])
    hazards = st.multiselect("Any home hazards?", ["Poor lighting","Loose rugs","Cold rooms","Damp or mould","Exposed wiring"])
    submitted = st.form_submit_button("Get guidance")

if submitted:
    intake = Intake(
        age_band=age_band if age_band!="Prefer not to say" else None,
        falls=falls, bathing=bathing, stairs=stairs,
        carer_strain=carer_strain, hazards=hazards
    )
    alerts = red_flags(intake)
    tips = suggest_signposts(intake)

    if alerts:
        st.error("Urgent. Contact your council or GP or 111. If you are in immediate danger call 999.")
        for a in alerts:
            st.write(f"• {a}")

    st.subheader("Things you can try now")
    for t in tips:
        st.write(f"• {t}")

    st.caption("This prototype stores no personal data.")
