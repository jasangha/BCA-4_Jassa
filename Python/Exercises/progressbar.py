import time

toolbar_width = 70

print("\n[", end="")

for i in range(toolbar_width):
    time.sleep(0.05)
    print("#", end="")

print("]\n\nProgress Completed !\n")
