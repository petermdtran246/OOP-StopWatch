import time

class StopWatch:
  def __init__(self):
    self._start_time = None
    self._elapsed_time = 0

  def start(self):
    if self._start_time is None:
      self._start_time = time.time()

  def stop(self):
    if self._start_time is not None:
      time_period = time.time() - self._start_time
      self._elapsed_time += time_period
      self._start_time = None

  def reset(self):
    self._start_time = None
    self._elapsed_time = 0

  def get_elapsed_time(self):
    if self._start_time is None:
      # Case 1: The watch is stopped
      return self._elapsed_time
    else:
      # Case 2: The clock is still running
      return self._elapsed_time + (time.time() - self._start_time)

  def display_time(self):
    total_seconds = self.get_elapsed_time()

    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = total_seconds % 60

    formatted_time = f"{hours:02d}:{minutes:02d}:{seconds:05.2f}"
    print(formatted_time)
    return

timer = StopWatch()
timer.start()
time.sleep(2)
timer.stop()
timer.display_time()
print(timer.get_elapsed_time())