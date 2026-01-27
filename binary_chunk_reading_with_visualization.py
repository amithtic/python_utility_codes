import struct
import matplotlib.pyplot as plt
from IPython.display import clear_output
import time

start = 0
num_floats = 4000
frame_size = num_floats * 4

raw_file = r'input binary file'

with open(raw_file, 'rb') as f:
    while True:
        f.seek(start)
        frame_data = f.read(frame_size)

        if len(frame_data) != frame_size:
            break

        frame = struct.unpack(f'>{num_floats}f', frame_data)

        clear_output(wait=True)   # clears previous plot
        plt.figure(figsize=(8, 4))
        plt.plot(frame)
        plt.title(f"Frame starting at byte {start}")
        plt.show()

        start += frame_size
        time.sleep(0.033)  # optional: control refresh speed
