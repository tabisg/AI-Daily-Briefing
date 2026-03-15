import streamlit as st
import subprocess
import sys
import os

# Website ka naya title aur icon
st.set_page_config(page_title="Global AI News", page_icon="🌍")

st.title("🌍 Universal AI News Feed")
st.write("Welcome! Click the button below to fetch the latest global trending news in crisp 60-word summaries (Inshorts Style).")

# 🛑 THE MAGIC TRICK: Streamlit ke secrets ko system mein daalna
try:
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
except:
    pass

if st.button("Get Trending News"):
    st.info("Fetching global trends and AI is writing 60-word summaries... Please wait.")
    
    try:
        # Ab seedha generate_briefing chalega (purana pipeline hata diya)
        result = subprocess.run(
            [sys.executable, "generate_briefing.py"], 
            capture_output=True, 
            text=True,
            encoding='utf-8'
        )
        
        if result.returncode != 0:
            st.error("Error in generating briefing. AI Logs:")
            st.code(result.stderr)
        else:
            st.success("Here are your 60-word updates!")
            st.markdown(result.stdout)
            
    except Exception as e:
        st.error(f"An error occurred: {e}")