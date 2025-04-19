# 📤 Universal File Sender with Bot Prompt

![Demo Animation](https://via.placeholder.com/800x400?text=Demo+Animation+Here)
_(Replace with actual demo GIF)_

A cross-platform automation tool that sends files to messaging apps with smart features.

## 🌟 Features

- **Universal Compatibility**  
  Works with WhatsApp Web, Telegram Web, Facebook Messenger, and most browser-based messaging platforms
- **Smart Bot Prompts**  
  Optional timestamps and counters (`[HH:MM:SS | X/Y]`)
- **Auto-Upload Detection**  
  Calculates required upload time based on file size
- **User-Friendly**  
  Drag & drop support and visual progress indicators

## 🛠 Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/universal-file-sender.git
cd universal-file-sender

# Install dependencies
pip install pyautogui
```

## 🚀 Usage

```bash
python universal_file_sender.py
```

**Follow the on-screen prompts:**

1. Drag & drop your file or enter path manually
2. Set number of repeats
3. Configure delays (between sends and upload time)
4. Enable/disable bot prompts (Y/N)
5. Focus on your messaging app's input box

## ⚙️ Configuration Options

| **Parameter** | **Description**           | **Default** | **Recommended** |
| ------------- | ------------------------- | ----------- | --------------- |
| File Path     | File to send              | -           | Any file type   |
| Repeat Count  | Number of times to send   | 1           | 1-20            |
| Send Delay    | Seconds between sends     | 1           | 0.5-5           |
| Upload Delay  | Seconds for file upload   | 3           | 3-15\*          |
| Bot Prompt    | Add status messages (Y/N) | N           | Y/N             |

\*_Automatically calculated based on file size_

## 📋 Requirements

- Python 3.6+
- Windows OS (Mac/Linux requires modifications)
- Browser-based messaging app (WhatsApp Web, Telegram Web, etc.)

## 🚨 Limitations

1. **Platform Support**:
   - Currently optimized for Windows
   - Requires manual adjustment for Mac/Linux
2. **File Size**:
   - Maximum tested: 25MB
   - Larger files may require increased upload delay
3. **Security**:
   - Some platforms may flag rapid automated sends
   - Recommended max: 5 messages/minute

## 🛠️ Troubleshooting

**Common Issues**:

- `File not found` → Use absolute paths
- `Send failed` → Increase upload delay
- `Clipboard errors` → Run as Administrator

**For Developers**:

```python
# To adapt for Mac/Linux:
# Replace PowerShell commands with:
subprocess.run(['pbcopy' if sys.platform == 'darwin' else 'xclip', file_path])
```

## 📜 License

MIT License - Free for personal and commercial use

## 📬 Contact

For support/questions:
[Your Email] · [Project Issues] · [Twitter Handle]
