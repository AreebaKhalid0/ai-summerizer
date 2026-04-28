import sys
# Ye line Python ko dhoka degi ke wo thora purana version hai
if sys.version_info >= (3, 11):
    import collections
    if not hasattr(collections, 'Mapping'):
        import collections.abc
        collections.Mapping = collections.abc.Mapping
import streamlit as st
import google.generativeai as genai

# Website settings
st.set_page_config(page_title="AI Summarizer", page_icon="📝")
st.title("📝 AI Trend Summarizer")

with st.sidebar:
    st.header("Settings")
    api_key = st.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)

        # Ye naya tareeqa hai model select karne ka
        model = genai.GenerativeModel(model_name='gemini-1.5-flash')

        user_text = st.text_area("Paste text here:", height=200)

        if st.button("Analyze Now"):
            if user_text:
                with st.spinner("AI is thinking..."):
                    # Prompt ko thora clear karte hain
                    response = model.generate_content(user_text)
                    st.subheader("Summary Result:")
                    st.write(response.text)
            else:
                st.warning("Please paste some text first.")
    except Exception as e:
        st.error(f"Error detail: {e}")
else:
    st.info("Please enter your API Key in the sidebar to start.")