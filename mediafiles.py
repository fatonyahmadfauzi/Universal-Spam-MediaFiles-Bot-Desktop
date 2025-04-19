import os
import time
import pyautogui
import subprocess
import tempfile
from datetime import datetime

def copy_file_to_clipboard(file_path):
    """Salin file ke clipboard dengan format yang benar (Windows)"""
    try:
        abs_path = os.path.abspath(file_path).replace('/', '\\')
        ps_script = f"""
        Add-Type -AssemblyName System.Windows.Forms
        $file = New-Object System.Collections.Specialized.StringCollection
        $file.Add('{abs_path}')
        [System.Windows.Forms.Clipboard]::SetFileDropList($file)
        """
        
        with tempfile.NamedTemporaryFile(suffix='.ps1', delete=False) as f:
            f.write(ps_script.encode('utf-8'))
            temp_path = f.name
        
        subprocess.run([
            'powershell.exe',
            '-ExecutionPolicy', 'Bypass',
            '-File', temp_path
        ], check=True, shell=True)
        
        os.unlink(temp_path)
        return True
    except Exception as e:
        print(f"❌ Gagal menyalin file: {e}")
        return False

def send_file(file_path, count=None, total=None, bot_prompt='N', upload_delay=3):
    """Fungsi universal untuk mengirim file dengan opsi bot prompt"""
    try:
        # Tambahkan status bot jika diaktifkan
        if bot_prompt == 'Y' and count is not None and total is not None:
            timestamp = datetime.now().strftime("%H:%M:%S")
            status_msg = f"[{timestamp} | {count}/{total}] "
            pyautogui.write(status_msg, interval=0.05)
            time.sleep(0.5)
        
        # Salin dan tempel file
        if not copy_file_to_clipboard(file_path):
            return False
            
        pyautogui.hotkey('ctrl', 'v')
        
        # Progress bar upload
        print("🔼 Uploading", end='', flush=True)
        for _ in range(int(upload_delay)):
            print('.', end='', flush=True)
            time.sleep(1)
        print()
        
        pyautogui.press('enter')
        return True
    except Exception as e:
        print(f"\n❌ Gagal mengirim: {e}")
        return False

def main():
    print("=== UNIVERSAL FILE SENDER WITH BOT PROMPT ===")
    
    # Konfigurasi
    file_path = input("Drag file ke sini atau ketik path: ").strip('"\'')
    if not os.path.exists(file_path):
        print("❌ File tidak ditemukan!")
        return

    repeat_count = int(input("Jumlah pengulangan: "))
    delay_between = float(input("Delay antar pengiriman (detik): "))
    upload_delay = float(input("Waktu upload file (detik): "))
    bot_prompt = input('Tambahkan bot prompt? (Y/N): ').strip().upper()

    print("\n⚠️ INSTRUKSI:")
    print("1. Buka aplikasi messaging (WhatsApp/Telegram/dll)")
    print("2. Klik kolom input teks")
    print("3. Jangan gunakan mouse/keyboard selama proses")
    print(f"\n🔄 Akan mengirim {repeat_count} kali dalam 5 detik...")
    time.sleep(5)

    # Proses pengiriman
    success_count = 0
    try:
        for i in range(1, repeat_count + 1):
            print(f"\n♻️ Pengiriman {i}/{repeat_count}")
            if send_file(
                file_path=file_path,
                count=i,
                total=repeat_count,
                bot_prompt=bot_prompt,
                upload_delay=upload_delay
            ):
                success_count += 1
                print(f"✅ Berhasil (Total: {success_count})")
            else:
                print("❌ Gagal")
            
            if i < repeat_count:
                print(f"⏳ Menunggu {delay_between} detik...")
                time.sleep(delay_between)

        # Pesan penutup
        if bot_prompt == 'Y':
            pyautogui.write("✅ Semua file terkirim", interval=0.05)
            pyautogui.press('enter')
            
    except KeyboardInterrupt:
        print("\n⏹️ Dihentikan oleh pengguna")

    print(f"\n📊 Hasil: {success_count}/{repeat_count} berhasil dikirim")
    input("\n🚪 Tekan Enter untuk keluar...")

if __name__ == "__main__":
    main()