#Exercise N1
import json
import threading
import time

sample_data = [
    {
        "id": 1,
        "name": "Alice",
        "age": 25,
        "city": "New York",
        "email": "alice@example.com",
        "skills": ["Python", "Java", "C++"],
        "projects": [
            {"name": "Project Alpha", "duration": "6 months"},
            {"name": "Project Beta", "duration": "4 months"}
        ]
    },
    {
        "id": 2,
        "name": "Bob",
        "age": 30,
        "city": "San Francisco",
        "email": "bob@example.com",
        "skills": ["JavaScript", "HTML", "CSS"],
        "projects": [
            {"name": "Website Redesign", "duration": "3 months"},
            {"name": "Mobile App", "duration": "8 months"}
        ]
    },
    {
        "id": 3,
        "name": "Charlie",
        "age": 35,
        "city": "Boston",
        "email": "charlie@example.com",
        "skills": ["Go", "Rust", "Kotlin"],
        "projects": [
            {"name": "Cloud Migration", "duration": "12 months"},
            {"name": "Backend Optimization", "duration": "5 months"}
        ]
    }
]

def write_json_to_file(file_name, data):
    start_time = time.time()
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)
    end_time = time.time() 
    
    elapsed_time = end_time - start_time 
    print(f"thread finished writing to {file_name} in {elapsed_time:.4f} seconds.")

threads = []

for i, data in enumerate(sample_data, start=1):
    file_name = f"Lecture 21 - Threads/sample_{i}.json"
    thread = threading.Thread(target=write_json_to_file, args=(file_name, data), name=f'thread{i}')
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("all threads have completed.")


#Exercise N2

import threading
import queue

def worker(q):
    thread_name = threading.current_thread().name
    while True:
        try:
            num = q.get(timeout=2)
            is_even = num % 2 == 0
            print(f"{thread_name}, value: {num}, even: {is_even}")
            q.task_done()  
        except queue.Empty:
            break

q = queue.Queue()

threads = []

for _ in range(3):
    thread = threading.Thread(target=worker, args=(q,))
    threads.append(thread)
    thread.start()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    q.put(number)

for thread in threads:
    thread.join()

q.join()

print("all tasks completed.")