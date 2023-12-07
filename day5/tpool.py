
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
import time

def update_progress_bar(index, total, sleep_time):
    progress_bar = tqdm(total=total, desc=f"Bar {index}")
    for i in range(total):
        time.sleep(sleep_time)
        progress_bar.update(1)
    progress_bar.close()

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(update_progress_bar, 1, 100, 0.1)
    executor.submit(update_progress_bar, 2, 80, 0.15)
    executor.submit(update_progress_bar, 3, 60, 0.2)
