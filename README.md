# TikTok Live Interaction Engine (CLI Edition)

Aplikasi ringan berbasis Python murni (*Command-Line Interface*) yang berfungsi untuk mendengarkan TikTok LIVE dan secara otomatis membacakan interaksi penonton menggunakan suara AI (Text-to-Speech).

Aplikasi ini mendeteksi dan menyuarakan:
- **Komentar**: "[Nama] bilang, [Pesan]"
- **Gift**: "Terima kasih [Nama] atas [Jumlah] [Gift]"
- **Follow**: "[Nama] mulai mengikuti"
- **Like (Tap-tap)**: "[Nama] menyukai live ini" (dibatasi 1x per 10 detik agar tidak *spam*).

## Cara Penggunaan (Windows)
1. Instal [Python](https://www.python.org/) terbaru. Pastikan Anda mencentang opsi **"Add Python to PATH"** saat proses instalasi.
2. Clone repositori ini melalui terminal/Command Prompt:
   ```bash
   git clone https://github.com/jarvis-id/botchat_livetiktok.git
   cd botchat_livetiktok
   ```
3. Jalankan file `run.bat` (klik dua kali) atau jalankan `python main.py` di terminal. 
4. Aplikasi akan otomatis menginstal dependensi saat dijalankan pertama kali.
5. Saat diminta, **masukkan username TikTok** target (tanpa @) dan tekan Enter.
6. Aplikasi akan mulai mendengarkan event dari TikTok Live dan menyuarakannya!

## Cara Penggunaan di Termux (Android)
Aplikasi ini telah dioptimalkan secara khusus untuk berjalan di perangkat Android menggunakan Termux, dengan dukungan penuh TTS Google Assistant yang natural.

### Syarat Wajib Termux:
Karena Termux berjalan di Android, Anda wajib menginstal aplikasi perantara (Termux:API) agar script Python bisa mengeluarkan suara lewat *speaker* HP Anda.
1. Instal aplikasi **Termux** dan **Termux:API** dari *F-Droid* (jangan dari Play Store).
2. Buka aplikasi Termux, lalu jalankan perintah ini untuk menginstal paket sistem yang dibutuhkan:
   ```bash
   pkg update && pkg upgrade
   pkg install python git termux-api
   ```

### Langkah Menjalankan:
1. Clone repositori ini ke dalam penyimpanan Termux Anda:
   ```bash
   git clone https://github.com/jarvis-id/botchat_livetiktok.git
   ```
2. Masuk ke direktori skrip:
   ```bash
   cd botchat_livetiktok
   ```
3. Jalankan aplikasi:
   ```bash
   python main.py
   ```
4. Masukkan username TikTok target saat diminta, dan biarkan aplikasi berjalan di latar belakang!

---
*Catatan Keamanan: Aplikasi ini berjalan sepenuhnya secara lokal dan tidak memerlukan login ke akun TikTok Anda.*
