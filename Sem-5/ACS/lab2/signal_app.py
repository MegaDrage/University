import signal
import time
import sys

def signal_handler(sig, frame):
    print(f"Received signal {sig}. Exiting...")
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_handler)
signal.signal(signal.SIGINT, signal_handler)

print("Application is running. Press Ctrl+C to exit or send SIGTERM.")

while True:
    time.sleep(1)
