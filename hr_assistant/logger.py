import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

log_filename = datetime.now().strftime("hr_assistant_%Y%m%d_%H%M%S.log")
log_filepath = os.path.join(LOGS_DIR, log_filename)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("hr_assistant")