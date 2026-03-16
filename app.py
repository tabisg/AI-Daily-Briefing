import streamlit as st
import os
# WE IMPORT OUR NEWS GENERATION LOGIC FROM THE OTHER FILE
from generate_briefing import generate_newsletter, generate_audio

# Website Config
st.set_page_config(page_title="Global AI News", page_icon="🌍")

st.title("🌍 Universal AI News Feed")
st.write("Get the latest insights analyzed by AI with Sentiment, Trust Scores, and Audio Podcast!")

# THE LOGIC TO FETCH NEWS AND GENERATE BRIEFING
if st.button("Get Trending News"):
    with st.spinner("🚀 Analyzing global trends and curating your buzz..."):
        try:
            # Direct function call (No subprocess - much faster!)
            briefing = generate_newsletter()
            
            # SAVE IN SESSION (taaki audio ke liye bhi accessible ho)
            st.session_state.full_briefing = briefing
            st.success("✨ Your Personalized Daily Briefing is Ready!")
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

# IF news is already generated, show it and offer audio option
if "full_briefing" in st.session_state:
    st.markdown(st.session_state.full_briefing)
    
    st.divider() # BEAUTIFYING DIVIDER
    
    # 🎙️ Podcast Section
    st.subheader("🎧 Audio Briefing")
    if st.button("🎙️ Listen to Daily Buzz"):
        with st.spinner("Preparing your audio podcast..."):
            try:
                # GENRATE AUDIO
                audio_data = generate_audio(st.session_state.full_briefing)
                # SHOW AUDIO PLAYER
                st.audio(audio_data, format="audio/mp3")
                st.success("▶️ Click play to listen!")
            except Exception as audio_err:
                st.error(f"Audio error: {audio_err}")