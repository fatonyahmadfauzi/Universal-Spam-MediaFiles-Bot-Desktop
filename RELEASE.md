# 📦 Release Notes - Universal File Sender Bot

**🌟 v1.0.0 - Initial Release**
_Released: 20/04/2025_

---

## 🚀 New Features

- **Universal File Sending**
  Send files to any messaging platform (WhatsApp/Telegram/Messenger) via clipboard automation
- **Smart Bot Prompts**
  Optional `[HH:MM:SS | X/Y]` status headers with `bot_prompt` toggle
- **Auto-Upload Timing**
  Dynamic delay calculation: `3s base + 0.5s per MB` (max 15s)

---

## 🛠 Technical Improvements

- PowerShell-based file copying for Windows
- Cross-platform CLI interface
- Visual progress indicators during upload

---

## ⚠️ Known Issues

- Limited to Windows (Mac/Linux support planned)
- Large files (>25MB) may require manual delay adjustment

**Installation Guide:**

1. **Base Installation**:

```bash
# First-time setup
pip install -r requirements.txt
```

2. **Platform-Specific Add-ons**:

```bash
# Windows (full feature set)
pip install pywin32 pypiwin32

# Mac (basic functionality)
pip install pyobjc-framework-Cocoa

# Linux (x11 required)
sudo apt-get install xclip
pip install xclip
```

**Key Version Choices**:

1. **PyAutoGUI 0.9.54** - Stable version with reliable Ctrl+V/Enter simulation
2. **PyWin32 306** - Latest compatible version for Windows clipboard operations
3. **Psutil 5.9.5** - Lightweight system monitoring for large file handling

**Key Features**:

1. **Robust Testing Suite**:

```text
pytest==7.4.0            # Core testing framework
pytest-cov==4.1.0        # Code coverage analysis
pytest-mock==3.11.1      # For mocking platform-specific operations
```

2. **Automated Code Quality**:

```text
black==23.7.0            # Uncompromising code formatter
flake8==6.0.0            # Style guide enforcement
mypy==1.5.1              # Type safety checks
```

3. **Git Integration**:

```text
pre-commit==3.3.3        # Auto-run checks before commit
commitizen==2.42.1       # Conventional commits standard
```

4. **Cross-Platform Debugging**:

```text
ipdb==0.13.13            # Works on all platforms
memory-profiler==0.61.0  # Monitor memory leaks
```

**Installation**:

```bash
# Install dev dependencies (after core requirements.txt)
pip install -r requirements-dev.txt

# Setup pre-commit hooks
pre-commit install
```

This setup ensures:

- **Windows/Mac/Linux parity** in development tools
- **Strict version control** to prevent toolchain conflicts
- **CI/CD readiness** with coverage and type checking
- **Automated code hygiene** through git hooks
