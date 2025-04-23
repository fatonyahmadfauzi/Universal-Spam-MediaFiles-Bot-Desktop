# WhatsApp Multi-File Sender Bot 🚀

![Demo](demo.gif)

A Python automation tool to send multiple files via WhatsApp Web with customizable intervals and status tracking.

## 🔥 Features

- **Multi-File Support**: Send multiple files in one batch (type "selesai" when done)
- **Smart Tracking**: Individual progress for each file
- **Flexible Configuration**:
  - Set repeat counts and delays
  - Adjust upload timing per file size
- **Status Updates**: Optional timestamps and counters
- **Cross-Platform**: Works on Windows (Mac/Linux support coming)

## 🛠 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/whatsapp-file-sender.git
cd whatsapp-file-sender

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

```bash
python whatsapp_file_sender.py
```

**Follow the prompts:**

1. Scan QR code when prompted
2. Enter recipient name (exact match)
3. Add files one by one (type "selesai" to finish)
4. Configure sending parameters:

- Repeat count
- Delay between sends
- Upload wait time
- Bot prompts (Y/N)

## 📊 Example Workflow

```text
Nama kontak/grup: Team Project

Masukkan path file (ketik 'selesai' jika sudah):
File 1: C:\docs\presentasi.pdf
File 2: D:\images\chart.png
File 3: selesai

Jumlah pengulangan: 3
Delay antar pengiriman (detik): 5
Waktu upload file (detik): 3
Tambahkan bot prompt? (Y/N): Y
```

## ⚙️ Configuration Options

| **Parameter** | **Description**         | **Default** | **Recommended** |
| ------------- | ----------------------- | ----------- | --------------- |
| File Paths    | Multiple files to send  | -           | Any file type   |
| Repeat Count  | Times to repeat sending | 1           | 1-10            |
| Send Delay    | Seconds between batches | 1           | 1-5             |
| Upload Delay  | Seconds per file upload | 3           | 2-10            |
| Bot Prompt    | Add status messages     | N           | Y/N             |

## 📜 License

MIT License - See [LICENSE.md]()

## ❗ Important Notes

- Use responsibly and comply with WhatsApp's ToS
- Recommended max 5 messages/minute
- Not affiliated with WhatsApp/Meta
