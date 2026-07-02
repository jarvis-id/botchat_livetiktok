import os
import sys
import subprocess
import threading
import queue
import time

def install_dependencies():
    try:
        import TikTokLive
        if sys.platform == 'win32':
            import pyttsx3
    except ImportError:
        print("Mendeteksi library yang kurang. Sedang menginstal dependensi...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("Dependensi berhasil diinstal. Memulai ulang aplikasi...")
        os.execv(sys.executable, ['python'] + sys.argv)

if __name__ == "__main__":
    install_dependencies()

from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent, GiftEvent, DisconnectEvent, FollowEvent, LikeEvent

# --- TTS WORKER ---
tts_queue = queue.Queue()
is_windows = sys.platform == 'win32'

if is_windows:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.0)

def tts_worker():
    while True:
        text = tts_queue.get()
        if text is None:
            break
        try:
            if is_windows:
                engine.say(text)
                engine.runAndWait()
            else:
                # Use Termux TTS for Android
                import shlex
                safe_text = shlex.quote(text)
                os.system(f"termux-tts-speak {safe_text}")
        except Exception as e:
            print(f"\n[TTS Error] Gagal memainkan suara: {e}")
        tts_queue.task_done()

tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()

def speak(text: str):
    tts_queue.put(text)

# --- TIKTOK LOGIC ---
last_like_tts_time = 0

def run_tiktok_client():
    global last_like_tts_time
    print("="*50)
    print("      TikTok Live Interaction Engine (CLI)     ")
    print("="*50)
    
    username = input("Masukkan Username TikTok target: ").strip()
    if not username:
        print("Username tidak boleh kosong!")
        return

    print(f"\nMenyiapkan koneksi ke @{username}...")
    client = TikTokLiveClient(unique_id=username)

    @client.on(ConnectEvent)
    async def on_connect(event: ConnectEvent):
        msg = f"Berhasil terhubung ke Room ID: {client.room_id}"
        print(f"\n[STATUS] {msg}")
        speak(f"Berhasil terhubung ke live {username}")

    @client.on(DisconnectEvent)
    async def on_disconnect(event: DisconnectEvent):
        print("\n[STATUS] Terputus dari live stream.")
        speak("Terputus dari live stream.")

    @client.on(CommentEvent)
    async def on_comment(event: CommentEvent):
        user = event.user.nickname
        comment = event.comment
        print(f"[COMMENT] {user} -> {comment}")
        speak(f"{user} bilang, {comment}")

    @client.on(GiftEvent)
    async def on_gift(event: GiftEvent):
        # Ignore streakable gifts that are still streaking
        if event.gift.streakable and not event.gift.streaking:
            pass 
        elif event.gift.streakable and event.gift.streaking:
            return 
            
        user = event.user.nickname
        gift_name = event.gift.info.name
        count = getattr(event.gift, "count", 1)
        
        print(f"[GIFT] {user} mengirim {count}x {gift_name}")
        speak(f"Terima kasih {user} atas {count} {gift_name}")

    @client.on(FollowEvent)
    async def on_follow(event: FollowEvent):
        user = event.user.nickname
        print(f"[FOLLOW] {user} mulai mengikuti")
        speak(f"{user} mulai mengikuti")

    @client.on(LikeEvent)
    async def on_like(event: LikeEvent):
        global last_like_tts_time
        user = event.user.nickname
        count = getattr(event, "count", 1)
        
        print(f"[LIKE] {user} tap-tap layar ({count}x)")
        
        # Rate limit Like TTS (max 1 per 10 seconds)
        now = time.time()
        if now - last_like_tts_time > 10:
            speak(f"{user} menyukai live ini")
            last_like_tts_time = now

    try:
        client.run()
    except Exception as e:
        print(f"\n[ERROR] Koneksi gagal: {e}")

if __name__ == "__main__":
    try:
        run_tiktok_client()
    except KeyboardInterrupt:
        print("\nMenghentikan program...")
