import streamlit as st

st.set_page_config(page_title="Cannabis Bill Generator", layout="centered")

st.title("⚖️ Cannabis Bill Generator")
st.markdown("""Type in a cannabis-related policy issue, and this app will generate a legislative draft to propose a new bill or amend existing law in Connecticut.
""")

# Input form
issue = st.text_area("📝 Describe the cannabis-related issue", placeholder="E.g. Medical patients are being denied home grow rights...")

action_type = st.selectbox("What kind of bill do you want?", ["New bill", "Amendment to existing law"])

submit = st.button("📜 Draft Legislation")

# GPT-style bill generator logic (simulated for now)
def generate_bill(issue, action):
    title = f"An Act Concerning {issue[:80].strip().capitalize()}"
    preamble = f"Be it enacted by the Senate and House of Representatives in General Assembly convened:\n\n"
    section_1 = f"Section 1. (NEW) Effective October 1, 2025, the following provisions shall apply regarding {issue.lower()}."
    section_2 = f"Section 2. The Department of Consumer Protection shall develop regulations to enforce and support this act."
    rationale = f"// This draft is based on an issue involving: {issue}. Tailored for Connecticut General Assembly 2025 session."

    if action == "Amendment to existing law":
        section_1 = f"Section 1. Subsection (a) of section 21a-408 of the general statutes is amended to include:\n\"{issue}.\""

    return title, preamble + section_1 + "\n\n" + section_2, rationale

# Output draft
if submit and issue.strip():
    title, body, note = generate_bill(issue, action_type)
    st.subheader("📘 Drafted Bill")
    st.markdown(f"### {title}")
    st.code(body, language="markdown")
    st.caption(note)
else:
    st.info("Enter a cannabis policy issue and click 'Draft Legislation'.")