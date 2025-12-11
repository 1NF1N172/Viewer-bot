# Release Notes - 1NF Twitch Viewer Bot

## Version 1.0.0 - Initial Release

### 🎉 Welcome to 1NF Twitch Viewer Bot!

A powerful, automated tool that helps you send viewers to your Twitch live stream using proxy servers. This tool automates the process of connecting to Twitch through various proxy services, making it easy to boost your viewer count without purchasing expensive proxy services.

---

## ✨ Features

### Core Functionality
- **🔄 Automated Proxy Integration**: Automatically connects through multiple proxy servers (Blockaway, CroxyProxy, and more)
- **🤖 Selenium Automation**: Uses Selenium WebDriver to automate browser interactions
- **🛡️ Built-in Ad Blocking**: Automatically downloads and installs uBlock Origin extension
- **📊 Multiple Session Support**: Run multiple viewer sessions without restarting
- **🎯 Quality Optimization**: Automatically reduces stream quality to 160p to minimize bandwidth usage
- **💻 Cross-Platform**: Works on Windows with Python 3.x

### User Experience
- **🎨 Beautiful ASCII Banner**: Custom 1NF branding with colorful terminal output
- **📝 Interactive CLI**: Easy-to-use command-line interface
- **⚡ Batch Processing**: Send multiple viewers in a single session
- **🔄 Session Management**: Add more sessions or exit cleanly

---

## 📋 Requirements

### System Requirements
- **OS**: Windows 10/11
- **RAM**: Minimum 4GB (8GB+ recommended for multiple viewers)
- **Internet**: Stable internet connection

### Software Dependencies
- **Python**: 3.11 or higher
- **Google Chrome**: Latest version
- **ChromeDriver**: Must match your Chrome version
- **Python Packages**:
  - `selenium`
  - `colorama`
  - `pystyle`
  - `requests`

---

## 🚀 Installation

### Step 1: Install Python
1. Download Python 3.11+ from [python.org](https://www.python.org/downloads/)
2. **Important**: Check "Add Python to PATH" during installation
3. Verify installation: `python --version`

### Step 2: Install ChromeDriver
1. Check your Chrome version: `chrome://version/`
2. Download matching ChromeDriver from [chromedriver.chromium.org](https://chromedriver.chromium.org/downloads)
3. Place `chromedriver.exe` in the project folder

### Step 3: Install Dependencies
```bash
# Option 1: Using pip
pip install -r requirements.txt

# Option 2: Using install.bat (Windows)
install.bat
```

### Step 4: Run the Bot
```bash
# Option 1: Double-click run.bat
# Option 2: Run Python script
python main.py
```

---

## 📖 Usage Guide

### Basic Usage

1. **Launch the Application**
   - Run `run.bat` or execute `python main.py`
   - You'll see the 1NF ASCII banner

2. **Select Proxy Server**
   - Choose from available proxy servers (1-7)
   - **Recommended**: Proxy Server 1 (Blockaway)

3. **Enter Channel Information**
   - Enter your Twitch channel name (e.g., `yourchannel`)
   - Specify number of viewers to send

4. **Monitor Progress**
   - Watch as tabs open and connect
   - Check success/failure statistics

5. **Add More Sessions** (Optional)
   - Choose to add more sessions or exit

### Advanced Usage

**Multiple Sessions**
- Run multiple sessions to send more viewers
- Each session can handle different proxy servers
- Sessions run independently

**Recommended Settings**
- For 20 viewers, request 30 (accounts for failures)
- Use on a separate computer from your streaming setup
- Ensure adequate RAM (8GB+ for 50+ viewers)

---

## 🔧 Technical Details

### Architecture
- **Language**: Python 3.x
- **Automation**: Selenium WebDriver
- **Browser**: Google Chrome (headless automation)
- **Ad Blocking**: uBlock Origin extension

### Supported Proxy Services
1. Blockaway.net
2. CroxyProxy.com
3. CroxyProxy.rocks
4. Croxy.network
5. Croxy.org
6. YouTubeUnblocked.live
7. CroxyProxy.net

### How It Works
1. Opens Chrome browser with uBlock Origin
2. Navigates to selected proxy service
3. Enters Twitch channel URL through proxy
4. Automatically handles consent popups
5. Reduces stream quality to minimize resources
6. Keeps connections active

---

## ⚠️ Important Notes

### System Recommendations
- **RAM**: Use a computer with plenty of RAM (8GB+ recommended)
- **Separate Machine**: Best used on a different computer than your streaming setup
- **Virtual Server**: Can run on a powerful VPS for best results

### Limitations
- Proxy services may occasionally be slow or unavailable
- Some viewers may disconnect due to proxy issues
- Requires stable internet connection
- ChromeDriver must match Chrome version

### Troubleshooting
- **Slow Performance**: Try a different proxy server
- **Connection Failures**: Close and restart the application
- **ChromeDriver Errors**: Update ChromeDriver to match Chrome version
- **Import Errors**: Run `pip install -r requirements.txt`

---

## 🛡️ Legal Disclaimer

This software is designed **solely for educational and security research purposes**. 

- The author is not responsible for any misuse or illegal activity
- Use at your own risk and responsibility
- Ensure compliance with Twitch Terms of Service
- This tool does not collect, store, or process personal data

---

## 📝 Changelog

### Version 1.0.0 (2025-12-11)
- ✨ Initial release
- 🎨 Custom 1NF branding and ASCII art
- 🤖 Automated proxy integration
- 🛡️ Built-in ad blocking with uBlock Origin
- 📊 Multiple session support
- 🎯 Stream quality optimization
- 💻 Windows compatibility
- 📝 Comprehensive error handling
- 🔄 Session management features

---

## 🙏 Credits

- **Developer**: 1NF
- **Original Concept**: Based on Twitch Viewer Bot automation
- **Technologies**: Selenium, Python, ChromeDriver

---

## 📞 Support

For issues, questions, or contributions:
- **GitHub Repository**: [1NF1N172/twitch-viewer-bot](https://github.com/1NF1N172/twitch-viewer-bot)
- **Report Issues**: Use GitHub Issues
- **Contributions**: Pull requests welcome!

---

## ⭐ Star This Project

If you find this project useful, please consider giving it a star on GitHub! Your support helps improve the project.

---

**Thank you for using 1NF Twitch Viewer Bot!** 🚀

