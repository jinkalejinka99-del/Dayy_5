import os
import socket
import datetime
import getpass

print("=== SYSTEM INFO ===")
print("Time:", datetime.datetime.now())
print("Hostname:", socket.gethostname())
print("Current Files:", os.listdir())
print("User:", getpass.getuser())
