# Release Notes

## v1.2.0 - Multi-File Enhancement (2023-11-20)

### Added

- Multiple file input (type "selesai" to finish)
- Individual file progress tracking
- Dynamic status messages per file
- File validation before sending

### Changed

- Improved user interface with step-by-step prompts
- Increased default delays for stability
- Better error handling for file operations

### Fixed

- Clipboard clearing between files
- Status message formatting
- QR code detection reliability

Key Features:

1. **Platform-Specific Packages**:

- Windows-only dependencies marked with `sys_platform`
- Clean separation for future cross-platform support

2. **Version Pinning**:

- Tested stable versions
- Prevents breaking changes

3. **Functional Grouping**:

- Core automation tools
- Windows utilities
- Optional enhancements
- Dev tools (can be moved to requirements-dev.txt)

3. WhatsApp Web Optimized:

- Selenium 4.9.0 for modern WhatsApp Web
- Webdriver-manager for automatic ChromeDriver

4. File Handling:

- PyAutoGUI for reliable file pasting
- Pyperclip as clipboard fallback

Installation commands:

```bash
# For production use:
pip install -r requirements.txt

# For development:
pip install -r requirements-dev.txt
```

This setup ensures:

- Stable core functionality
- Clean Windows-specific dependencies
- Room for future expansion
- Separate dev/prod environments
