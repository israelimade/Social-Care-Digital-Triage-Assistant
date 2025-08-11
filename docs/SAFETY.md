# Safety and Guardrails

This project is an information and signposting prototype for adult social care. It does not make eligibility decisions or give medical advice. It must be used with care to protect users and staff.

## Purpose
Help people prepare for adult social care by collecting structured information, highlighting clear risks, and pointing to trusted resources.

## Scope
- Pre-triage questions about daily activities, home environment, falls, carers
- Simple rules that surface obvious risks
- Signposting to public services and community support
- Local demo mode only, no data retention

## Non goals
- No eligibility or funding decisions
- No diagnosis or clinical advice
- No replacement for safeguarding processes
- No storage of personal data in the demo

## Guardrails
1. Safeguarding first. If immediate risk is indicated, show urgent routes and advise calling 999 for danger, 111 or GP for non-emergency.
2. Information only. Output is guidance and signposting. Never state that someone is eligible or ineligible.
3. Plain language. Keep content clear, specific, and respectful.
4. Data minimisation. Only ask what is needed to produce safe guidance. Do not store personal data in demo mode.
5. Transparency. Keep rules simple and visible in code. Document changes in pull requests.
6. Accessibility. Aim for WCAG 2.2 AA. Support keyboard navigation, screen readers, and mobile use.

## Red flag responses
The rules should trigger urgent messaging when any of the following appear:
- Fall with injury or head impact
- Electrical hazards such as exposed wiring
- Significant carer strain or risk of breakdown
- Safeguarding concerns about abuse or neglect
- Unsafe environment affecting transfers or toileting

When triggered, the app must:
- Show an urgent banner with the correct action: 999 for danger, 111 or GP for non-emergency, council safeguarding contact for concerns
- Avoid collecting sensitive details beyond what is necessary to display the right routes
- Remind users that this tool does not store their information

## Content sourcing
- Link only to trusted sources such as NHS, GOV.UK, local authorities, Age UK, Turn2us
- Review links at least quarterly
- Avoid affiliate links or commercial upsell

## Privacy and data
- Demo mode stores nothing
- If storage is added later, require a DPIA, retention schedule, access controls, and a privacy notice
- Never commit sample data with personal information to the repository

## Clinical safety note
- This tool does not replace professional judgment
- If in doubt, advise the user to contact their council adult social care team, GP, or NHS 111

## Change control
- Describe safety impact in every pull request that changes rules or wording
- Add or update unit tests for red flag logic
- Keep a simple changelog in the README for user facing behaviour

## Incident handling
If someone reports harmful advice, unsafe content, or a broken rule:
- Acknowledge and create a GitHub issue with a clear title and reproduction steps
- Patch within 24 to 72 hours depending on severity
- Add a test to prevent regression
