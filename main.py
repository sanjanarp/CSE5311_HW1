import random
import time
import matplotlib.pyplot as plt
import platform
import psutil

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def benchmark_sorting_algorithms():
    input_sizes = [5, 10, 20, 50, 100, 500, 1000, 5000, 10000]
    insertion_times, selection_times, bubble_times = [], [], []

    for size in input_sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]

        for sort_func, times in zip(
            [insertion_sort, selection_sort, bubble_sort],
            [insertion_times, selection_times, bubble_times],
        ):
            arr_copy = arr.copy()
            start_time = time.time()
            sort_func(arr_copy)
            end_time = time.time()
            times.append(end_time - start_time)

    return input_sizes, insertion_times, selection_times, bubble_times

def plot_results(input_sizes, insertion_times, selection_times, bubble_times):
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, insertion_times, label="Insertion Sort", marker="o")
    plt.plot(input_sizes, selection_times, label="Selection Sort", marker="o")
    plt.plot(input_sizes, bubble_times, label="Bubble Sort", marker="o")

    plt.xlabel("Input Size (n)")
    plt.ylabel("Runtime (seconds)")
    plt.title("Sorting Algorithm Performance")
    plt.legend()
    plt.grid()
    plt.show()

def system_info():
    print("System Specifications:")
    print(f"CPU: {platform.processor()}")
    print(f"Cores: {psutil.cpu_count(logical=False)}")
    print(f"Threads: {psutil.cpu_count(logical=True)}")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")

if __name__ == "__main__":
    system_info()

    input_sizes, insertion_times, selection_times, bubble_times = benchmark_sorting_algorithms()
    plot_results(input_sizes, insertion_times, selection_times, bubble_times)
