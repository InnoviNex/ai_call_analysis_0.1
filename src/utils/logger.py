from datetime import datetime

def log_info(message):
    print(message)
    with open("logs/log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[INFO] {datetime.now()}: {message}\n")

def log_error(message):
    print(message)
    with open("logs/log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"[ERROR] {datetime.now()}: {message}\n")