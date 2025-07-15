@echo off
title 🤖 Fake News Detector Chatbot - FastAPI Launcher

REM Optional: Activate virtual environment (uncomment if needed)
REM call venv\Scripts\activate

REM Step 1: Start FastAPI backend
start cmd /k "uvicorn main:app --reload"

REM Step 2: Wait for server
timeout /t 2 >nul

REM Step 3: Open the chatbot in browser
start "" "http://127.0.0.1:8000"

@echo FastAPI running. Press any key to close this window.
pause
