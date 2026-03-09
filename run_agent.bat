@echo off
cd "C:\Users\tabis\OneDrive\Desktop\DATA SCIENCE PROJECT"
call agent_env\Scripts\activate
python run_pipeline.py
python generate_briefing.py > latest_briefing.txt