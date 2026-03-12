import streamlit as st
import subprocess
import sys
import os

st.title("🤖 Autonomous AI Curation Agent")
st.write("Welcome to my RAG Pipeline! Click the button below to generate today's briefing.")

# 🛑 THE MAGIC TRICK: Streamlit ke secrets ko zabardasti system mein daalna
try:
    if "GROQ_API_KEY" in st.secrets:
        os.environ["GROQ_API_KEY"] = st.secrets["GROQ_API_KEY"]
except:
    pass

if st.button("Generate Today's News"):
    st.info("Fetching data and generating AI briefing... Please wait.")
    
    try:
        # Background scripts ab automatically nayi OS key pick karengi
        subprocess.run([sys.executable, "run_pipeline.py"], check=True)
        
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
            st.success("Briefing Generated Successfully!")
            st.markdown(result.stdout)
            
    except Exception as e:
        st.error(f"An error occurred: {e}")