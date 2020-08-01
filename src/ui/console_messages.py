def start():
    print("[START] Starting...")

def stop():
    print("[STOP] Exiting...")

def warning(msg: str):
    print(f"[WARNING] {msg}")

def fail(error: Exception or str):
    print(f"[FAIL] {error}")
