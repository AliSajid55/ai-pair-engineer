import streamlit as st
import json
from src.reviewer import review_code

st.set_page_config(page_title="AI Pair Engineer", layout="wide")
st.title("AI Pair Engineer")
st.caption("Paste code → get design flaws, tests, and refactor patch (JSON-backed).")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    language = st.selectbox("Language", ["python", "javascript", "typescript", "java", "cpp", "go"])
    extra = st.text_area("Extra context (optional)", placeholder="e.g., This is a FastAPI endpoint. Must be backward compatible.")
    code = st.text_area("Paste your code", height=420, placeholder="Paste code here...")

    run = st.button("Review", type="primary", use_container_width=True)

with col2:
    if run:
        if not code.strip():
            st.error("Paste code first.")
        else:
            with st.spinner("Reviewing..."):
                result = review_code(language, code, extra)

            st.subheader("Summary")
            st.write(result.get("summary", ""))

            st.subheader("Design flaws")
            flaws = result.get("design_flaws", [])
            if flaws:
                for f in flaws:
                    sev = f.get("severity", "minor")
                    st.markdown(f"**[{sev.upper()}] {f.get('title','')}**")
                    st.write(f.get("why_it_matters",""))
                    st.code(f.get("evidence",""), language=language)
                    st.write("**Fix:** " + f.get("fix",""))
                    st.divider()
            else:
                st.info("No flaws listed.")

            st.subheader("Tests")
            tests = result.get("tests", [])
            if tests:
                for t in tests:
                    st.markdown(f"**({t.get('type','unit')}) {t.get('title','')}**")
                    st.write(t.get("what_to_test",""))
                    st.code(t.get("example_test_code",""), language=language)
                    st.divider()
            else:
                st.info("No tests listed.")

            st.subheader("Refactor patch")
            ref = result.get("refactor", {})
            goals = ref.get("goals", [])
            if goals:
                st.write("Goals:")
                st.write("- " + "\n- ".join(goals))
            st.code(ref.get("patch",""), language=language)

            st.subheader("Raw JSON Output")
            json_str = json.dumps(result, indent=2)
            st.code(json_str, language="json")
            st.download_button(
                label="Download JSON",
                data=json_str,
                file_name="review.json",
                mime="application/json",
            )

            if "_error" in result:
                st.warning(f"JSON parse issue: {result['_error']}")
                st.text_area("Raw output", value=result.get("_raw",""), height=200)
    else:
        st.info("Paste code and click Review button")