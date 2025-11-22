import logging, os

LOG_PATH = os.path.expanduser("~/.sinai/logs")
os.makedirs(LOG_PATH, exist_ok=True)
LOG_FILE = os.path.join(LOG_PATH, "server.log")

def init_logging():
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                        format="%(asctime)s [%(levelname)s] %(message)s")

def log_info(msg:str): logging.info(msg)
def log_error(msg:str): logging.error(msg)
