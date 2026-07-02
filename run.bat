@echo off
echo ==============================================
echo TikTok Live Interaction Engine
echo ==============================================

:: Cek apakah Python sudah terinstal
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python tidak ditemukan! Harap instal Python dari https://www.python.org/
    echo Pastikan Anda mencentang "Add Python to PATH" saat proses instalasi.
    pause
    exit /b
)

:: Cek apakah file .env ada, jika tidak, salin dari .env.example
if not exist ".env" (
    echo Memasukkan konfigurasi default...
    copy .env.example .env >nul
    echo Tolong edit file .env dan isi TIKTOK_USERNAME Anda terlebih dahulu.
    pause
    exit /b
)

echo Memulai aplikasi...
python main.py
pause
