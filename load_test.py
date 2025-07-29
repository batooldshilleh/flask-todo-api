import requests
from multiprocessing import Pool
import time

URL = "http://localhost:8000/items"

def send_post(i):
    task = {"task": f"LoadTest task {i}"}
    response = requests.post(URL, json=task)
    return response.status_code

if __name__ == "__main__":
    start = time.time()

    NUM_REQUESTS = 50  # عدد الطلبات المتزامنة
    with Pool(10) as p:  # عدد العمليات المتوازية
        results = p.map(send_post, range(NUM_REQUESTS))

    end = time.time()

    print(f"✅ Done. Sent {NUM_REQUESTS} requests in {end - start:.2f} seconds.")
    print(f"Results summary: {results.count(201)} successful, {results.count(200)} duplicates, {results.count(500)} errors")
