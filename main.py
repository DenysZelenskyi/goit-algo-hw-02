import queue
import time
import threading
import random

request_queue = queue.Queue()

def generate_request():
    while True:
        request_id = int(time.time() * 10)
        request_queue.put(request_id)
        print(f"Заявка {request_id} була додана до черги")
        time.sleep(random.uniform(0.5, 2)) 

def process_request():
    while True:
        if not request_queue.empty():
            request_id = request_queue.get()
            print(f"Заявка {request_id} була оброблена")
        else:
            print("Черга пуста")
        time.sleep(random.uniform(1, 3)) 

generator_thread = threading.Thread(target=generate_request)
processor_thread = threading.Thread(target=process_request)

generator_thread.start()
processor_thread.start()

generator_thread.join()
processor_thread.join()