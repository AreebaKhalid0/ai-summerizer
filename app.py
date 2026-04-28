import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Summarizer", page_icon="📝")
st.title("📝 AI Trend Summarizer")

# Sidebar for API Key
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

if api_key:
    try:
        # 'rest' transport use karne se puranay errors khatam ho jate hain
        genai.configure(api_key=api_key, transport='rest')
        
        # Sab se stable model use kar rahay hain
        model = genai.GenerativeModel('gemini-pro')
        
        user_text = st.text_area("Paste text here:", height=200)

        if st.button("Analyze Now"):
            if user_text:
                with st.spinner("AI is thinking..."):
                    # Seedha prompt bhej rahay hain bina extra configuration ke
                    response = model.generate_content(f"Summarize this text in points: {user_text}")
                    st.subheader("Summary Result:")
                    st.write(response.text)
            else:
                st.warning("Please paste some text first.")
    except Exception as e:
        st.error(f"System Note: {e}")
else:
    st.info("Enter your Gemini API Key in the sidebar to start.")
