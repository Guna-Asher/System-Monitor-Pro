#!/usr/bin/env python3
"""
System Monitor Pro - Simple but powerful system monitoring tool
Perfect for DataOps internship preparation
"""

import psutil
import time
import os
from datetime import datetime
import sys

class SystemMonitor:
    def __init__(self):
        self.log_file = "logs/system_monitor.csv"
        self.alerts = {
            "cpu": 80,      # Alert if CPU > 80%
            "memory": 85,   # Alert if Memory > 85%
            "disk": 90      # Alert if Disk > 90%
        }
        
    def collect_metrics(self):
        """Collect system metrics with error handling"""
        try:
            # Get system metrics
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            return {
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'cpu': round(cpu_percent, 1),
                'memory_percent': round(memory.percent, 1),
                'memory_gb': round(memory.used / (1024**3), 2),
                'disk_percent': round(disk.percent, 1),
                'disk_free_gb': round(disk.free / (1024**3), 2),
                'process_count': len(psutil.pids())
            }
        except Exception as e:
            print(f"Error collecting metrics: {e}")
            return None
    
    def check_alerts(self, metrics):
        """Check if any metrics exceed alert thresholds"""
        alerts = []
        
        if metrics['cpu'] > self.alerts['cpu']:
            alerts.append(f"High CPU: {metrics['cpu']}%")
        
        if metrics['memory_percent'] > self.alerts['memory']:
            alerts.append(f"High Memory: {metrics['memory_percent']}%")
        
        if metrics['disk_percent'] > self.alerts['disk']:
            alerts.append(f"Low Disk: {metrics['disk_percent']}%")
        
        return alerts
    
    def log_metrics(self, metrics):
        """Log metrics to CSV file"""
        # Create logs directory if it doesn't exist
        os.makedirs("logs", exist_ok=True)
        
        # Create header if file doesn't exist
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("timestamp,cpu_percent,memory_percent,memory_gb,disk_percent,disk_free_gb,process_count\n")
        
        # Append metrics
        with open(self.log_file, 'a') as f:
            f.write(f"{metrics['timestamp']},{metrics['cpu']},{metrics['memory_percent']},{metrics['memory_gb']},{metrics['disk_percent']},{metrics['disk_free_gb']},{metrics['process_count']}\n")
        
        return self.log_file
    
    def display_dashboard(self, metrics, alerts):
        """Display system dashboard"""
        print("\n" + "═" * 50)
        print(f"🖥️  SYSTEM MONITOR PRO - {metrics['timestamp']}")
        print("═" * 50)
        
        # CPU Status
        cpu_icon = "🔴" if metrics['cpu'] > self.alerts['cpu'] else "🟢"
        print(f"{cpu_icon} CPU:          {metrics['cpu']:>6}%")
        
        # Memory Status
        mem_icon = "🔴" if metrics['memory_percent'] > self.alerts['memory'] else "🟢"
        print(f"{mem_icon} Memory:       {metrics['memory_percent']:>6}% ({metrics['memory_gb']:>6} GB)")
        
        # Disk Status
        disk_icon = "🔴" if metrics['disk_percent'] > self.alerts['disk'] else "🟢"
        print(f"{disk_icon} Disk:         {metrics['disk_percent']:>6}% ({metrics['disk_free_gb']:>6} GB free)")
        
        # Process Count
        print(f"📊 Processes:    {metrics['process_count']:>6}")
        
        print("─" * 50)
        
        # Show alerts if any
        if alerts:
            print("🚨 ALERTS:")
            for alert in alerts:
                print(f"   • {alert}")
        
        # Show log file info
        if os.path.exists(self.log_file):
            file_size = os.path.getsize(self.log_file) / 1024  # Size in KB
            print(f"\n📝 Log file: {self.log_file} ({file_size:.1f} KB)")
    
    def run_once(self):
        """Run monitoring once"""
        print("🔍 Collecting system metrics...")
        
        metrics = self.collect_metrics()
        if not metrics:
            return False
        
        alerts = self.check_alerts(metrics)
        self.display_dashboard(metrics, alerts)
        
        log_file = self.log_metrics(metrics)
        print(f"\n✅ Metrics logged to: {log_file}")
        
        return True
    
    def run_continuous(self, interval=5):
        """Run monitoring continuously"""
        print(f"🔄 Starting continuous monitoring (Interval: {interval}s)")
        print("Press Ctrl+C to stop\n")
        
        try:
            count = 0
            while True:
                count += 1
                print(f"\n📊 Check #{count}")
                print("─" * 30)
                
                self.run_once()
                
                if count > 1:  # Don't wait after first check
                    print(f"\n⏳ Next check in {interval} seconds...")
                    time.sleep(interval)
                    
        except KeyboardInterrupt:
            print("\n\n🛑 Monitoring stopped by user")
        except Exception as e:
            print(f"\n❌ Error: {e}")
    
    def show_summary(self):
        """Show summary of logged data"""
        if not os.path.exists(self.log_file):
            print("No log file found. Run monitor first.")
            return
        
        print("\n📈 DATA SUMMARY")
        print("─" * 30)
        
        try:
            with open(self.log_file, 'r') as f:
                lines = f.readlines()
            
            if len(lines) > 1:
                data_count = len(lines) - 1  # Subtract header
                print(f"Total records: {data_count}")
                
                # Show first and last timestamp
                first = lines[1].split(',')[0]
                last = lines[-1].split(',')[0]
                print(f"First entry: {first}")
                print(f"Last entry:  {last}")
            else:
                print("Log file is empty")
                
        except Exception as e:
            print(f"Error reading log file: {e}")


