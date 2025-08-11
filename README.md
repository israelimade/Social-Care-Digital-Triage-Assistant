# Social Care Digital Triage Assistant (SCDTA)

Early-stage, open-source project to help people pre-triage adult social care needs and signpost safely. Examples include functional concerns, falls risk, home adaptations, and accessibility. The tool respects Care Act 2014 duties, safeguarding, and data minimisation.

**Status:** Concept and skeleton for collaboration  
**Audience:** OT and social care teams, service designers, govtech engineers

## Why this matters
Local authorities face long triage queues, inconsistent information quality, and high admin overhead. A guided, accessible intake tool can collect better first-contact information, offer low-risk self-management resources, and flag red alerts such as safeguarding or urgent hazards. It does not replace professional judgment.

## What it does (MVP scope)
- Structured pre-assessment of ADLs and IADLs, mobility, cognition and communication, home environment, carers
- Rules-based risk flags for issues like recurrent falls or cold homes
- Signposting to trusted UK resources such as NHS, GOV.UK, local councils, Age UK, Turn2us
- Accessibility first: plain English, WCAG 2.2 AA intent, mobile friendly
- Privacy by default: local only in demo mode

## What it does not do
- No eligibility decisions
- No medical advice
- Does not replace safeguarding processes or assessments

## Architecture plan


Default mode uses rules and forms only. An open-source LLM can be added later to summarise user input for practitioners. No decisions are delegated to AI.

## Guardrails and safety

Golden rules:
1. No eligibility decisions. Output is information and signposting.
2. No medical advice. Direct to 999 or 111 or GP when needed.
3. Safeguarding first. If immediate risk is indicated, show urgent routes. Do not capture sensitive details in demo mode.
4. Data minimisation. Collect only what is necessary. Demo runs local only.
5. Auditability. Rules are transparent and testable.
6. Accessibility. Plain language and screen reader friendly.

Example red flags:
- Recent falls with injury or head impact
- Electrical hazards or severe damp and cold homes
- Safeguarding concerns including abuse or neglect
- Carer breakdown or risk of placement collapse
- Equipment failure affecting transfers or toileting

## Example flow
- About you: optional age band and living situation
- Daily activities and mobility including falls
- Home environment such as steps and bathroom type
- Communication and cognition
- Carers and carer strain
- Signposting to DFG, Attendance Allowance, and local services

## Local setup

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app/main.py
