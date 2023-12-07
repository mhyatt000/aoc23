
from tqdm import tqdm

import threading
import time

def update_progress_bar(progress_bar, total, sleep_time):
    for i in range(total):
        time.sleep(sleep_time)  # Simulate work
        progress_bar.update(1)
    progress_bar.close()

# Create tqdm instances
bar1 = tqdm(total=100, desc="Bar 1")
bar2 = tqdm(total=80, desc="Bar 2")
bar3 = tqdm(total=60, desc="Bar 3")

# Create threads for each progress bar
thread1 = threading.Thread(target=update_progress_bar, args=(bar1, 100, 0.1))
thread2 = threading.Thread(target=update_progress_bar, args=(bar2, 80, 0.15))
thread3 = threading.Thread(target=update_progress_bar, args=(bar3, 60, 0.2))

# Start threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()
