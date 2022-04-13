from vidstream import CameraClient
from vidstream import StreamingServer

import threading
import time
toolbar_width = 70

receiving = StreamingServer('192.168.43.65', 8080)  # port=8080)
sending = CameraClient('192.168.43.65', 8080)

t1 = threading.Thread(target=receiving.start_server)
t1.start()

print("\n[", end="")
for i in range(toolbar_width):
    time.sleep(0.05)
    print("#", end="")
print("]\n")

t2 = threading.Thread(target=sending.start_stream)
t2.start()

while input("") != "stop":
    continue

receiving.stop_server()
sending.stop_stream()
