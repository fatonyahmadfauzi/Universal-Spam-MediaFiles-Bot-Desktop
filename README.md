# 🌐 Universal File Sender Bot

![Demo](demo.gif)

A cross-platform automation tool to send files to any web-based messaging service (WhatsApp, Telegram, Messenger, etc.)

## 🔥 Core Features

- **Multi-Service Support**: Works with WhatsApp Web, Telegram Web, Facebook Messenger, and most browser-based chat platforms
- **Batch File Sending**: Send multiple files in one operation (type "done" when finished)
- **Smart Tracking**:
  - Individual file progress indicators
  - Success/failure reporting per file
- **Flexible Configuration**:
  - Custom repeat intervals (1-100x)
  - Adjustable delays between sends (0.5-30s)
  - File-size aware upload timing

## 🛠 Installation

```bash
# Clone the repository
git clone -b multi-file --single-branch https://github.com/fatonyahmadfauzi/Universal-Spam-MediaFiles-Bot-Desktop.git Universal-Spam-MediaFiles-Bot-Desktop_Multi-File
cd Universal-Spam-MediaFiles-Bot-Desktop_Multi-File

# Install core dependencies
pip install -r requirements.txt
```

## 🚀 Basic Usage

```bash
python mediafiles.py
```

**Interactive Guide:**

1. Open your web messaging platform in Chrome
2. Navigate to the desired chat
3. Run the script and follow prompts:

- Add files one by one (type "done" to finish)
- Set sending parameters
- Activate status messages (optional)

4. Click the message input box when instructed

## ⚙️ Configuration Options

| **Parameter** | **Description**         | **Default** | **Recommended** |
| ------------- | ----------------------- | ----------- | --------------- |
| File Paths    | Multiple files to send  | -           | Any file type   |
| Repeat Count  | Times to repeat sending | 1           | 1-10            |
| Send Delay    | Seconds between batches | 1           | 1-5             |
| Upload Delay  | Seconds per file upload | 3           | 2-10            |
| Bot Prompt    | Add status messages     | N           | Y/N             |
