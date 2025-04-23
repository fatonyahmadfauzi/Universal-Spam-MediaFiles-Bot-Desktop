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

def send_files(file_paths, count=None, total=None, bot_prompt='N', upload_delay=3):
    """Fungsi universal untuk mengirim multiple file dengan opsi bot prompt"""
    success_count = 0
    try:
        for i, file_path in enumerate(file_paths, 1):
            # Tambahkan status bot jika diaktifkan
            if bot_prompt == 'Y' and count is not None and total is not None:
                timestamp = datetime.now().strftime("%H:%M:%S")
                status_msg = f"[{timestamp} | File {i}/{len(file_paths)}] "
                pyautogui.write(status_msg, interval=0.05)
                time.sleep(0.5)
            
            # Salin dan tempel file
            if not copy_file_to_clipboard(file_path):
                print(f"❌ Gagal mengirim {os.path.basename(file_path)}")
                continue
                
            pyautogui.hotkey('ctrl', 'v')
            
            # Progress bar upload
            print(f"🔼 Uploading {os.path.basename(file_path)}", end='', flush=True)
            for _ in range(int(upload_delay)):
                print('.', end='', flush=True)
                time.sleep(1)
            print()
            
            pyautogui.press('enter')
            success_count += 1
            
            # Jangan tunggu setelah file terakhir
            if i < len(file_paths):
                time.sleep(1)  # Delay antar file
        
        return success_count
    except Exception as e:
        print(f"\n❌ Gagal mengirim: {e}")
        return success_count

def main():
    print("=== UNIVERSAL MULTI-FILE SENDER WITH BOT PROMPT ===")
    
    # Input multiple files
    file_paths = []
    print("\nMasukkan path file (ketik 'selesai' jika sudah):")
    while True:
        file_path = input(f"File {len(file_paths)+1}: ").strip('"\'')
        if file_path.lower() == 'selesai':
            if not file_paths:
                print("⚠️ Minimal 1 file diperlukan!")
                continue
            break
        if not os.path.exists(file_path):
            print(f"❌ File tidak ditemukan: {file_path}")
            continue
        file_paths.append(file_path)

    # Konfigurasi
    repeat_count = int(input("Jumlah pengulangan: "))
    delay_between = float(input("Delay antar pengiriman (detik): "))
    upload_delay = float(input("Waktu upload file (detik): "))
    bot_prompt = input('Tambahkan bot prompt? (Y/N): ').strip().upper()

    print("\n⚠️ INSTRUKSI:")
    print("1. Buka aplikasi messaging (WhatsApp/Telegram/dll)")
    print("2. Klik kolom input teks")
    print("3. Jangan gunakan mouse/keyboard selama proses")
    print(f"\n🔄 Akan mengirim {len(file_paths)} file sebanyak {repeat_count} kali dalam 5 detik...")
    time.sleep(5)

    # Proses pengiriman
    total_success = 0
    try:
        for cycle in range(1, repeat_count + 1):
            print(f"\n♻️ Siklus {cycle}/{repeat_count}")
            
            success = send_files(
                file_paths=file_paths,
                count=cycle,
                total=repeat_count,
                bot_prompt=bot_prompt,
                upload_delay=upload_delay
            )
            total_success += success
            
            if cycle < repeat_count:
                print(f"⏳ Menunggu {delay_between} detik...")
                time.sleep(delay_between)

        # Pesan penutup
        if bot_prompt == 'Y':
            pyautogui.write(f"✅ {total_success}/{len(file_paths)*repeat_count} file terkirim", interval=0.05)
            pyautogui.press('enter')
            
    except KeyboardInterrupt:
        print("\n⏹️ Dihentikan oleh pengguna")

    print(f"\n📊 Hasil: {total_success}/{len(file_paths)*repeat_count} file berhasil dikirim")
    input("\n🚪 Tekan Enter untuk keluar...")

if __name__ == "__main__":
    main()