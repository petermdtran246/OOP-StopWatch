# ⏱️ Python OOP StopWatch

A precision stopwatch utility built in pure Python.

I designed this project to explore core Object-Oriented Programming (OOP) concepts—specifically **Encapsulation** and **State Management**. The class provides a reliable, fault-tolerant timer that can be started, stopped, resumed, and reset without losing track of accumulated time.

## 🚀 What it does

The `StopWatch` class acts as a state machine that tracks elapsed time down to the microsecond using Python's native `time` module. It includes formatted console output and handles edge cases like double-starting or stopping a paused timer.

## 🧠 Architecture & Design Decisions

While a timer seems simple on the surface, keeping the data strictly accurate requires careful defensive programming.

* **Strict Encapsulation:** Internal state variables (`_start_time` and `_elapsed_time`) are prefixed with an underscore, signaling that they are private. This prevents external code from mutating the timer's internal state directly, ensuring data integrity.

* **State-Aware Guard Clauses:** The `start()` and `stop()` methods use `is None` and `is not None` guard clauses. 
  * If the timer is already running, calling `start()` again is safely ignored rather than overwriting the current timestamp.
  * Calling `stop()` on a paused timer will not crash the application or alter the elapsed time.

* **Dynamic Time Resolution:** The `get_elapsed_time()` method dynamically calculates the correct output based on the current state. If the watch is actively running, it calculates the delta on the fly `(time.time() - self._start_time)` and adds it to the accumulated `_elapsed_time`. If stopped, it simply returns the accumulated time. This ensures accuracy at the exact millisecond the method is called.

* **Lightweight Formatting:** Instead of importing heavy external formatting libraries, the `display_time()` method uses fundamental arithmetic (integer division `//` and modulo `%`) combined with f-string formatting to convert raw seconds into a clean `hh:mm:ss.ss` display.

## 💻 Quick Start

### Prerequisites

* Python 3.x (Zero external dependencies)

### Usage Example

```python
import time
from stopwatch import StopWatch

# Initialize the timer
timer = StopWatch()

# Start tracking time
timer.start()

# Simulate a process taking time
time.sleep(2.5)

# Pause the timer
timer.stop()

# Display the formatted result
timer.display_time() 
# Output: 00:00:02.50

# Retrieve raw seconds for further calculations
raw_seconds = timer.get_elapsed_time()
print(f"Raw seconds: {raw_seconds}")
```

## 🔮 Future Improvements

1. **Context Manager Support:** Implement `__enter__` and `__exit__` dunder methods so the stopwatch can be used cleanly in a `with` block to measure the execution time of specific code chunks automatically.
2. **Lap Tracking:** Add a `lap()` method and an internal list to record intermediate timestamps without stopping the main timer.
3. **High-Performance Counter:** Migrate from `time.time()` to `time.perf_counter()` to avoid potential issues with system clock updates and ensure the highest available resolution for benchmarking code.
