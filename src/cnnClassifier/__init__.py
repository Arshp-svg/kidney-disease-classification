import os
import sys
import logging

logger_str = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
logs_dir="logs"
log_file_path=os.path.join(logs_dir, "running_logs.log")

os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(level=logging.INFO, format=logger_str, handlers=[logging.StreamHandler(sys.stdout), logging.FileHandler(log_file_path)])
logger = logging.getLogger("CNNlogger")