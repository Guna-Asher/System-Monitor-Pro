# System Monitor Pro 🖥️

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://python.org)
[![Platform](https://img.shields.io/badge/platform-Linux%20%7C%20macOS%20%7C%20WSL-green.svg)](https://ubuntu.com)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)


## 🎯 **Project Overview**

**System Monitor Pro** is a command-line utility that provides real-time monitoring of system resources including CPU, memory, disk usage, and running processes. Built with simplicity and professionalism in mind, it showcases the exact skills required for DataOps roles: **Python scripting, Linux system interaction, automation, and software development best practices**.

### **Why This Project Stands Out**
- **Directly aligns** with DataOps internship requirements (Python + Linux + Git)
- **Clean, professional code** that's interview-ready
- **Production-quality** with error handling, logging, and configuration
- **Simple but powerful** - demonstrates fundamentals without complexity
- **Extensible architecture** - easy to build upon for real-world scenarios

## ✨ **Key Features**

### **📊 Comprehensive Monitoring**
- **Real-time CPU usage** tracking with percentage and alert thresholds
- **Memory utilization** monitoring in both percentage and gigabytes
- **Disk space analysis** with free space calculation and warnings
- **Process count tracking** to monitor system load

### **🔔 Intelligent Alerting System**
- Configurable thresholds (CPU: 80%, Memory: 85%, Disk: 90%)
- Visual indicators (🟢/🔴) for quick status assessment
- Detailed alert messages with specific metrics
- Non-intrusive warning system

### **📈 Data Management**
- **CSV logging** with automatic file creation and management
- **Timestamped entries** for historical analysis
- **Log rotation** considerations built-in
- **Data summary** feature for quick insights

### **💻 User Experience**
- **Interactive menu system** for easy navigation
- **Command-line interface** for automation and scripting
- **Color-coded output** for better readability
- **Multiple run modes** (once, continuous, scheduled)
- **Comprehensive help system**

### **⚙️ Professional Engineering**
- **Object-oriented design** with clear separation of concerns
- **Comprehensive error handling** and graceful degradation
- **Modular architecture** for easy maintenance and extension
- **Dependency management** with automatic installation
- **Cross-platform compatibility** (Linux, macOS, WSL)

## 🛠️ **Technology Stack**

### **Core Technologies**
- **Python 3.6+** - Primary programming language
- **psutil** - Cross-platform system monitoring library
- **Bash/Shell** - Automation and deployment scripting
- **Git** - Version control and collaboration

### **Key Python Concepts Demonstrated**
```python
# Object-Oriented Programming
class SystemMonitor:
    def __init__(self):
        self.log_file = "logs/system_monitor.csv"
    
    def collect_metrics(self):
        # Method demonstrates error handling and data processing
        pass

# File I/O and Data Management
with open(self.log_file, 'a') as f:
    f.write(f"{data['timestamp']},{data['cpu']},...")

# System Interaction
cpu_percent = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

# Command-Line Interface
import argparse
parser = argparse.ArgumentParser(description='System Monitor Pro')
```

## 🚀 **Quick Start**

### **Prerequisites**
- Python 3.6 or higher
- pip (Python package manager)
- Git (for version control)

### **Installation (3 Methods)**

#### **Method 1: One-Command Setup (Recommended)**
```bash
# Clone and setup in one command
git clone https://github.com/YOUR_USERNAME/system-monitor-pro.git && \
cd system-monitor-pro && \
chmod +x setup.sh && \
./setup.sh
```

#### **Method 2: Step-by-Step Manual Setup**
```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/system-monitor-pro.git
cd system-monitor-pro

# 2. Make setup script executable
chmod +x setup.sh

# 3. Run the setup script
./setup.sh

# 4. Verify installation
python monitor.py --help
```

#### **Method 3: Minimal Setup (For Testing)**
```bash
# Just install dependencies and run
pip install psutil
python monitor.py once
```

### **Verification**
After installation, you should see:
```
╔══════════════════════════════════════════╗
║     System Monitor Pro - Setup          ║
╚══════════════════════════════════════════╝

[1/4] Checking Python...
  ✓ Python 3.9.0 found

[2/4] Installing dependencies...
  ✓ psutil 5.9.0 installed successfully

[3/4] Setting up permissions...
  ✓ Setup script is now executable

[4/4] Creating directory structure...
  ✓ Created logs/ directory

══════════════════════════════════════════
✅ Setup completed successfully!
══════════════════════════════════════════
```

## 📖 **Usage Guide**

### **Interactive Mode (Default)**
Run without arguments to launch the interactive menu:
```bash
python monitor.py
```

You'll see:
```
══════════════════════════════════════════
   SYSTEM MONITOR PRO - Main Menu
══════════════════════════════════════════

1. Run once
2. Run continuously
3. Show data summary
4. Check system requirements
5. Exit

Select option (1-5):
```

### **Command-Line Interface**

#### **Single Execution**
```bash
# Run once and display results
python monitor.py once
```

#### **Continuous Monitoring**
```bash
# Monitor continuously with 5-second intervals (default)
python monitor.py start

# Custom interval (10 seconds)
python monitor.py start 10

# Monitor for specific duration (300 seconds = 5 minutes)
python monitor.py start 5 300
```

#### **Data Analysis**
```bash
# View logged data summary
python monitor.py summary

# View last 10 log entries
python monitor.py summary --lines 10
```

#### **Help and Information**
```bash
# Display help message
python monitor.py help

# Check system requirements
python monitor.py check

# Show version information
python monitor.py version
```

### **Sample Output**
When running the monitor, you'll see:
```
══════════════════════════════════════════════════
🖥️  SYSTEM MONITOR PRO - 2024-03-15 10:30:00
══════════════════════════════════════════════════
🟢 CPU:          24.5%
🟢 Memory:       67.3% (8.2 GB)
🟢 Disk:         45.2% (128.5 GB free)
📊 Processes:    342
──────────────────────────────────────────────────

📝 Log file: logs/system_monitor.csv (12.5 KB)
```

### **Alert Example**
If system resources are high:
```
══════════════════════════════════════════════════
🖥️  SYSTEM MONITOR PRO - 2024-03-15 10:30:00
══════════════════════════════════════════════════
🔴 CPU:          92.5%
🟢 Memory:       67.3% (8.2 GB)
🟢 Disk:         45.2% (128.5 GB free)
📊 Processes:    342
──────────────────────────────────────────────────
🚨 ALERTS:
   • High CPU: 92.5%
```

## ⚙️ **Configuration**

### **Alert Thresholds**
Edit `monitor.py` to customize alert thresholds:
```python
self.alerts = {
    "cpu": 80,      # Alert if CPU > 80%
    "memory": 85,   # Alert if Memory > 85%
    "disk": 90      # Alert if Disk > 90%
}
```

### **Logging Configuration**
- Logs are stored in `logs/system_monitor.csv`
- CSV format for easy import into Excel/Google Sheets/Pandas
- Automatic directory creation
- Timestamp format: `YYYY-MM-DD HH:MM:SS`

### **Monitoring Intervals**
- Default interval: 5 seconds
- Configurable via command line: `python monitor.py start 10`

## 🔧 **Automation & Scheduling**

### **Cron Job (Linux/macOS)**
Set up automatic monitoring with cron:
```bash
# Open crontab editor
crontab -e

# Add this line to run every 5 minutes
*/5 * * * * cd /path/to/system-monitor-pro && python3 monitor.py once >> logs/cron.log 2>&1

# Run every hour
0 * * * * cd /path/to/system-monitor-pro && python3 monitor.py once >> logs/hourly.log 2>&1
```

### **Systemd Service (Linux)**
Create a system service for 24/7 monitoring:
```bash
# Create service file
sudo nano /etc/systemd/system/system-monitor.service

# Add configuration:
[Unit]
Description=System Monitor Pro
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/system-monitor-pro
ExecStart=/usr/bin/python3 /path/to/system-monitor-pro/monitor.py start 30
Restart=always

[Install]
WantedBy=multi-user.target

# Enable and start the service
sudo systemctl enable system-monitor
sudo systemctl start system-monitor
```

### **Task Scheduler (Windows)**
```powershell
# Create a scheduled task
$action = New-ScheduledTaskAction -Execute "python.exe" -Argument "monitor.py once" -WorkingDirectory "C:\path\to\system-monitor-pro"
$trigger = New-ScheduledTaskTrigger -Daily -At "9:00AM"
Register-ScheduledTask -TaskName "SystemMonitor" -Action $action -Trigger $trigger
```

## 📁 **Project Structure**

```
system-monitor-pro/
├── monitor.py              # Main application entry point
├── setup.sh                # Automated setup script
├── README.md               # This documentation file
├── .gitignore              # Git ignore patterns
├── logs/                   # Log directory (auto-generated)
   └── system_monitor.csv  # CSV log file
```

### **File Descriptions**

1. **monitor.py** - Core application with SystemMonitor class, command-line interface, and main logic
2. **setup.sh** - Bash script for automated environment setup
3. **README.md** - Comprehensive project documentation
4. **.gitignore** - Patterns to exclude from version control
5. **logs/** - Directory for CSV log files (auto-created)

## 🧪 **Testing**

### **Running Tests**
```bash
# Run basic functionality test
python -c "import psutil; print('✅ psutil installed')"

# Test monitor functionality
python monitor.py once

# Test error handling
python monitor.py invalid-command
```

### **Manual Test Scenarios**
1. **Normal operation**: `python monitor.py once`
2. **High load simulation**: Run stress tests while monitoring
3. **Disk space test**: Fill disk to trigger alerts
4. **Long-running test**: `python monitor.py start 5 60` (1 minute)
5. **Data validation**: Check CSV output format

## 🎓 **Skills Demonstrated**

### **Core Technical Skills**
| Skill | How Demonstrated | Relevance to DataOps |
|-------|-----------------|---------------------|
| **Python Scripting** | Complete application with classes, functions, error handling | Essential for automation and tooling |
| **Linux/Unix Systems** | Bash scripting, cron jobs, system monitoring | Core requirement for DataOps roles |
| **Git Version Control** | Project structure, .gitignore, commit history | Collaboration and code management |
| **System Monitoring** | Resource tracking, alerting, logging | Fundamental DataOps responsibility |
| **Data Management** | CSV logging, data collection, analysis | Data pipeline basics |

### **Software Engineering Practices**
- **Modular Design**: Separate concerns in classes and functions
- **Error Handling**: Graceful degradation and informative messages
- **Configuration Management**: Centralized settings and thresholds
- **Documentation**: Comprehensive README and inline comments
- **User Experience**: Intuitive CLI with help system

### **DevOps/DataOps Concepts**
- **Infrastructure Monitoring**: System resource tracking
- **Automation**: Scripted setup and scheduled execution
- **Logging & Observability**: Structured data collection
- **Alerting**: Threshold-based notifications
- **Tool Development**: Building internal utilities

## 💡 **Extension Ideas**

1. **Web Dashboard**: Add Flask/FastAPI backend with React frontend
2. **Database Integration**: Store metrics in PostgreSQL/InfluxDB
3. **Notification System**: Email/Slack alerts for critical issues
4. **Dockerization**: Containerize for easy deployment
5. **REST API**: Expose metrics via API for integration
6. **Historical Analysis**: Add trending and prediction features
7. **Multi-system Monitoring**: Monitor multiple servers simultaneously
8. **Configuration File**: YAML/JSON config instead of hardcoded values

### **Quick Enhancements You Can Add**
```python
# 1. Add email alerts
import smtplib
def send_alert(email, subject, message):
    # Implementation here
    pass

# 2. Add database logging
import sqlite3
def log_to_database(metrics):
    conn = sqlite3.connect('metrics.db')
    # Implementation here
    pass

# 3. Add web server
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/metrics')
def get_metrics():
    return jsonify(collect_metrics())
```

## 🤝 **Contributing**

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### **Development Setup**
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt  # If you create one

# Run tests
python -m pytest tests/
```

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**MIT License Summary:**
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ License and copyright notice must be included

## 👨‍💻 **Author**

**Your Name** - DataOps Aspirant

- GitHub: [@YourUsername](https://github.com/YourUsername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Portfolio: [yourportfolio.com](https://yourportfolio.com)

## 🙏 **Acknowledgments**

- **psutil library** by Giampaolo Rodola for cross-platform system monitoring
- **Python community** for excellent documentation and resources
- **DataOps professionals** whose workflows inspired this tool
- **Open source community** for continuous learning opportunities

## 🔗 **Additional Resources**

- [Python Official Documentation](https://docs.python.org/3/)
- [psutil Documentation](https://psutil.readthedocs.io/)
- [Linux Command Line Basics](https://ubuntu.com/tutorials/command-line-for-beginners)
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [DataOps Fundamentals](https://www.datakitchen.io/dataops-fundamentals/)

## 📞 **Support**

For questions, suggestions, or issues:
1. Check the [Issues](https://github.com/YourUsername/system-monitor-pro/issues) page
2. Create a new issue with detailed description
3. Email: your.email@example.com

---

<div align="center">
  
### ⭐ **If you find this project useful, please give it a star!** ⭐

**Built with ❤️ for DataOps aspirants everywhere**

</div>

---

## 📊 **Project Metrics**

![Code Size](https://img.shields.io/github/languages/code-size/YourUsername/system-monitor-pro)
![Last Commit](https://img.shields.io/github/last-commit/YourUsername/system-monitor-pro)
![Open Issues](https://img.shields.io/github/issues/YourUsername/system-monitor-pro)

**Lines of Code:** ~300  
**Files:** 4  
**Dependencies:** 1 (psutil)  
**Test Coverage:** Manual testing only  
**Documentation:** Comprehensive README  
