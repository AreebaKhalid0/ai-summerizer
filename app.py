import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Summarizer", page_icon="📝")
st.title("📝 AI Trend Summarizer")

api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        # Hum gemini-pro use kar rahay hain jo sab se stable hai
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        user_text = st.text_area("Paste text here:", height=200)

        if st.button("Analyze Now"):
            if user_text:
                with st.spinner("AI is thinking..."):
                    response = model.generate_content(f"Summarize this: {user_text}")
                    st.subheader("Summary Result:")
                    st.write(response.text)
            else:
                st.warning("Please paste text.")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info("Enter API Key in sidebar.")
