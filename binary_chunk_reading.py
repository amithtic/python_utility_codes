raw_file = 'C:/Users/gupta/HTIC/demo_binary_code/1_7_ 410_1465_PLRAW.sgl'

import struct
import numpy as np
import matplotlib.pyplot as plt

# Open the binary file
with open(raw_file, 'rb') as f:
  # Read one frame of data (4000 samples x 4 bytes per sample)
  frame_data = f.read(4000 * 4)

# Convert the binary data to a list of 4000 floats
frame = struct.unpack('>4000f', frame_data)

# print frame data
print(frame)

# Plot the frame
plt.plot(frame)
plt.show()
