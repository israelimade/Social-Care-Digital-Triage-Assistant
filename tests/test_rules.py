from core.schemas import Intake
from core.rules import red_flags, suggest_signposts

def test_red_flag_fall_with_injury_triggers_alert():
    i = Intake(
        age_band="75+",
        falls="Yes, with injury",
        bathing="Some",
        stairs="Multiple steps",
        carer_strain="Manageable",
        hazards=[]
    )
    alerts = red_flags(i)
    assert any("fall with injury" in a.lower() for a in alerts)

def test_red_flag_electrical_hazard_triggers_alert():
    i = Intake(
        age_band=None,
        falls="No",
        bathing="None",
        stairs="No stairs",
        carer_strain="No carer",
        hazards=["Exposed wiring"]
    )
    alerts = red_flags(i)
    assert any("electrical hazard" in a.lower() for a in alerts)

def test_carer_strain_triggers_alert():
    i = Intake(
        age_band=None,
        falls="No",
        bathing="None",
        stairs="No stairs",
        carer_strain="Significant strain",
        hazards=[]
    )
    alerts = red_flags(i)
    assert any("carer strain" in a.lower() for a in alerts)

def test_signposts_include_adaptations_and_falls_support():
    i = Intake(
        age_band="65–74",
        falls="Yes, no injury",
        bathing="Unable without help",
        stairs="One step",
        carer_strain="Manageable",
        hazards=["Loose rugs", "Cold rooms"]
    )
    tips = " ".join(suggest_signposts(i)).lower()
    assert "disabled facilities grants" in tips
    assert "falls prevention" in tips
    assert "energy efficiency" in tips or "warm home discount" in tips