def main():
    """Main function with command line options"""
    monitor = SystemMonitor()
    
    # Simple command line interface
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "once":
            monitor.run_once()
        elif command == "start":
            interval = 5
            if len(sys.argv) > 2 and sys.argv[2].isdigit():
                interval = int(sys.argv[2])
            monitor.run_continuous(interval)
        elif command == "summary":
            monitor.show_summary()
        elif command == "help":
            show_help()
        else:
            print(f"Unknown command: {command}")
            show_help()
    else:
        # Default: interactive mode
        show_menu(monitor)


def show_menu(monitor):
    """Show interactive menu"""
    print("\n" + "═" * 40)
    print("   SYSTEM MONITOR PRO - Main Menu")
    print("═" * 40)
    
    print("\n1. Run once")
    print("2. Run continuously")
    print("3. Show data summary")
    print("4. Check system requirements")
    print("5. Exit")
    
    try:
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == "1":
            monitor.run_once()
        elif choice == "2":
            interval = input("Enter interval in seconds (default: 5): ").strip()
            interval = int(interval) if interval.isdigit() else 5
            monitor.run_continuous(interval)
        elif choice == "3":
            monitor.show_summary()
        elif choice == "4":
            check_requirements()
        elif choice == "5":
            print("\n👋 Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")
            
        input("\nPress Enter to continue...")
        show_menu(monitor)
        
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
        sys.exit(0)


def check_requirements():
    """Check system requirements"""
    print("\n🔧 SYSTEM REQUIREMENTS CHECK")
    print("─" * 30)
    
    # Check Python version
    python_version = sys.version_info
    print(f"Python: {'✅' if python_version.major == 3 and python_version.minor >= 6 else '❌'} Version {sys.version.split()[0]}")
    
    # Check psutil
    try:
        import psutil
        psutil_version = psutil.__version__
        print(f"psutil: ✅ Version {psutil_version}")
    except ImportError:
        print("psutil: ❌ Not installed")
    
    # Check logs directory
    if os.path.exists("logs"):
        print("Logs dir: ✅ Exists")
    else:
        print("Logs dir: ⚠️ Will be created automatically")
    
    print("\n✅ System check complete!")


def show_help():
    """Show help message"""
    print("\n📖 SYSTEM MONITOR PRO - Help")
    print("─" * 40)
    print("\nUsage:")
    print("  python monitor.py               # Interactive menu")
    print("  python monitor.py once          # Run once and exit")
    print("  python monitor.py start [5]     # Run continuously (5 sec interval)")
    print("  python monitor.py summary       # Show logged data summary")
    print("  python monitor.py help          # Show this help")
    
    print("\nFeatures:")
    print("  • Monitors CPU, Memory, Disk usage")
    print("  • Logs data to CSV file (logs/system_monitor.csv)")
    print("  • Alert system for high usage")
    print("  • Interactive menu and command line")
    
    print("\nDependencies:")
    print("  • Python 3.6+")
    print("  • psutil library (install with: pip install psutil)")


if __name__ == "__main__":
    # Check if psutil is installed
    try:
        import psutil
        main()
    except ImportError:
        print("❌ psutil library is required!")
        print("\nInstall it with:")
        print("  pip install psutil")
        print("\nThen run:")
        print("  python monitor.py")
        sys.exit(1)