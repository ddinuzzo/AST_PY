"""Countdown da 10"""
import time
# Numero di partenza
count = 10
for i in range(count, 0, -1):
    print(i, end="...")
    time.sleep(1)
print("vai!")
