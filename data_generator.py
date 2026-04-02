import time
import csv

# -----------------------------
# Test Program
# -----------------------------
def test_program(input_size, loop_iterations):
    total = 0
    for _ in range(loop_iterations):
        for i in range(input_size):
            for _ in range(200):   # increase workload
                total += i
    return total

# -----------------------------
# Measure Function (averaging)
# -----------------------------
def measure(input_size, loops, runs=5):
    times = []
    for _ in range(runs):
        start = time.perf_counter()
        test_program(input_size, loops)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)

# -----------------------------
# Main
# -----------------------------
data = []

for input_size in range(100, 2000, 100):
    for loops in range(1, 20):
        exec_time = measure(input_size, loops)
        exec_time_ms = exec_time * 1000
        data.append([input_size, loops, exec_time_ms])

# -----------------------------
# Save CSV
# -----------------------------
with open("../data/execution_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["input_size", "loop_iterations", "execution_time"])
    writer.writerows(data)

print("\nDataset generated successfully!")