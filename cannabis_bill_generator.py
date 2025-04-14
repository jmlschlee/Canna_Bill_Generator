import streamlit as st

st.set_page_config(page_title="Cannabis Bill Generator", layout="centered")

st.title("⚖️ Cannabis Bill Generator")
st.markdown("""
Type in a cannabis-related policy issue and generate a legislative draft using Connecticut-style legal language. You can simulate GPT-backed drafting, cite CT statutes, and export or comment on your proposal.
""")

# Inputs
issue = st.text_area("📝 Describe the cannabis-related issue", placeholder="E.g. Patients are being denied home grow rights.")
action_type = st.selectbox("Bill type", ["New bill", "Amendment to existing law"])
jurisdiction = st.selectbox("📚 Legal Format", ["Connecticut General Assembly", "Federal Congress", "Municipal Ordinance"])
include_notes = st.checkbox("📎 Add rationale and references", value=True)

gpt_simulated = st.checkbox("🤖 Use GPT-style drafting (simulated)", value=True)
submit = st.button("📜 Generate Bill")

# Mock GPT function
def gpt_draft(issue, action, jurisdiction):
    key_line = f"This draft addresses the cannabis-related concern: '{issue}'"
    if "home grow" in issue.lower():
        line = "This act affirms the right of registered medical cannabis patients to cultivate up to six plants at home."
    else:
        line = "The act shall ensure rights, access, or enforcement mechanisms tied to this concern."
    return f"{key_line}\n\n{line}\n\nAdditional sections may be appended after stakeholder review."

# Build draft
def draft_bill(issue, action_type, jurisdiction, with_notes=True, gpt=False):
    title = f"An Act Concerning {issue[:60].strip().capitalize()}"
    if action_type == "Amendment to existing law":
        section = f"Section 1. Subsection (a) of section 21a-408 of the general statutes is amended to include:\n\"{issue}.\""
    else:
        if jurisdiction == "Federal Congress":
            section = f"Section 1. SHORT TITLE. This Act may be cited as the \"{issue.title()} Act of 2025\".\nSection 2. Congress finds that {issue.lower()} impacts public policy."
        else:
            section = f"Section 1. (NEW) Effective October 1, 2025:\n(a) The following provisions apply regarding {issue.lower()}.\n(b) DCP shall enforce compliance."

    if gpt:
        gpt_inserts = gpt_draft(issue, action_type, jurisdiction)
        section += f"\n\n// GPT Draft Insert:\n{gpt_inserts}"

    foot = f"// Notes: Generated for {jurisdiction} format using cannabis advocacy AI draft tool." if with_notes else ""
    return title, section, foot

# Output
if submit and issue.strip():
    title, text, foot = draft_bill(issue, action_type, jurisdiction, include_notes, gpt_simulated)
    st.subheader("📘 Draft Output")
    st.markdown(f"### {title}")
    st.code(text, language="markdown")
    if foot:
        st.caption(foot)

    st.text_input("💬 Public comment (optional):", placeholder="Enter your feedback or suggested changes here...")
    st.button("📤 Submit to Advocate Portal (simulated)")
else:
    st.info("Enter a cannabis issue to generate a draft.")