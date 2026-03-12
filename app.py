import streamlit as st
import subprocess

st.title("🤖 Autonomous AI Curation Agent")
st.write("Welcome to my RAG Pipeline! Click the button below to generate today's briefing.")

if st.button("Generate Today's News"):
    st.info("Fetching data and generating AI briefing... Please wait.")
    
    try:
        # 1. Fetch the latest developer and entertainment data in the background
        subprocess.run(["python", "run_pipeline.py"])
        
        # 2. Generate the briefing via AI and bring the output directly to the website (No file needed!)
        briefing = subprocess.getoutput("python generate_briefing.py")
        
        st.success("Briefing Generated Successfully!")
        st.markdown(briefing)
        
    except Exception as e:
        st.error("An error occurred. Please check the terminal for details.")