import streamlit as st
import subprocess
import sys

st.title("🤖 Autonomous AI Curation Agent")
st.write("Welcome to my RAG Pipeline! Click the button below to generate today's briefing.")

if st.button("Generate Today's News"):
    st.info("Fetching data and generating AI briefing... Please wait.")

    try:
        # 1. Background mein data layega (Sahi Python use karke)
        subprocess.run([sys.executable, "run_pipeline.py"])

        # 2. AI se news generate karwayega aur output layega
        briefing = subprocess.getoutput(f"{sys.executable} generate_briefing.py")

        st.success("Briefing Generated Successfully!")
        st.markdown(briefing)

    except Exception as e:
        st.error("Kuch gadbad hui. Terminal check karein.")