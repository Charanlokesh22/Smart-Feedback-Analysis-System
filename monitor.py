import psutil
from datetime import datetime

def get_system_metrics():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    response_time = psutil.boot_time()
    
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_usage": cpu,
        "memory_usage": memory,
        "uptime_seconds": psutil.boot_time()
    }
