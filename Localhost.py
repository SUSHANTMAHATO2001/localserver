import os

port = 8080

if port == 8080:
    print(f"Starting server on port {port}...")
    os.system(f"python3 -m http.server {port}")
else:
    print("Port not allowed!")
