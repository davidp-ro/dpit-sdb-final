def start() -> None:
    """
    Show the start message
    """
    print("[START] Starting...")

def stop() -> None:
    """
    Show the stop message
    """
    print("[STOP] Exiting...")

def warning(msg: str) -> None:
    """
    Show a warning message

    Args:
        msg (str): The message
    """
    print(f"[WARNING] {msg}")

def fail(error: Exception or str) -> None:
    """
    Show a fail message

    Args:
        error (Exception or str): The message or Exception
    """
    print(f"[FAIL] {error}")
