import streamlit as st
import subprocess
import sys

st.title("🤖 Autonomous AI Curation Agent")
st.write("Welcome to my RAG Pipeline! Click the button below to generate today's briefing.")

if st.button("Generate Today's News"):
    st.info("Fetching data and generating AI briefing... Please wait.")
    
    try:
        # 1. Fetch data in the background (List format handles spaces safely)
        subprocess.run([sys.executable, "run_pipeline.py"], check=True)
        
        # 2. Generate the briefing via AI and capture output safely
        result = subprocess.run(
            [sys.executable, "generate_briefing.py"], 
            capture_output=True, 
            text=True,
            encoding='utf-8' # Yeh emojis ko bhi safe rakhega
        )
        
        # Check agar script mein koi error aaya ho
        if result.returncode != 0:
            st.error("Error in generating briefing. AI Logs:")
            st.code(result.stderr)
        else:
            st.success("Briefing Generated Successfully!")
            st.markdown(result.stdout)
            
    except Exception as e:
        st.error(f"An error occurred: {e}")