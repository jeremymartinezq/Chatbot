@echo off
echo Starting CopyCoder Chatbot...

cd backend
start "Backend Server" cmd /k "C:\Users\Jeremy\AppData\Local\Programs\Python\Python313\python.exe -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000"

timeout /t 2
cd ..
start "" "frontend\chatbot.html"

echo Chatbot is running!
echo Backend server: http://localhost:8000
echo Frontend should open in your browser automatically.
echo.
echo Press Ctrl+C in the backend server window to stop the server when done. 