import psutil
from datetime import datetime

def get_system_info():
    """Collects current CPU, memory, and disk usage."""
    cpu_percent = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    return cpu_percent, memory.percent, disk.percent

def format_log_line(cpu, memory, disk):
    """Formats the system info into a log line with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"

def append_to_log(line):
    """Appends a log line to log.txt."""
    with open("log.txt", "a") as file:
        file.write(line + "\n")

def main():
    cpu, memory, disk = get_system_info()
    log_line = format_log_line(cpu, memory, disk)
    print(log_line)
    append_to_log(log_line)

if __name__ == "__main__":
    main()
