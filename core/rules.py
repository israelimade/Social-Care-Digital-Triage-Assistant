from .schemas import Intake

def red_flags(i: Intake):
    alerts = []
    if "Yes, with injury" in i.falls:
        alerts.append("Recent fall with injury. Seek clinical review and a home safety check.")
    if i.carer_strain == "Significant strain":
        alerts.append("Carer strain. Ask for a carers assessment and urgent support planning.")
    if "Exposed wiring" in i.hazards:
        alerts.append("Electrical hazard. Contact landlord or council repairs. Risk of injury.")
    return alerts

def suggest_signposts(i: Intake):
    tips = []
    if i.bathing != "None":
        tips.append("Consider a bath board or shower seat. Ask for an OT assessment via your local council.")
    if "Loose rugs" in i.hazards or i.falls.startswith("Yes"):
        tips.append("Falls prevention. Remove trip hazards and request a home hazard check from the OT team.")
    if "Cold rooms" in i.hazards:
        tips.append("Warm Home Discount and ECO4 schemes. Contact your council for energy efficiency support.")
    tips.append("Learn about Disabled Facilities Grants for home adaptations on your council website.")
    return tips
